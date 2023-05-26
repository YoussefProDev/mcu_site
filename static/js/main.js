
let x = 0;

let slider = document.getElementsByClassName('slider')
console.log(slider);
let nextButton = document.getElementsByClassName("next");
console.log(nextButton);
let prevButton = document.getElementsByClassName("prev");
console.log(prevButton);
// console.log("hello world"); 
// console.log("fuziona");
// console.log(x)
// console.log(slider.offsetWidth );
// console.log(window.innerWidth);
// console.log(nextButton.);
nextButton.onclick = translateToRight   
prevButton.onclick = translateToLeft
const btn = document.querySelector("button.menu-button");
const menu = document.querySelector(".menu");

// Add Event Listeners
btn.addEventListener("click", () => {
menu.classList.toggle("hidden");
menu.classList.toggle('open-menu')
});
for (let i = 0; i < nextButton.length; i++) {
    nextButton[i].addEventListener('click', translateToRight) 
    prevButton[i].addEventListener('click', translateToLeft) 
    function translateToRight() {
        console.log("to right")
        if (checkerRight(i)) {
            console.log("x + 208");
            x -= 190
            slider[i].style.transform = `translateX(${x}px)`
        }
       
    }
    
    function translateToLeft() {
        console.log("to left")
        if (checkerLeft(i)) {
            x += 190
            slider[i].style.transform = `translateX(${x}px)`
        }
    }
    function checkerLeft() {
        if (x + 80 >= 0)  {
    
            prevButton[i].setAttribute('disabled', '')
            x = 0
            return false
         } else {
    
             nextButton[i].removeAttribute('disabled')
             return true
         } 
        
    }
    
    function checkerRight() {
        if (x - 100 <= -(slider[i].offsetWidth - window.innerWidth)){
            nextButton[i].setAttribute('disabled', '')
            x = -(slider[i].offsetWidth - window.innerWidth)
            return false
        } else {
            prevButton[i].removeAttribute('disabled')        
            return true
        }
    }
}