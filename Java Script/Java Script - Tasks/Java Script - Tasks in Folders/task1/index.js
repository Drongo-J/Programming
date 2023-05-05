let calculator = document.getElementById("calculator")
let buttons = document.getElementById("buttons");
let inputsSection = document.getElementById("inputs-section");
let inputs = document.getElementById("inputs");
let myHistory = document.getElementById("history");

// ☾
// ☀

let buttonElements = [
    "☀",
    "AC",
    "⌫",
    "÷",
    "7",
    "8",
    "9",
    "×",
    "4",
    "5",
    "6",
    "−",
    "1",
    "2",
    "3",
    "+",
    "0",
    ".",
];


let plusSign = '+';
let minusSign = '−';
let multiplySign = '×';
let divideSign = '÷';
let percentSign = '%';
let dotSign = '.';
let equalsSign = '=';
let defaultInputsText = "0";
let stringEmpty = "";
let signIsCliked = false;
let currentSign = undefined;
let equalCliked = false;
let backspaceSign = "⌫";
let sunSymbol = "☀";
let moonSymbol = "☾";
let isNightMode = false;
let max11numbers = "Max 11 numbers!";
let errorMessage = "Error!";

function addButtons() {
    for (let i = 0; i < 18; i++) {
        if (i == 0) {
            buttons.innerHTML += `<div class='button' onClick='lightMode()' id='modeChange' style='color: #ED802E !important;'>${buttonElements[i]}</div>`;
        }
        else if (i < 4 || i % 4 == 3) {
            buttons.innerHTML += `<div class='button' style='color: #ED802E !important;'>${buttonElements[i]}</div>`;
        }
        else {
            buttons.innerHTML += `<div class='button'>${buttonElements[i]}</div>`;
        }
    }
    buttons.innerHTML +=
        `<div class='button' 
              id='equalsButton'
              style='background-color: #ED802E; color: white; max-height:90px;'>
            =
        </div>`;
}

function clear() {
    inputs.innerText = defaultInputsText;
    myHistory.innerText = stringEmpty;
    signIsCliked = false;
    currentSign = undefined;
}

function addEventListenersToButtons() {
    const elements = document.querySelectorAll('.button');

    elements.forEach(element => {
        element.addEventListener('click', function () {
            if (element.innerText === "AC") {
                clear();
            }
            // If sign in clicked
            else if (element.innerText === plusSign ||
                element.innerText === minusSign ||
                element.innerText === divideSign ||
                element.innerText === multiplySign) {

                if (inputs.innerText === errorMessage) {
                    clear();
                    return;
                }
                if (inputs.innerText === max11numbers) return;

                if (!containsSymbol()) {
                    if (equalCliked) {
                        equalCliked = false;
                        myHistory.innerText = stringEmpty;
                    }

                    // Check if inputs ends with dot
                    checkDotInInputs();
                    // Change History
                    if (signIsCliked) {
                        let arr = myHistory.innerText.split(" ");
                        let n1 = arr[0];
                        myHistory.innerText = `${n1} ${element.innerText}`;
                    }
                    else {
                        myHistory.innerText = `${inputs.innerText} ${element.innerText}`;
                    }
                    // Reset Inputs
                    inputs.innerText = defaultInputsText;
                    // Set Font Size
                    setFontSizeOfInputs();
                    signIsCliked = true;
                    currentSign = element.innerHTML;
                }
            }
            else if (element.innerText === dotSign) {   // If dot is clicked
                if (equalCliked) {
                    equalCliked = false;
                    myHistory.innerText = stringEmpty;
                }

                if (inputs.innerText.indexOf(dotSign) == -1) {
                    inputs.innerText += element.innerText;
                    setFontSizeOfInputs();
                }
            }
            else if (element.innerText === equalsSign) { // If equals is clicked
                if (signIsCliked) { // if first number is given and sign is known
                    equalCliked = true;
                    let n1 = myHistory.innerText.replace(plusSign, stringEmpty)
                        .replace(minusSign, stringEmpty)
                        .replace(multiplySign, stringEmpty)
                        .replace(divideSign, stringEmpty);

                    // Check if inputs ends with dot
                    checkDotInInputs();
                    let n2 = inputs.innerText;

                    try {
                        let result = calculateResult(n1, n2);
                        if (result === Infinity || isNaN(result))
                            throw Error;

                        myHistory.innerText = `${n1} ${currentSign} ${n2} ${equalsSign}`;
                        inputs.innerText = result.toFixed(4).replace(/\.?0+$/, '');
                        signIsCliked = false;
                    } catch (error) {
                        inputs.innerText = errorMessage;
                        myHistory.innerText = stringEmpty;
                        inputs.style.color = "red";
                        setTimeout(() => {
                            inputs.innerText = defaultInputsText;
                            myHistory.innerText = stringEmpty;
                            inputs.style.color = "white";
                            clear();
                        }, 1000);
                    }
                }
            }
            else if (element.innerText === backspaceSign) {
                let length = inputs.innerText.length;
                if (length > 1) {
                    inputs.innerText = inputs.innerText.substring(0, length - 1);
                }
                else {
                    inputs.innerText = defaultInputsText;
                }
            }
            else { // If any number is clicked
                if (element.innerHTML === sunSymbol || element.innerHTML === moonSymbol) {
                    return
                }
                if (inputs.innerText.length < 12) {
                    if (equalCliked) {
                        equalCliked = false;
                        inputs.innerText = defaultInputsText;
                        myHistory.innerText = stringEmpty;
                    }

                    if (inputs.innerText === defaultInputsText)
                        inputs.innerText = element.innerText;
                    else
                        inputs.innerText += element.innerText;
                    setFontSizeOfInputs();
                }
                else {
                    if (inputs.innerText != max11numbers) {
                        let text = inputs.innerText;
                        let text2 = myHistory.innerText;
                        inputs.innerText = max11numbers;
                        inputs.style.color = "red";
                        setTimeout(() => {
                            inputs.innerText = text;
                            myHistory.innerText = text2;
                            inputs.style.color = "white";
                        }, 1000);
                    }
                }
            }
            checkInputs();
        });
    });
}

