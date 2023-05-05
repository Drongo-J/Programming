var alertPlaceholder = document.getElementById('liveAlertPlaceholder')
let nameInput = document.getElementById("s-7-name");
let surnameInput = document.getElementById("s-7-surname");
let emailInput = document.getElementById("s-7-email");
let form = document.getElementById("s-7-form");
let stringEmpty = "";

form.addEventListener("submit", function (event) {
    event.preventDefault();
    if (form.checkValidity()) {
        let toastHTML = createToast(`Incorrect Inputs`);
        showToast(toastHTML);
    } else {
        signIn();
    }
});


const users_url = "https://reqres.in/api/users";
let USERS;
getUsers();
let CURRENT_USER;

function signIn() {
    let name_val = nameInput.value;
    let surname_val = surnameInput.value;
    let email_val = emailInput.value;

    if (name_val == stringEmpty || surname_val == stringEmpty || email_val == stringEmpty)
        return;

    if (USERS) {
        let found = false;
        USERS.forEach(user => {
            if (user.firstname == name_val && user.lastname == surname_val && user.email == email_val) {
                CURRENT_USER = user;
                window.location.href = "main.html";
                found = true;
            }
        });
        if (!found) {
            let toastHTML = createToast(`User Was Not Found!`);
            showToast(toastHTML);
        }
    }
}

function getUsers() {
    let users = [];
    $.ajax({
        url: users_url,
        success: function (result) {
            let data = result.data;
            data.forEach(user => {
                let newUser = new User(user.id, user.email, user.first_name, user.last_name, user.avatar);
                users.push(newUser);
            });
            USERS = users;
        },
        error: function () {
            let toastHTML = createToast(`An Error Occured While Fetching Users`);
            showToast(toastHTML);
            USERS = null;
        }
    });
}

function showToast(toastHTML) {
    $('body').append(toastHTML);
    let toastElement = $('#liveToast');
    let toast = new bootstrap.Toast(toastElement);
    toast.show();
}

function createToast(text) {
    let toast = `
    <div class="position-fixed bottom-0 end-0 p-3" style="z-index: 11">
        <div id="liveToast" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
            <div class="toast-header">
            <strong class="me-auto">aykhan.net</strong>
            <small>Now</small>
            <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
            <div class="toast-body text-danger">
                ${text}
            </div>
        </div>
    </div>
    `;
    return toast;
}