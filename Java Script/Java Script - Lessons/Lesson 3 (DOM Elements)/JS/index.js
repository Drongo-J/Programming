
// let person={
//     firstName:"John",
//     lastName:"Johnlu",
//     age:50,
//     score:98.7,
//     cars:[
//         {vendor:"Ford",model:"Mustang"},
//         {vendor:"Chevrolet",model:"Malibu"},
//         {vendor:"Ferrari",model:"F12 Berlinetta"},
//     ],
//     Fullname:function(){
//         return this.firstName+" "+this.lastName;
//     }
// };
// //person["firstName"]="Elvin";
// // person.cars.push({vendor:"Mercedes",model:"GL-500"});
// // console.log(person);

// // delete person.firstName;
// let demo=document.getElementById("demo");

// let content='';

// for(let key in person){
//     if(key!='cars' && key!='Fullname'){
//         content+=`<li><h1>${key+" : "+person[key]}
//                     </h1></li>`;
//     }
//     else if(key=='cars'){
//         content+=`<li><h1>CARS</h1><ul>`;
//         let mycars=person.cars;
//         mycars.forEach((car)=>{
//                 content+=`<li>
//                 ${car.model+"  -  "+car.vendor}</li>`;
//         });
//         content+=`</ul></li>`
//     }
// }

// demo.innerHTML=content;



class Student{
    constructor(name,surname){
        this.name=name;
        this.surname=surname;
    }

    fullname(){
        return this.name+" "+this.surname;
    }

    static hello(){
        alert("Hi");
    }
}

// let student=new Student("Mike","Mammadov");
// console.log(student.name);
// console.log(student.surname);
// console.log(student.fullname());
// Student.hello();



// function changeAll(){
//     let elements=document.getElementsByTagName("h1");
//     console.log(elements);
//     for (let i = 0; i < elements.length; i++) {
//         const element = elements[i];
//         element.style.color="springgreen";
//     }
// }




// function changeAll(){
//     let elements=document.getElementsByClassName("mytitle");
//     console.log(elements);
//     for (let i = 0; i < elements.length; i++) {
//         const element = elements[i];
//         element.style.color="springgreen";
//     }


// }




// function set(){
//     // let first=document.querySelector("h1");
//     // first.style.color="blue";

//      let all=document.querySelectorAll("h1");
//      for (let i = 0; i < all.length; i++) {
//         const element = all[i];
//         element.addEventListener(("onclick"),function(e){
//         });
//      }
//     // all.forEach((e)=>{
//     //     e.style.boxShadow="0 0 10px 10px red";
//     // });

//     // let second=document.querySelector("#second");
//     // console.log(second.nextElementSibling);
//     // second.nextElementSibling.style.color="red";
//     // second.previousElementSibling.style.color="green";

// }


// let myTitle=document.querySelector("h1");
// let element=document.createElement("h2");
// element.innerHTML="Hi Guys";
// myTitle.appendChild(element);
// setTimeout(() => {
//     myTitle.removeChild(element);
// }, 2000);

let myTitle=document.querySelector("h1");

window.addEventListener("resize", function(){
    document.getElementById("myTitle").innerHTML = `${window.outerWidth}  ${window.outerHeight}`;
    if(this.window.outerWidth>=1000){
        myTitle.addEventListener("click",function(){
                myTitle.style.color="#00bfff";
        });
    }
  });












