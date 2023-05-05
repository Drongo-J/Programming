let imagesArray = [
    "https://res.cloudinary.com/dbriqxpaa/image/upload/v1679213413/web-programming/task8/cabin_bmenzq.png",
    "https://res.cloudinary.com/dbriqxpaa/image/upload/v1679213413/web-programming/task8/cake_hhpyw7.png",
    "https://res.cloudinary.com/dbriqxpaa/image/upload/v1679213413/web-programming/task8/circus_qq4s1u.png",
    "https://res.cloudinary.com/dbriqxpaa/image/upload/v1679213413/web-programming/task8/game_avjezu.png",
    "https://res.cloudinary.com/dbriqxpaa/image/upload/v1679213413/web-programming/task8/safe_nxp0bg.png",
    "https://res.cloudinary.com/dbriqxpaa/image/upload/v1679213413/web-programming/task8/submarine_ys32dm.png"];

let imageTags = [
    "LOG CABIN",
    "TASTY CAKE",
    "CIRCUS TENT",
    "CONTROLLER",
    "LOCKED SAFE",
    "SUBMARINE"];

let id = 0;
let portfolioModals = document.getElementById("portfolio-modals");
imagesArray.forEach((imgLink) => {
    id++;
    portfolioModals.innerHTML += (`
    <section class="portfolio-modal modal fade" id="portfolioModal${id}" tabindex="-1" aria-labelledby="portfolioModal${id}"
    aria-hidden="true">
    <section class="modal-dialog modal-xl">
        <section class="modal-content">
            <section class="modal-header border-0"><button class="btn-close" type="button" data-bs-dismiss="modal"
                    aria-label="Close"></button></section>
            <section class="modal-body text-center pb-5">
                <section class="container">
                    <section class="row justify-content-center">
                        <section class="col-lg-8">
                            <section class="d-flex justify-content-center pb-3 flex-column align-items-center container-fluid">
                              <h1 id="portfolio-headline" class="fw-bolder pt-3 text-center w-100 text-uppercase">${imageTags[id - 1]}</h1>
                                <section id="portfolio-section" class="divider-container d-flex flex-row justify-content-center align-items-center mt-2">
                                  <section class="divider-line"></section>
                                  <section class="divider-icon mx-auto"><i class="fas fa-star"></i></section>
                                  <section class="divider-line"></section>
                                 </section>
                            </section>
                            <img class="img-fluid rounded mb-5" src="${imagesArray[id - 1]}" alt="..." />
                            <p class="mb-4">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque
                                assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam
                                velit asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam.
                            </p>
                            <button class="btn btn-primary" data-bs-dismiss="modal">
                                <i class="fas fa-xmark fa-fw"></i>
                                Close Window
                            </button>
                        </section>
                    </section>
                </section>
            </section>
        </section>
    </section>
</section>
    `);
});

console.log(portfolioModals.innerHTML);




const portfolioLink = document.querySelector('.nav-item a[href="#portfolio"]');
const aboutLink = document.querySelector('.nav-item a[href="#about"]');
const contactLink = document.querySelector('.nav-item a[href="#contact"]');

addEventListenerToLink(portfolioLink, "#portfolio");
addEventListenerToLink(aboutLink, "#about");
addEventListenerToLink(contactLink, "#contact");

const navbarCollapse = document.querySelector('.navbar-collapse');

function addEventListenerToLink(link, id) {
    link.addEventListener('click', function (event) {
        event.preventDefault();

        const contactSection = document.querySelector(id);

        const isNavbarOpen = navbarCollapse.classList.contains('show');

        let yOffset = 0;
        if (isNavbarOpen) {
            yOffset = -61;
        } else {
            yOffset = -72;
        }

        const y = contactSection.getBoundingClientRect().top + window.pageYOffset + yOffset;

        window.scrollTo({ top: y, behavior: 'smooth' });
    });
}

window.onscroll = function () {
    var scrollPosition = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;

    let nav = document.getElementById("mainNav");
    if (scrollPosition > 0) {
        nav.classList.remove("p-4");
        nav.classList.add("p-2");
    }
    else {

        nav.classList.remove("p-2");
        nav.classList.add("p-4");
    }
};

window.addEventListener('DOMContentLoaded', event => {
    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }
    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element 
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 72,
        });
    };
});

let elements = document.querySelectorAll('.btn-social');
elements.forEach(element => {
    element.addEventListener('click', function () {
        element.style.boxShadow = '0 0 10px 5px white';
        setTimeout(() => {
            element.style.boxShadow = 'none';
        }, 300);
    });
});

const navLinks = document.querySelectorAll('.navbar-nav>li>a');

navLinks.forEach(function(navLink) {
  navLink.addEventListener('click', function() {
    const navCollapse = document.querySelector('.navbar-collapse');
    if (navCollapse.classList.contains('show')) {
      navCollapse.classList.remove('show');
    }
  });
});
