

// $(document).ready(function(){
//     $("h1").hide();
//     $("#mypage").click(function(){
//         $("h1").show('1s');
//         $("#mypage").hide('1s');
        
//     });
// });




$(document).ready(function(){
    
    // $(".pages").click(function(){
    //     $(this).css('color','#00bfff');
    // })

    // let isClicked=false;
    // $(".pages").dblclick(function(){
    //     if(!isClicked){
    //         $(this).css("font-size",'4em');
    //         $(this).css("color",'red');
    //     }
    //     else{
    //         $(this).css("font-size",'1em');
    //         $(this).css("color",'green');
    //     }
    //     isClicked=!isClicked;
    // })

    // $("p").mouseenter(function(){
    //     $(this).css("color","red");
    //     $(this).css("transition","1s");
    // });

    // $("p").mouseleave(function(){
    //     $(this).css("color","green");
    //     $(this).css("transition","1s");
    // });

    // $("input").css("outline","none");

    // $("input").focus(function(){
    //     $(this).css("border","2px solid #00bfff");
    //     $(this).css("transition","1s");
    // });

    // $("input").blur(function(){
    //     $(this).css("border","2px solid red");
    //     $(this).css("transition","1s");
    // });


    // $("input").keydown(function(){
    //     $(this).css("border","2px solid orange");
    // });

    // $("input").keyup(function(){
    //     $(this).css("border","2px solid #00bfff");
    // });


});


let names=['Ahmedov Ali','Ahmedzade Ayxan','Axundzade Nihad','Bayramov Mehemmed'];
let content="";

for (let i = 0; i < names.length; i++) {
    content+=`
    <div style='top:${(i*150)}px' class='notification-success animate__animated animate__bounceInRight'>
        <div>
            <img class='circle' src='images/${i+1}.png' />
        </div>
        <div class='rectangle'>
            <p>
            ${names[i]}
            </p>
    
        </div>
    </div>
    `;
}

$(document).ready(function(){
    // html  text  val   attr  css
    //$("#div1").html(content);
   // $(".notification-success").hide();

    // $("img").hover(function(){
    //     $(".notification-success").show();
    // });

    // $("img").mouseleave(function(){
    //     $(".notification-success").hide();
    // });


    // $(".notification-success").click(function(){
    //     //$(this).fadeOut();
    // // $(this).fadeOut("slow");
    //  $(this).fadeOut(3000);
    // });


    $("p").on({
        mouseleave:function(){
            $(this).css("color",'red');
            $(this).text('leaved');
        },
        mouseenter:function(){
            $(this).css("color",'green');
            $(this).text('entered');
        },
        click:function(){
            $(this).css("color",'red');
            $(this).css("transition",'orange');
            $(this).text('clicked');

            $(this).off("mouseleave");
            $(this).off("mouseenter");
        }
    });

});