// let timeSection = document.querySelector("#time-section");
// let button = document.querySelector("#offerBtn");
// let element = document.querySelector("#offerValue");
// var totalseconds = 10;
// var clearInterval;
// var CURRENTROOM="";


// const connection = new signalR.HubConnectionBuilder()
//     .withUrl("https://localhost:7115/offers")
//     .configureLogging(signalR.LogLevel.Information)
//     .build();
// async function start() {
//     try {
//         await connection.start();

//         $.get("https://localhost:7115/api/Offer", function (data, status) {
//             console.log(data);
//             element.innerHTML = 'Begin PRICE $ ' + data;
//         });

//         console.log("SignalR Connected");
//     }
//     catch (err) {
//         console.log(err);
//         setTimeout(() => {
//             start();
//         }, 5000);
//     }
// }
// var lastOffer = 0;
// connection.on("ReceiveMessage", (message, data) => {
//     let element2 = document.querySelector("#offerValue2");
//     data += 100;
//     element2.innerHTML = message + data;
//     button.disabled = false;
//     totalseconds = 0;
//     clearTimeout(clearInterval);
//     timeSection.style.display = "none";

// })


// connection.on("ReceiveInfo", (message, data) => {
//     let element2 = document.querySelector("#offerValue2");
//     element2.innerHTML = message+"\n with this offer : "+data+"$";
//     button.disabled = true;
//     timeSection.style.display = "none";
// })

// connection.onclose(async () => {
//     await start();
// })


// async function IncreaseOffer() {
//     timeSection.style.display = "block";
//     totalseconds = 10;
//     let result = document.querySelector("#user");
//     $.get("https://localhost:7115/Increase?number=100", function (data, status) {
//         element.innerHTML = data;
//         $.get("https://localhost:7115/api/Offer", function (data, status) {
//             lastOffer = data;
//             let element2 = document.querySelector("#offerValue2");
//             element2.innerHTML = lastOffer;
//         });
//     });

//     await connection.invoke("SendMessage", result.value);
//     button.disabled = true;

//     clearInterval = setInterval(async () => {
//         let time = document.querySelector("#time");
//         --totalseconds;
//         time.innerHTML = totalseconds;
//         if (totalseconds == 0) {
//             button.disabled = false;
//             clearTimeout(clearInterval);
//             let result = document.querySelector("#user");
//             button.disabled = true;
//             await connection.invoke("SendWinnerMessage", "Game Over\n" + result.value + " is winner");
//         }
//     }, 1000);

// }

// start();


/////////////////////////////////////////////////////
////////////////////////////////////////////////////

let timeSection = document.querySelector("#time-section");
let button = document.querySelector("#offerBtn");
let element = document.querySelector("#offerValue");
var totalseconds = 10;
var clearInterval;
var CURRENTROOM="";
let room=document.getElementById("room");
let currentUser="";

const connection = new signalR.HubConnectionBuilder()
    .withUrl("https://localhost:7115/offers")
    .configureLogging(signalR.LogLevel.Information)
    .build();
async function start() {
    try {
        await connection.start();

        $.get("https://localhost:7115/Room?room="+CURRENTROOM, function (data, status) {
            console.log(data);
            element.innerHTML = 'Begin PRICE $ ' + data;
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
var lastOffer = 0;
connection.on("ReceiveMessageRoom", (message, data) => {
    let element2 = document.querySelector("#offerValue2");
    data += 100;
    element2.innerHTML = message + data;
    button.disabled = false;
    totalseconds = 0;
    clearTimeout(clearInterval);
    timeSection.style.display = "none";

})


connection.on("ReceiveInfoRoom", (message, data) => {
    let element2 = document.querySelector("#offerValue2");
    element2.innerHTML = message+"\n with this offer : "+data+"$";
    button.disabled = true;
    timeSection.style.display = "none";
})

connection.on("ReceiveJoinInfo", (user) => {
    let infoUser = document.querySelector("#info");
    infoUser.innerHTML = user+" connected to our Room";
})

connection.onclose(async () => {
    await start();
})


async function IncreaseOffer() {
    timeSection.style.display = "block";
    totalseconds = 10;
    let result = document.querySelector("#user");
    $.get(`https://localhost:7115/IncreaseRoom?room=${CURRENTROOM}&number=100`, function (data, status) {
        element.innerHTML = data;
        $.get("https://localhost:7115/Room?room="+CURRENTROOM, function (data, status) {
            lastOffer = data;
            let element2 = document.querySelector("#offerValue2");
            element2.innerHTML = lastOffer;
        });
    });

    await connection.invoke("SendMessageRoom",CURRENTROOM,result.value);
    button.disabled = true;

    clearInterval = setInterval(async () => {
        let time = document.querySelector("#time");
        --totalseconds;
        time.innerHTML = totalseconds;
        if (totalseconds == 0) {
            button.disabled = false;
            clearTimeout(clearInterval);
            let result = document.querySelector("#user");
            button.disabled = true;
            await connection.invoke("SendWinnerMessageRoom",CURRENTROOM, "Game Over\n" + result.value + " is winner");
        }
    }, 1000);

}



async function JoinC(){
    CURRENTROOM="chevrolet";
    room.style.display="block";
    await start();
    currentUser=document.getElementById("user").value
    await connection.invoke("JoinRoom",CURRENTROOM,currentUser);
}

async function JoinM(){
    CURRENTROOM="mercedes";
    room.style.display="block";
    await start();
    currentUser=document.getElementById("user").value
    await connection.invoke("JoinRoom",CURRENTROOM,currentUser);
}