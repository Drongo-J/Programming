const requestUrl="https://reqres.in/api/users?page=2";


function sendRequest(method,url,body=null){
    return fetch(url)
    .then(response=>{
        return response.json();
    });
}

sendRequest('GET',requestUrl)
.then(d=>{
    console.log(d.data);FillHtmlContent(d.data);
})
.catch(err=>console.log(err));

function FillHtmlContent(data) {
    let container=document.getElementById("container");
    let content="";
    data.forEach(element => {
        content+=`<div style='width:8rem;margin:10px;'>
        <h1>${element.first_name}</h1>
        <img src='${element.avatar}' />
        </div>`
    });
    console.log(content);
    container.innerHTML=content;
}