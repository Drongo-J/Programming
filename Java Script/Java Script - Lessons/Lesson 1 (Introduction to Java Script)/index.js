function CallFunction() {
  //alert(document.body.innerHTML);
  //alert("Hello World");

  console.log("Hello Javascript");
}

// function CallApple(){
//     let appleElement=document.getElementById("apple");
//     appleElement.innerHTML="Apple clicked";
// }

// function CallMango(){
//     let element=document.getElementById("mango");
//     element.innerHTML="Mango clicked";
// }

// function CallWaterMelon(){
//     let element=document.getElementById("waterMelon");
//     element.innerHTML="WaterMelon clicked";
// }

var isClicked = false;
function Call(id) {
  let element = document.getElementById(id);
  if (!isClicked) {
    element.innerHTML = element.innerHTML + " clicked";
  } else {
    let arr = element.innerHTML.split(" ");
    element.innerHTML = arr[0];
  }
  isClicked = !isClicked;
}

let turned = false;
let imageElement = document.getElementById("bulbImage");
function Turn() {
  if (!turned) {
    imageElement.src = "images/on.png";
  } else {
    imageElement.src = "images/off.png";
  }

  turned = !turned;
}

// let x=10;
// let y=20;

function main() {
  //   var name="Tural";
  //   //  alert(x+y);
  //   //document.write(x+y);
  //     // const pi=3.14;
  //     // pi=5;
  //     // console.log(pi);
  //     //let name="Elvin";
  //     if(name=="Tural"){
  //         var name="Elvin";
  //         console.log(name);
  //     }
  //     console.log(name);
  // let name="John";
  //let surname="Johnlu";
  //let data="     salam      ";
  // console.log(data.trim());
  // let info="6f8042c Tural Eliyev";
  // alert(info.substring(0,7));
  // console.log(name+" "+surname);
  // let result="10 + 20";
  // alert(eval(result));
  // let number=10.5;//Number type
  // let name="Salam";//String type
  // let data=NaN;
  // console.log(data);
  // data=100;
  //  +  -  *   /   %  ++   --
  // +=   -=   *=
  //   let number1 = 10;
  //   let number2 = 20;
  //   alert(number1 * number2);
  // >  <  >=  <=  != ==   !==   ===
  // alert(100==100);
  // alert(100==="100");
  // let name=prompt("Enter your name : ");
  // let age=prompt("Enter you age : ");
  // alert("Welcome "+name+" your age is "+age);
  // let num1=Number(prompt("Enter first number : "));
  // let num2=Number(prompt("Enter second number : "));
  // let element=document.getElementById("result");
  // element.innerHTML=num1+"+"+num2+"="+(num1+num2);
  // let data=confirm("Are you a programmer ? ");
  // var headerElement=document.getElementById("result");
  // if(data){
  //     headerElement.innerHTML="You are best programmer";
  //     headerElement.style.color="#00ff7f";
  // }
  // else{
  //     headerElement.innerHTML="You are oout of software";
  //     headerElement.style.color="red";
  // }
}

main();

let isDark = false;
function Turn() {
  let myBody = document.body;
  let header = document.getElementById("header");

  if (!isDark) {
    myBody.classList.remove("light-body");
    myBody.classList.add("dark-body");
    header.classList.remove("light-header");
    header.classList.add("dark-header");
    header.classList.add("animate__zoomInDown");
    header.classList.remove("animate__zoomOutDown");
  } else {
    header.classList.remove("animate__zoomInDown");
    header.classList.add("animate__zoomOutDown");
    myBody.classList.add("light-body");
    myBody.classList.remove("dark-body");
    header.classList.add("light-header");
    header.classList.remove("dark-header");
  }
  isDark = !isDark;
}
