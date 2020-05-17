const elems = document.querySelectorAll('.laya-please');
const layer2 = document.querySelector('.layer-2');
const layer3 = document.querySelector('.layer-3');
const layer4 = document.querySelector('.layer-4');
const layer5 = document.querySelector('.layer-5');
const layer6 = document.querySelector('.layer-6');
const layer7 = document.querySelector('.layer-7');
const layer8 = document.querySelector('.layer-8');


setTimeout(function () {
  elems.forEach(function (elem, index) {
    elem.style.animation = "none";
  });
}, 1500);



document.body.addEventListener('mousemove', function (e) {
  if (!e.currentTarget.dataset.triggered) {
    elems.forEach(function (elem, index) {
      if (elem.getAttribute('style')) {
        elem.style.transition = "all .5s";
        elem.style.transform = "none";
      }
    });
  }
  e.currentTarget.dataset.triggered = true;

  let width = window.innerWidth / 2;
  let mouseMoved2 = ((width - e.pageX) / 50);
  let mouseMoved3 = ((width - e.pageX) / 40);
  let mouseMoved4 = ((width - e.pageX) / 30);
  let mouseMoved5 = ((width - e.pageX) / 20);
  let mouseMoved6 = ((width - e.pageX) / 10);
  let mouseMoved7 = ((width - e.pageX) / 5);

  layer3.style.transform = "translateX(" + mouseMoved2 + "px)";
  layer4.style.transform = "translateX(" + mouseMoved3 + "px)";
  layer5.style.transform = "translateX(" + mouseMoved4 + "px)";
  layer6.style.transform = "translateX(" + mouseMoved5 + "px)";
  layer7.style.transform = "translateX(" + mouseMoved6 + "px)";
  layer8.style.transform = "translateX(" + mouseMoved7 + "px)";
});

document.body.addEventListener('mouseleave', function (e) {
  elems.forEach(function (elem, index) {
    elem.style.transition = "all .5s";
    elem.style.transform = "none";
  });
});

document.body.addEventListener('mouseenter', function (e) {
  elems.forEach(function (elem, index) {
    setTimeout(function () {
      elem.style.transition = "none";
    }, 500);
  });
});

var elements = document.getElementsByClassName("column");

var i;
for (i = 0; i < elements.length; i++) {
  elements[i].style.flex = "15%";
}


$('.slider__offset').slick({
  slidesToShow: 3,
  slidesToScroll: 1,
  arrows: true,
  prevArrow: $(".arrow__left"),
  nextArrow: $(".arrow__right"),
  fade: false,
  infinite: true,
  autoplay: true,
  pauseOnHover: true,
  focusOnSelect: true,
  centerPadding: 0,
  slideMargin: 10,
  centerPadding: 0,
  responsive: [{
      breakpoint: 1140,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1,
      }
    },
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1,
      }
    },
    {
      breakpoint: 577,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1,
      }
    }
  ]
});