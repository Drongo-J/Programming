let loginClicked = true;

const register = document.querySelector('#s-8-options > :nth-child(3)');
const login = document.querySelector('#s-8-options > :nth-child(1)');


function s8LoginRegister(no) {
    if (loginClicked) {
        if (no == 2) {
            register.style.backgroundColor = "rgb(107, 190, 146)";
            login.style.backgroundColor = "#707c84";
        }
    } else {
        if (no == 1) {
            login.style.backgroundColor = "rgb(107, 190, 146)";
            register.style.backgroundColor = "#707c84";
        }
    }
    loginClicked = !loginClicked;
}