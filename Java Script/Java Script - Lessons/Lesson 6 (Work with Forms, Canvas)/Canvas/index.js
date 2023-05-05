


let mycanvas = document.getElementById("mycanvas");

let context = mycanvas.getContext('2d');

// let x=100;
// let y=100;

// function Drawer(){
//     context.fillStyle='#00bfff';
//     context.fillRect(x,y,250,250);
//     x+=1;
//     y+=1;
//     context.clearRect(x+125,y+125,125,125);
// }

// function main() {

//     // setInterval(()=>{
//     //     Drawer();
//     // },100);
//     // context.fillStyle = '#00bfff';
//     // context.fillRect(50, 70, 150, 100);

//     // context.fillStyle='rgba(255,0,0,0.4)';
//     // context.fillRect(80,80,150,100);


//     // context.strokeStyle='#00ff7f';
//     // context.strokeRect(50,50,300,300);
// }


// main();

const centerX = mycanvas.width / 2;
const centerY = mycanvas.height / 2;
let x=centerX;
let y=centerY-350;
let counter=1;
const radius = centerY;
function main() {

    context.arc(centerX, centerY, radius, 0, 2 * Math.PI, false);
    context.fillStyle = 'green';
    context.fill();
    
    context.moveTo(centerX,centerY);
    context.lineTo(x,y);
    context.lineWidth=8;
    context.strokeStyle = "black";
    context.stroke();

setInterval(() => {
    ClearContext();
    Draw();
    counter++;
    if(counter>=60){
        counter=0;
    }
}, 1000);

}


function ClearContext(){
       
    

}


function Draw(){
    context.moveTo(centerX,centerY);
    context.lineTo(x,y);
    if(counter>=0 && counter<=14){
        x+=26;
        y+=26;
    }
    else if(counter>=15 && counter<=29){
        y+=26;
        x-=26;
    }
    else if(counter>=30 && counter<=44){
        y-=26;
        x-=26;
    }
    else if(counter>=45 && counter<=59){
        y-=26;
        x+=26;
    }
    context.lineWidth=8;
    context.strokeStyle = "red";
    context.stroke();
}


main();