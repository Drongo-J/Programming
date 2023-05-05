// let jsonText=`
//     {
//         "students":[
//             {"name":"Akif","surname":"Akifli"},
//             {"name":"Leyla","surname":"Eliyeva"},
//             {"name":"Mammad","surname":"Memmedli"},
//             {"name":"Axmed","surname":"Axmedlinsky"}
//         ]
//     }
// `;

// let h1=document.getElementById("demo");

// let obj=JSON.parse(jsonText);
// console.log(obj);

// // h1.innerHTML=obj.students[0].surname;

// obj.students.forEach(s => {
//     h1.innerHTML+=s.name+" - ";
//     h1.innerHTML+=s.surname+"</br>";
// });

// let h1=document.getElementById("demo");

// let student={
//     "name":"John",
//     "surname":"Johnlu",
//     "age":25,
//     "scores":[100,99,98]
// };

// let jsonText=JSON.stringify(student);
// h1.innerHTML=jsonText;

// let studentObj=JSON.parse(jsonText);
// alert(studentObj.age);

// let h1=document.getElementById("demo");

// async function MyFunctionAsync(){
//     //throw "Some Errors";
//     return 1;
// }

// async function ForCallAsync(){
//     let result=await MyFunctionAsync();
//     h1.innerHTML=result;
// }

// ForCallAsync().then(()=>{
//     setTimeout(() => {
//         console.log("Completed callback");
//     }, 2000);
// }).catch((e)=>{
//     console.log(`Error : ${e}`);
// }).finally(()=>{
//     console.log("End");
// });

// let myFunc=(async(e)=>{
    
    // });
    
// let h1 = document.getElementById("demo");
// let spinner=document.getElementById("spinner");

// async function GetCarsCall() {
//   const url = "http://127.0.0.1:5500/api/cars.json";
//   const xhr = new XMLHttpRequest();
//   xhr.open("GET", url, true);
//   xhr.onload = () => {
//     setTimeout(() => {
//       const data = JSON.parse(xhr.responseText);
//       console.log(data);
//       h1.innerHTML = xhr.responseText;
//       h1.innerHTML += "</br><h2 style='color:#00ff7f;'>Success</h2>";
//       spinner.style.display="none";
//     }, 5000);
//   };
//   xhr.send();
// }

// function GetCars() {
//   GetCarsCall()
//     .then(() => {
//         spinner.style.display="block";
//     })
//     .catch((e) => {
//       h1.innerHTML = e;
//     })
//     .finally(() => {
//       console.log("Ended process");
//     });
// }




async function GetMovies(){
    let content="";
    let movie=document.getElementById("movie").value;
    let url=`http://www.omdbapi.com/?apikey=ddee1dae&s=${movie}&plot=full`;
    const xhttp=new XMLHttpRequest();
    xhttp.open('GET',url,true);
    xhttp.onload=()=>{
        const obj=JSON.parse(xhttp.responseText);
        obj.Search.forEach(m => {
            console.log(m);
            content+=`<div class="card m-5" style="width: 18rem;">
            <img class="card-img-top" src="${m.Poster}" alt="Card image cap">
            <div class="card-body">
              <h5 class="card-title">${m.Title}</h5>
              <p class="card-text">Year : ${m.Year}</p>
              <a href="#" class="btn btn-primary">${m.Title}</a>
            </div>
          </div>`;
        });
      let section=document.getElementById("result");
      section.innerHTML=content;
    };
    xhttp.send();
}

async function GetMoviesCall(){
    await GetMovies();
}
let h1 = document.getElementById("demo");
function GetCarsText(){
    const url='http://127.0.0.1:5500/api/car.txt';
    let xhttp=new XMLHttpRequest();
    xhttp.open("GET",url,true);
    xhttp.onload=function(){
        let data=this.response;
        h1.innerHTML=data;
    };
    xhttp.send();
}


