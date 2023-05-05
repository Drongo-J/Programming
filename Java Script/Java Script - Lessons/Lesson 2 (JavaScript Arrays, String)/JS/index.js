

// function main(){

//     // let mylist=document.getElementById("myList");
//     // let count=Number(prompt("Enter list count : "));

//     // let content="";
//     // let style=" style='background-color:rgb(";
//     // let number=50;
//     // for (let i = 0; i < count; i++) {
//     //     content+="<li ";
//     //     content+=style;
//     //     content+=number+",0,0)'>";
//     //     content+=i+1;
//     //     content+="</li>";  
//     //     number+=10; 
//     // }
//     // mylist.innerHTML=content;


//     // let fruits=["Banana","Orange","Apple","Mango"];

//     // fruits.forEach(f=>alert(f));

//         let mytable=document.getElementById("myTable");
//         let content="";
//         let id=1;
//         for (let i = 0; i < 3; i++) {
//             content+="<tr>";
//             for (let k = 0; k < 3; k++) {
//                 let number=getRandom(10);
//                 numbers.push(number);
//                 content+=`
//                 <td id='${id}' onclick='show(id)'>
//                     ${number}
//                     </td>
//                 `;
//                 ++id;
//             }
//             content+="</tr>";
//         }

//         console.log(numbers);
//         mytable.innerHTML=content;

// }
// var comp_number=getRandom(10);
// var numbers=[];
// function getRandom(max){
//     return Math.floor(Math.random()*max);
// }

// var counter=0;
// function show(id){
//     ++counter;
//     let element=document.getElementById(id);
//     if(numbers[comp_number]==Number(element.innerHTML)){
//         element.style.backgroundColor="#00ff7f";
//         alert("You Won");
//     }
//     else{
//         element.style.backgroundColor="red";
//     }
//     if(counter>=3){
//         alert("you lost");
//         main();
//     }
// }
// main();



let numbers = [];
function main() {

    let mytable = document.getElementById("myTable");
    let content = "";
    for (let i = 0; i < 4; i++) {
        content += "<tr>";
        let subnumbers = [];
        for (let k = 0; k < 4; k++) {
            let id = `${i + 1}${k + 1}`;
            let number = getRandom(100);
            subnumbers.push(number);
            content += `
                <td id='${id}' onclick='show(id)'>   
                    </td>
                `;
        }
        numbers.push(subnumbers);
        content += "</tr>";
    }
    console.log(numbers);
    mytable.innerHTML = content;





}

function getRandom(max) {
    return Math.floor(Math.random() * max);
}

function show(id) {
    let stringId = String(id);
    const row = Number(stringId[0]) - 1;
    const col = Number(stringId[1]) - 1;
    let data = numbers[row][col];
    let element = document.getElementById(id);
    setTimeout(() => {
        element.innerHTML = data;
    }, 50);
}
main();

function MyTimer(){
    let date=new Date();
    let myTitle=document.getElementById("myTitle");
    myTitle.innerHTML=date.toLocaleTimeString();
}
var clear;

function Start(){
    clear=setInterval(() => {
        MyTimer();
    }, 1000);
}


function Stop(){
    clearTimeout(clear);
}