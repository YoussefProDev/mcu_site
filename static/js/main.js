
let x = 0;

let slider = document.getElementById("slider");

let nextButton = document.getElementById("next");

let prevButton = document.getElementById("prev");
console.log("hello world"); 
nextButton.onclick = translateToRight   
prevButton.onclick = translateToLeft

function translateToRight() {
    if (checkerRight()) {
        console.log("x + 208");
        x -= 208 
    }
    slider.style.transform = `translateX(${x}px)`
}

function translateToLeft() {
    if (checkerLeft()) x += 208 
    slider.style.transform = `translateX(${x}px)`
}
function checkerLeft() {
    if (x + 248 >= 0)  {

        prevButton.setAttribute('disabled', '')
        x = 0
        return false
     } else {

         nextButton.removeAttribute('disabled')
         return true
     } 
    
}
console.log(slider.offsetWidth  );
function checkerRight() {
    if (x - 248 <= -(slider.offsetWidth - window.innerWidth)){
        nextButton.setAttribute('disabled', '')
        x = -(slider.offsetWidth - window.innerWidth)
        return false
    } else {
        prevButton.removeAttribute('disabled')        
        return true
    }
}