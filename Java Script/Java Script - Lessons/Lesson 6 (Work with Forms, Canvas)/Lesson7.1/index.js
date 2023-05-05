let mycanvas = document.getElementById("canvas");

let ctx = mycanvas.getContext('2d');

window.requestAnimationFrame(draw);
let oldX=-1;
let oldY=-1;
let size=50;
function draw(x,y){  
    size+=0.3;
    ctx.fillStyle = '#f9dc5c';
    if(oldX==-1 && oldY==-1){
        oldX=x;
        oldY=y;
    }
    ctx.clearRect(oldX,oldY, size, size);
    ctx.fillRect(x,y, size, size);
    oldX=x;
    oldY=y;
    //ctx.translate(10,10);
   // draw();
   console.log("test");
}

function myFunction(e){   
    let x = e.offsetX;
    let y = e.offsetY;
      draw(x,y);
}

window.addEventListener("mousemove", (e) => {
    myFunction(e);
  });

