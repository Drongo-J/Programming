const imageLinks = [
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task4/img12_q8kva7",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task4/img9_lzhasd",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task4/img4_jqq7dt",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task4/img8_byxddu",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task4/img6_he77n6",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task4/img1_qfug4c",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task4/img7_nr0z0t",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task4/img2_fzctwn",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task4/img10_axtob1",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task4/img4_kidw9c",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task4/img5_mnqzsp",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task4/img11_fzoqnb",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task4/img13_oep4ao"
];

document.addEventListener("touchstart", function () { }, true);

const carousel = document.getElementById("carousel");
let mainImage = document.getElementById("main-img");

let id = 1;

function addImages() {
    imageLinks.forEach(link => {
        const img = new Image();
        img.src = link;
        carousel.innerHTML += `
            <img id='${id}' onclick='imgClick(src)' src='loading.gif' alt='Image'>
        `;

        let myId = id;
        img.onload = function () {
            let imgElement = document.getElementById(myId);
            imgElement.src = img.src;
        };
        id++;
    });
    mainImage.src = imageLinks[0];
}

addImages();

function imgClick(src) {
    mainImage.src = src;
}

let dragStarted = false;

let prevX = 0;
let prevScrollLeft = 0;

const dragStart = (e) => {
    dragStarted = true;
    prevX = e.pageX;
    prevScrollLeft = carousel.scrollLeft;
}

const dragging = (e) => {
    if (!dragStarted) return;
    e.preventDefault();
    let positionDiff = e.pageX - prevX;
    carousel.scrollLeft = (prevScrollLeft - positionDiff);
}

const dragEnd = (e) => {
    dragStarted = false;
}

carousel.addEventListener("mousedown", dragStart);
carousel.addEventListener("mousemove", dragging);
carousel.addEventListener("mouseup", dragEnd);