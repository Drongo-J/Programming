const calendar = document.querySelector(".calendar");
const inputs = document.getElementById("date-selection");
const dateInfo = document.getElementById("date-info");
const myButton = document.getElementById("generateButton");
const modal = document.getElementById("mymodal");
const date_for_modal = document.getElementById("date-for-modal");

myButton.addEventListener("click", (event) => {
    event.preventDefault();
});

window.addEventListener("resize", function () {
    inputs.style.width = calendar.offsetWidth + "px";
});

let month_input = document.getElementById("month-input");
let year_input = document.getElementById("year-input");

let today = new Date();
month_input.value = today.getMonth() + 1;
year_input.value = today.getFullYear();
let today_day = today.getDate();

function addDaysOfWeek() {
    calendar.innerHTML += `
    <p class="week">Mo</p>
    <p class="week">Tu</p>
    <p class="week">We</p>
    <p class="week">Th</p>
    <p class="week">Fr</p>
    <p class="week">Sa</p>
    <p class="week">Su</p>
    `;
}

function getDaysInMonth(month, year) {
    return new Date(year, month, 0).getDate();
}

function createDayForCalendar(id, value, mySecretToken, isInactive = false) {
    let inactive = "win-btn-inactive";
    if (!isInactive)
        inactive = "";

    let secret = `data-secret="${mySecretToken}"`;
    return `<section class="win-btn ${inactive}" id="${id}" ${secret}>${value}</section>`;
}

function getMonthName(monthNumber) {
    const months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ];
    return months[monthNumber - 1];
}

const MAX_DAYS_IN_CALENDAR = 35;

function generateCalendar() {
    calendar.innerHTML = '';
    addDaysOfWeek();
    let addedDaysCount = 0;
    var date = new Date(`${month_input.value} 1, ${year_input.value}`);
    const index_of_first_day = date.getDay() - 1;
    let prev_month_days = getDaysInMonth(month_input.value - 1, year_input.value);
    let given_month_days = getDaysInMonth(month_input.value, year_input.value);

    // Add last dates of the previous month of given month
    for (let i = 0; i < index_of_first_day; i++) {
        calendar.innerHTML += createDayForCalendar(addedDaysCount + 1, prev_month_days - index_of_first_day + i + 1, '', true);
        addedDaysCount++;
    }

    let day = 1;
    // Add dates of given month
    for (let k = index_of_first_day; k < given_month_days + index_of_first_day; k++) {
        let value = (k - index_of_first_day) + 1;
        calendar.innerHTML += createDayForCalendar(addedDaysCount + 1, value, `${getMonthName(month_input.value)} ${value}, ${year_input.value}`);
        day++;
        addedDaysCount++;
    }

    day = 1;
    // Add days of the next month of the given month to fill the calendar
    for (let z = addedDaysCount; z < MAX_DAYS_IN_CALENDAR; z++) {
        calendar.innerHTML += createDayForCalendar(addedDaysCount, (z - addedDaysCount) + 1, '', true);
    }
    inputs.style.width = calendar.offsetWidth + "px";
    dateInfo.innerText = `${getMonthName(month_input.value)}, ${year_input.value}`;

    let btns = document.querySelectorAll(".win-btn:not(.win-btn-inactive)");
    btns.forEach(btn => {
        btn.addEventListener('click', function () {
            modal.style.visibility = 'visible';
            modal.style.opacity = '1';
            const secretToken = btn.dataset.secret;
            date_for_modal.innerText = secretToken;
            notes.value = getCookie(secretToken);
        });
    });
}

function closeModal() {
    modal.style.visibility = 'hidden';
    modal.style.opacity = '0';
}

function saveNotes() {
    const notes = document.getElementById("notes");
    let key = date_for_modal.innerText; //date
    let value = notes.value;
    setCookie(key, value);
    // closeModal();
}

generateCalendar();