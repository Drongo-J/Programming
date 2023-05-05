document.addEventListener("touchstart", function () { }, true);

function setHeightOfTheMeals() {
    var meals = document.getElementsByClassName("meal");
    for (var i = 0; i < meals.length; i++) {
        var meal = meals[i];
        meal.style.height = meal.offsetWidth + "px";
    }
}

setHeightOfTheMeals();

let bar = document.getElementById("bar");
let navigators = document.getElementById("navigators");

const maxScreenWidth = window.matchMedia("(max-width:1360px)");

function barMouseEnter() {
    if (maxScreenWidth.matches) {
        bar.style.display = "none";
        navigators.style.display = "block";
    }

}

function navigatorsMouseLeave() {
    if (maxScreenWidth.matches) {
        bar.style.display = "block";
        navigators.style.display = "none";
    }
}

function handleViewportChange(event) {
    if (event.matches) {
        navigators.style.display = "none";
        bar.style.display = "block";
    } else {
        navigators.style.display = "flex";
        bar.style.display = "none";
    }
}

if (maxScreenWidth.matches) {
    navigators.style.display = "none";
    bar.style.display = "block";
}

maxScreenWidth.addListener(handleViewportChange);

const brunch = document.getElementById("brunch");
const welcome = document.getElementById("welcome");
const menu = document.getElementById("menu");
const events = document.getElementById("events");
const contact = document.getElementById("contact");

addEventListenerToElement(brunch, "header");
addEventListenerToElement(welcome, ".s-1");
addEventListenerToElement(menu, ".s-3");
addEventListenerToElement(events, ".s-5");
addEventListenerToElement(contact, ".s-6");

function addEventListenerToElement(element, target) {
    element.addEventListener('click', function (event) {
        event.preventDefault();

        const targetElement = document.querySelector(target);
        const targetPosition = targetElement.offsetTop;

        console.log(element);
        console.log(target);
        console.log(targetElement);
        console.log(targetPosition);


        window.scrollTo({
            top: targetPosition,
            behavior: 'smooth'
        });
    });
}

window.addEventListener('resize', function () {
    const screenWidth = window.innerWidth;
    if (screenWidth <= 280) {
        let deleduz = document.getElementById("deleduz");
        let text = "Created by <span style='color: #9d6b22'>Aykhan Ahmadzada</span> Baku,Azerbaijan";
        deleduz.innerHTML = text;

    }
});
