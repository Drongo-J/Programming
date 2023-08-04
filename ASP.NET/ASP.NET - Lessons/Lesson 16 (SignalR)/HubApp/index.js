let element=document.querySelector("#offerValue");
const connection = new signalR.HubConnectionBuilder()
    .withUrl("https://localhost:7115/offers")
    .configureLogging(signalR.LogLevel.Information)
    .build();
async function start() {
    try {
        await connection.start();
       

        

        $.get("https://localhost:7115/api/Offer", function(data, status){
            console.log(data);
            element.innerHTML=data;
          });
          
        console.log("SignalR Connected");
    }
    catch (err) {
        console.log(err);
        setTimeout(() => {
            start();
        }, 5000);
    }
}

connection.on("ReceiveMessage",(message)=>{
    let element=document.querySelector("#offerValue2");
        element.innerHTML=message;
       // alert(message);
        console.log(message);
})

connection.onclose(async () => {
    await start();
})

 async function IncreaseOffer(){
    let result=10;
    $.get("https://localhost:7115/Increase?number=100", function(data, status){
        let element=document.querySelector("#offerValue");
        element.innerHTML=data;
        result=data;
    });
    await connection.invoke("SendMessage",result);

            
}

start();