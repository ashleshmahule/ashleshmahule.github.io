import pandas as pd
from flask import Flask, request, jsonify, render_template

app = Flask(__name__,template_folder='',static_folder='/')


@app.route('/')
def home():
    return render_template('cofrecom.html')

@app.route('/about')
def homae():
    return render_template('about.html')


def listToString(s):
    str1 = " "
    return (str1.join(s))

@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    # int_features = [int(x) for x in request.form.values()]

    # final_features = [np.array(int_features)]
    # prediction = model.predict(final_features)

    # output = round(prediction[0], 2)
    rating_col = ['user_id', 'coffee_id', 'rating']
    ratings = pd.read_csv(r'''data.csv''', names=rating_col, usecols=range(3), encoding="ISO-8859-1")

    movie_col = ['coffee_id', 'type']
    movies = pd.read_csv(r'''item.csv''', names=movie_col, usecols=range(2), encoding="ISO-8859-1")

    ratings = pd.merge(movies, ratings)

    userRatings = ratings.pivot_table(index=['user_id'], columns=['type'], values='rating')
    print(userRatings.head(20))

    corrMatrix = userRatings.corr(method='pearson', min_periods=2)
    print(corrMatrix)

    type1 = request.form['ing1']
    rate1 = request.form['ing2']
    type2 = request.form['ing3']
    rate2 = request.form['ing4']

    names = [type1.strip(), type2.strip()]
    myRatings = [rate1.strip(), rate2.strip()]
    myRatings = pd.Series(myRatings, names, dtype='float64')
    print(myRatings)

    simCandidates = pd.Series()
    for i in range(0, len(myRatings.index)):
        sims = corrMatrix[myRatings.index[i]]
        sims = sims.map(lambda x: x * myRatings[i])
        simCandidates = simCandidates.append(sims)

    simCandidates.sort_values(inplace=True, ascending=False)
    print(simCandidates.head(10))

    simCandidates = simCandidates.groupby(simCandidates.index).sum()

    simCandidates.sort_values(inplace=True, ascending=False)
    print(simCandidates.head(10))

    filteredSims = simCandidates.drop(myRatings.index)
    print(filteredSims.head(10))

    result=filteredSims.index[0]

    return render_template('cofrecom.html',
                           prediction_text='We think, making {} would be a good choice for you today! '.format(
                               result))


@app.route('/predict_api', methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
