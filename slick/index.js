$('.slider__offset').slick({
  slidesToShow: 3,
  slidesToScroll: 1,
  arrows: true,
  prevArrow: $(".arrow__left"),
  nextArrow: $(".arrow__right"),
  fade: false,
  infinite: true,
  autoplay: true,
  pauseOnHover:true,
  focusOnSelect: true,
  centerPadding: 0,
  slideMargin: 10,
  centerPadding: 0,
  responsive: [
  {
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