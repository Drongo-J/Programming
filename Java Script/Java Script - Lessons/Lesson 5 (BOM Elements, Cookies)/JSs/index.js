//document.cookie='username=Togrul Eliyev';
//console.log(document.cookie);
// setTimeout(()=>{
//     console.log(document.cookie);
// },5000);

function setCookie(name, value, seconds) {
  const d = new Date();
  d.setTime(d.getTime() + seconds * 1000);
  let expires = "expires=" + d.toUTCString();
  document.cookie = name + "=" + value + ";" + expires + ";path=/";
}

//setCookie('name','Tural',50);

//console.log(document.cookie);

function getCookie(key) {
  let name = key + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(";");

  for (let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == " ") {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

//setCookie("agent", "AGENT007", 3600);

// setInterval(() => {
//   let data = getCookie("agent");
//   console.log(data);
// }, 1000);


let game=[];
function FillGame(){
    for (let i = 0; i < 3; i++) {
        let subGame=[];
        for (let k = 0; k < 3; k++) {
            subGame.push(0);
        }    
        game.push(subGame);
    }
}
let id=1;
function DrawGame(){
    let content='';
    for (let i = 0; i < game.length; i++) {
        const subGame = game[i];
        content+=`<tr>`;
        for (let k = 0; k < subGame.length; k++) {
            const data = subGame[k];
            let element='';
            if(data!=0)
            {
                element=data;
            }
            if(data==1){
                element='X';
            }
            else if(data==2){
                element='O';
            }
            content+=`<td id='${id}' onclick="SelectItem(id,${i},${k})">${element}</td>`
            ++id;
        }
        content+=`</tr>`;
    }
    let gameTable=document.getElementById('gameTable');
    gameTable.innerHTML=content;
}


let isFirstPlayer=true;
function Turn(){
    let element=document.getElementById("turn");
    if(isFirstPlayer){
        element.innerHTML='X Player';
        element.style.color="#00bfff";
    }
    else{
        element.innerHTML='O Player';
        element.style.color='#00ff7f';
    }
}
function StartGame(){
    game=[];
    Turn();
    FillGame();
    DrawGame();
}

function SelectItem(id,i,k){
    let item=document.getElementById(id);
    if(isFirstPlayer){
        item.innerHTML='X';
        game[i][k]=1;
    }
    else{
        item.innerHTML='O';
        game[i][k]=2;
    }
    isFirstPlayer=!isFirstPlayer;
    Turn();
    console.log(game);
}

function gameArrayToString(){
    let content='';
    for (let i = 0; i < game.length; i++) {
        const subGame = game[i];
        for (let k = 0; k < subGame.length; k++) {
            const element = subGame[k];
            if(k==subGame.length-1)
            content+=`${element}`;
            else content+=`${element} `;
        }
        if(i!=game.length-1)
        content+='=';
    }
    return content;
}


function SaveGame(){
    let result=gameArrayToString();
    console.log(result);
    setCookie('game',result,3600);
}

function InitialLoad(){
    let result=getCookie('game');
    if(result.length>0){
        let element=document.getElementById('info');
        element.innerHTML='You can continue your last game';
    }
}

InitialLoad();

function ResetGame(){
    setCookie('game','');
}

function ResumeGame(){
    let result=getCookie('game');
    let data=result.split('=');
    game=[];
    for (let i = 0; i < data.length; i++) {
        const element = data[i].split(' ');
        let subGame=[];
        for(let k=0;k<element.length;k++){
            const item=element[k];
            subGame.push(item);
        }
        game.push(subGame);
    }
    DrawGame();
}