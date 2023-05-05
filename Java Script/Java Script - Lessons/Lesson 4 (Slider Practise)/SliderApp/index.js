var myimage = document.getElementById("myimg");

let l = document.getElementById("left");
let r = document.getElementById("right");

let index = 1;

let min = 1

let max = 4;

left();

function left() {
    if (index > min) {
        index--;
    }
    if (index < max) {
        r.style.display = "inline-block";
    }

    if (index == min) {
        l.style.display = "none";
    }
    else {
        l.style.display = "inline-block";
    }
    myimage.src = `images/${index}.jpg`;
}

function right() {

    if (index < max) {
        index++;
    }
    if (index == max) {
        r.style.display = "none";
    }
    else {
        r.style.display = "inline-block";
    }

    if(index>min){
        l.style.display="inline-block";
    }

    myimage.src = `images/${index}.jpg`;
}

var changed=false;
setInterval(() => {
    if(!changed){
        r.style.color="white";
        l.style.color="white";
    }
    else{
        r.style.color="black";
        l.style.color="black";
    }
    changed=!changed;
}, 1000);



function slider(){
    right();
    if(index==max){
        index=0;
    }
    
}

setInterval(() => {
    slider();
}, 1000);