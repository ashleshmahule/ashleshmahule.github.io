import pandas as pd
from flask import Flask, request, jsonify, render_template

rating_col = ['user_id', 'coffee_id', 'rating']
ratings = pd.read_csv(r'''data.csv''', names=rating_col, usecols=range(3), encoding="ISO-8859-1")

movie_col = ['coffee_id', 'type']
movies = pd.read_csv(r'''item.csv''', names=movie_col, usecols=range(2), encoding="ISO-8859-1")

ratings = pd.merge(movies, ratings)

userRatings = ratings.pivot_table(index=['user_id'], columns=['type'], values='rating')
print(userRatings.head(20))

corrMatrix = userRatings.corr(method='pearson', min_periods=2)
print(corrMatrix)

type1 = 'Cappuccino'
rate1 = '2'
type2 = 'Espresso'
rate2 = '3'

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

print(result)
