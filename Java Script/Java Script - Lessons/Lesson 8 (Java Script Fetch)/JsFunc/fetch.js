const requestUrl = "https://jsonplaceholder.typicode.com/users";

function sendRequest(method, url, body = null) {
  return fetch(url).then((response) => {
    return response.json();
  });
}


sendRequest("GET", requestUrl)
  .then((data) => console.log(data))
  .catch((err) => console.log(err));




// function sendRequest(method,url,body=null){
//     const headers={
//         'Content-type':'application/json'
//     };
//     return fetch(url,{
//         method:method,
//         body:JSON.stringify(body),
//         headers:headers
//     })
//     .then(response=>{
//         return response.json();
//     })
// }


// const body ={
//     name:'Elvin',
//     age:26
// };


// sendRequest('POST',requestUrl,body)
// .then(data=>{console.log(data)})
// .catch(err=>console.log(err))
