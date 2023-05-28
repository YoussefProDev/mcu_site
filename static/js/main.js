

const btn = document.querySelector("button.menu-button");
const menu = document.querySelector(".menu");

btn.addEventListener("click", () => {
menu.classList.toggle("hidden");
menu.classList.toggle('open-menu')
});
window.onload = function() {
    var sliderContainers = document.querySelectorAll('.slider-container');
  
    sliderContainers.forEach(function(container) {
      var slider = container.querySelector('.slider');
      var prevButton = container.querySelector('.prev-button');
      var nextButton = container.querySelector('.next-button');
  
      var slides;
      var slideWidth;
      var slideMarginRight;
      var totalSlidesWidth;
      var containerWidth;
      var slidesPerView;
      var maxTranslate;
      var currentTranslate = 0;
  
      function initializeSlider() {
        slides = slider.querySelectorAll('.slide');
        slideWidth = slides[0].offsetWidth;
        slideMarginRight = parseInt(getComputedStyle(slides[0]).marginRight);
        calculateSliderDimensions();
        setSliderWidth();
      }
  
      function calculateSliderDimensions() {
        containerWidth = slider.parentNode.offsetWidth;
        slidesPerView = Math.floor(containerWidth / (slideWidth + slideMarginRight));
        totalSlidesWidth = (slideWidth + slideMarginRight) * slides.length;
        maxTranslate = -(totalSlidesWidth - containerWidth);
        currentTranslate = 0;
      }
  
      function setSliderWidth() {
        slider.style.width = totalSlidesWidth + 'px';
      }
  
      function handleNextSlide() {
        if (currentTranslate > maxTranslate) {
          currentTranslate -= slideWidth + slideMarginRight;
          slider.style.transform = 'translateX(' + currentTranslate + 'px)';
        }
      }
  
      function handlePrevSlide() {
        if (currentTranslate !== 0) {
          currentTranslate += slideWidth + slideMarginRight;
          slider.style.transform = 'translateX(' + currentTranslate + 'px)';
        }
      }
  
      function handleResize() {
        calculateSliderDimensions();
        setSliderWidth();
      }
  
      prevButton.addEventListener('click', handlePrevSlide);
      nextButton.addEventListener('click', handleNextSlide);
      window.addEventListener('resize', handleResize);
  
      initializeSlider();
    });
  };
  