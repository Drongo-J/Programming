class User{
    constructor(id,email,firstname,lastname,avatar){
            this.id=id;
            this.email=email;
            this.firstname=firstname;
            this.lastname=lastname;
            this.avatar=avatar;
    }
}

let users=[];

$(document).ready(function(){
    $(document).ajaxStart(function(){
        $("#wait").fadeIn();
    });
    
    $(document).ajaxComplete(function(){
        $("#wait").fadeOut();
    })
    
    $(document).ajaxError(function(){
        let errorPage=`<section class="page_404">
        <div class="container">
            <div class="row">	
            <div class="col-sm-12 ">
            <div class="col-sm-10 col-sm-offset-1  text-center">
            <div class="four_zero_four_bg">
                <h1 class="text-center ">404</h1>
            
            
            </div>
            
            <div class="contant_box_404">
            <h3 class="h2">
            Look like you're lost
            </h3>
            
            <p>the page you are looking for not avaible!</p>
            
            <a href="" class="link_404">Go to Home</a>
        </div>
            </div>
            </div>
            </div>
        </div>
    </section>`;

    $("#data").append(errorPage);  

    })
    
    
    let url="https://reqres.in/api/users";
    $("button").click(function(){
        $.ajax({url:url,success:function(result){
            //$("#data").html(JSON.stringify(result));

            setTimeout(() => {    
                let data=result.data;
                data.forEach(u => {
                    users.push(new User(u.id,u.email,u.first_name,
                        u.last_name,u.avatar));
                    });
                    console.log(users);
                    LoadToView(users);
                }, 1500);
        }})


        // $.getJSON(url,function(result){
        //     let allData=result.data;
        //     allData.forEach(u=>{
        //             $.each(u,function(name,field){
        //                 $("#data").append(`<b>${name}</b> : `+field+" <br>");
        //             });
        //     });
        //     $.getScript("helper.js");
        // })


      





    });
});

function LoadToView(users){
    let content='';
    users.forEach(u=>{
        content+=`
        <section>
        <img src='${u.avatar}' style='width:200px;'/>
        <h1>${u.firstname} - ${u.lastname}</h1>
        <h2>${u.email}</h2>
        </section>
        `;
    });
    $("#data").html(content);
}
