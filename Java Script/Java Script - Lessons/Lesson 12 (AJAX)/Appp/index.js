// $(document).ready(function(){

// // $("div").find("span").css(
// //     {
// //         "color":"red",
// //         "border":"2px solid orange"
// //     }
// // );

// // $("div").find("*").css({
// //     "color":"red",
// //     "border-bottom":"2px solid springgreen"
// // });

// // $("div").children("p.first").css(
// //     {"color":"deepskyblue"});


// // $("p").siblings().css({
// //     "color":"red"
// // });

// $("div").click(function(e){

//    // $(".item").first().hide(2000);
//   //  $(".item").first().show(2000);
//   //$(".item").eq(2).hide(1000);

//   //$("h1").filter(".box").hide(1000);
//   //$("h1").not(".box").hide(1000);

//   //$(this).prevUntil().hide(1000);
//   //$(this).prevUntil().hide(1000);
//   $(this).nextAll().hide(1000);

// });



// });

$(document).ready(function () {

    $("button").click(function () {
        //let url = "https://reqres.in/api/users";

        //$(".container").load(url);

        // $(".container").load(url,function(responseText,statusText,xhr){
        //     if(statusText=="success"){
        //         $(".container").css({"border":"4px solid #00ff7f"});
        //         console.log(JSON.parse(responseText));
        //     }
        //     else if(statusText=="error"){
        //         console.log(xhr.status);
        //         console.log(xhr.statusText);
        //         $(".container").css({"border":"4px solid red"});
        //     }
        // })

        let url = "https://reqres.in/api/users";
    // $.get(url,function(response,status){
    //     console.log(response);
    //     console.log(status);
    //     $(".container").text(JSON.stringify(response.data));
    //     $(".container").append(`Status : ${status}`);
    // })

        let body={
            name:'John',
            job:'Internship'
        };

        $.post(url,body,function(data,status){
                let result=data;
                $(".container").html(`<h1>${result.name} - ${result.job}</h1>`);
                console.log(result);
                $(".container").append(`<br>Status : ${status}`);
        });


    });


});