function calculateResult(n1, n2) {
    let number1 = Number(n1);
    let number2 = Number(n2);

    if (currentSign === plusSign) {
        return number1 + number2;
    }
    else if (currentSign === minusSign) {
        return number1 - number2;
    }
    else if (currentSign === divideSign) {
        return number1 / number2;
    }
    else if (currentSign === multiplySign) {
        return number1 * number2;
    }
    else {
        alert("Unknow error occured!");
    }
}

function checkDotInInputs() {
    if (inputs.innerText.endsWith(dotSign)) {
        inputs.innerText = inputs.innerText.replace(dotSign, stringEmpty);
    }
}

function setFontSizeOfInputs() {
    let pxSize = getComputedStyle(inputs).getPropertyValue('font-size');
    var remSize = pxToRem(pxSize.replace("px", ""));
    if (inputs.innerText.length > 7) {
        inputs.style.fontSize = remSize - 0.25 + 'rem';
    }
    else {
        inputs.style.fontSize = "4.5rem";
    }
}

function containsSymbol() {
    if (inputs.innerHTML.indexOf(plusSign) != -1 ||
        inputs.innerHTML.indexOf(minusSign) != -1 ||
        inputs.innerHTML.indexOf(divideSign) != -1 ||
        inputs.innerHTML.indexOf(multiplySign) != -1 ||
        inputs.innerHTML.indexOf(percentSign) != -1) {
        return true;
    }
    return false;
}

function checkInputs() {
    if (inputs.innerText.trim() == stringEmpty) {
        inputs.innerText = defaultInputsText;
    }
}

function pxToRem(px) {
    return px / parseFloat(getComputedStyle(document.documentElement).fontSize);
}

function lightMode() {
    isNightMode = !isNightMode;
    if (isNightMode) {
        document.body.style.setProperty('--main-color', "#EBEBEB");
        document.body.style.setProperty('--second-color', "black");
        modeChange.innerHTML = moonSymbol;
    }
    else {
        document.body.style.setProperty('--main-color', "#243441");
        document.body.style.setProperty('--second-color', "white");
        modeChange.innerHTML = sunSymbol;
    }
}

function setSizes() {
    try {
        var myButtons = document.getElementsByClassName("button");
        let myWidth = 0;
        for (let i = 0; i < myButtons.length - 1; i++) {
            const btn = myButtons[i];
            let width = btn.offsetWidth;
            console.log("width : " + width)
            myWidth = width;
            btn.style.height = width + "px";
            console.log("myWidth : " + myWidth);
        }

        var widthValue = window.getComputedStyle(buttons).getPropertyValue('width');
        var widthInt = parseInt(widthValue);
        let gap = widthInt * 0.02;
        if (window.innerWidth > 500) {
            equalsButton.style.width = (myWidth * 2) + (gap * 1) + "px";
        }
        else {
            equalsButton.style.width = (myWidth * 2) + (gap * 0.5) + "px";
        }
        equalsButton.style.height = myWidth + "px";
        console.log(equalsButton.style.width);
    } catch (error) {
        console.log(error)
    }
}

window.addEventListener("resize", setSizes);



let equalsButton;
function createCalculator() {
    addButtons();
    equalsButton = document.getElementById("equalsButton");
    setSizes();
    let modeChange = document.getElementById("modeChange");
    addEventListenersToButtons();
    checkInputs();
}

createCalculator();