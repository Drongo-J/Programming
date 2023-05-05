const requestUrl="https://jsonplaceholder.typicode.com/users";

function sendRequest(method,url,body=null){
    return new Promise((resolve,reject)=>{
        const xhr=new XMLHttpRequest();
        xhr.open(method,url);
        
        xhr.onload=()=>{
            if(xhr.status>=400){
                reject(xhr.response);
            }
            else{
                resolve(xhr.response);
            }
        }

        xhr.onerror=()=>{
            reject(xhr.response);
        }

        xhr.send(body);
    });
}




function FillDataToHtml(response){
    let jsonResult=JSON.parse(response);
    let mytable=document.getElementById("mytable");

    let content="";

    content+=`
    <tr>
    <th>Name</th>
    <th>Username</th>
    <th>Email</th>
    <th></th>
    </tr>
    `;

    jsonResult.forEach(e => {
        content+=`
        <tr>
        <td>${e.name}</td>
        <td>${e.username}</td>
        <td>${e.email}</td>
       <td>
       <button onclick='MyDelete(${e.id})'>Delete</button>
       </td>
        </tr>
        `;
    });


    mytable.innerHTML=content;
}



sendRequest('GET',requestUrl)
.then(data=>{
    FillDataToHtml(data);
    console.log(data)})
.catch(err=>console.log(err));