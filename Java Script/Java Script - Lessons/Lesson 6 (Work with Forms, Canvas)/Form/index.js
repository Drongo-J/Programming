
let myForm = document.forms["MyForm"];

function OnSubmit(event) {
    event.preventDefault();
    //alert("Submit Clicked");

    // let email=myForm['email'].value;
    // let password=myForm['password'].value;

    // alert(email+" "+password);
    Validate();
    
}


function Validate(){
    let startDate = myForm['startDate'].value;
    let endDate = myForm['endDate'].value;
    
    let element = document.querySelector("#infoStart");
    if (startDate > endDate) {
        element.innerHTML = "Invalid Date Selected";
    }
    else {
        element.innerHTML = "";
    }
    
}