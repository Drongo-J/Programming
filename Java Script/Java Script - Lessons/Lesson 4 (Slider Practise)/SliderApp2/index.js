var myimage = document.getElementById("myimg");
myimage.style.transitionProperty = "margin-left";
myimage.style.transitionDuration = "2s";

myimage.style.marginLeft = "0px";

var index = 1;
var max=4;
setInterval(() => {
    myimage.style.marginLeft = `-${index * 650}px`;
    index++;
    if(index==max){
        index=0;
    }
}, 2000);