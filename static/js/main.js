
let x = 0;

let slider = document.getElementById("slider");

let nextButton = document.getElementById("next");

let prevButton = document.getElementById("prev");
console.log("hello world"); 
console.log("fuziona");
console.log(x)
console.log(slider.offsetWidth );
console.log(window.innerWidth);
// console.log(nextButton.);
nextButton.onclick = translateToRight   
prevButton.onclick = translateToLeft

function translateToRight() {
    console.log("to right")
    if (checkerRight()) {
        console.log("x + 208");
        x -= 200
        slider.style.transform = `translateX(${x}px)`
    }
   
}

function translateToLeft() {
    console.log("to left")
    if (checkerLeft()) {
        x += 208 
        slider.style.transform = `translateX(${x}px)`
    }
}
function checkerLeft() {
    if (x + 200 >= 0)  {

        prevButton.setAttribute('disabled', '')
        x = 0
        return false
     } else {

         nextButton.removeAttribute('disabled')
         return true
     } 
    
}

function checkerRight() {
    if (x - 100 <= -(slider.offsetWidth - window.innerWidth)){
        nextButton.setAttribute('disabled', '')
        x = -(slider.offsetWidth - window.innerWidth)
        return false
    } else {
        prevButton.removeAttribute('disabled')        
        return true
    }
}