document.addEventListener("touchstart", function () { }, true);

const navLinks = document.querySelectorAll('nav a');

navLinks.forEach(link => {
    link.addEventListener('click', function () {
        const prevActiveLink = document.querySelector('nav a.active');
        if (prevActiveLink) {
            prevActiveLink.classList.remove('active');
        }
        this.classList.add('active');
    });
});

function openMap() {
    window.open("https://www.google.com/maps?q=step+it+academy+location&FORM=HDRSC4&cp=40.395228%7E49.882221&lvl=16.0");
}

let nav = document.getElementById('nav');

function checkScreenSize() {
    const newLink = nav.querySelector('#login-id');
        if (newLink) {
          nav.removeChild(newLink);
        }
    if (window.matchMedia('(max-width: 934px)').matches) {
        const newLink = document.createElement('a');
        newLink.classList.add('main-text-style');
        newLink.id = 'login-id'
        newLink.setAttribute('href', '#');
        newLink.textContent = 'Log In';
        nav.appendChild(newLink);
    }
}

checkScreenSize();
window.addEventListener('resize', checkScreenSize);
