var modal = document.getElementById("modal");
var span = document.getElementsByClassName("close")[0];

span.onclick = function () {
    modal.style.display = "none";
}

window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

const length = 4;
const cardCount = length ** 2;
const game = document.getElementById("game");

const images = [
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f927_jef7n1",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f929_sbb4tc",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f928_gsepmq",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f926-200d-2642-fe0f_k6aguu",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f926-200d-2640-fe0f_zbgzwy",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f926-1f3ff_j0vsoi",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f926-1f3fc_rmmgpg",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f926-1f3fd_imazgp",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f926-1f3fe_klx7z7",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f926_igemrs",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f926-1f3fb_vkdqsh",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f925_krmwda",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f923_hdj9ip",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f924_wvbkca",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f922_gt12fl",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f920_uryj6w",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f921_hvbemt",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f919-1f3ff_yjun79",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f919-1f3fe_n5dpt9",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f919-1f3fc_i9bs65",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f919-1f3fd_taagtg",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f919-1f3fb_pjbbh0",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f919_hdagbx",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f918-1f3ff_zd15p6",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f918-1f3fe_mz8jna",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f918-1f3fd_lgvllp",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f918-1f3fc_wfyxrb",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f918-1f3fb_vm3ykd",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f918_v0n0j0",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f917_im5i8x",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f916_zyacat",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f915_rczhsc",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f913_p535gk",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f914_robqbd",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f912_qnlfov",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f697_xr2rxj",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f911_mqjxwp",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f910_giq9xj",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f698_eetiym",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f699_dblgf3",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f696_lwreaj",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f695_z81sjk",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f692_ocauol",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f694_abunjo",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f693_dhr5op",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f691_bxownp",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f690_ycnmkr",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f687_p7hfti",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f688_uwj6us",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f689_jjf9zl",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f685_wzx5jf",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f686_k0naaz",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f683_xny4jd",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f684_tz0jzd",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f682_uw1jpo",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f681_fwlt2f",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f649_pmoalf",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f680_ozberh",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f648_sytl72",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f647-200d-2640-fe0f_hkckjt",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f647-1f3fd_iw7ygj",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f647-1f3fe_iqq9yb",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f647-1f3ff_r7xklh",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f647-1f3fc_rnxu3c",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f647-1f3fb_fsuaqp",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f647_apyzs8",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f646-200d-2642-fe0f_cx8qj0",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f646-1f3ff_jq5nm6",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f646-1f3fe_ipqpoz",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f646-1f3fd_fxfljz",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f646-1f3fc_ozdfzv",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f646_klmpzh",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f646-1f3fb_v0nf6f",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f645-200d-2642-fe0f_ckm1fa",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f645-1f3fe_ed4rys",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f645-1f3ff_tn1hvn",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f645-1f3fc_m6vztm",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f645-1f3fd_ksvc7t",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f645-1f3fb_caxlgn",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f645_qvnowb",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f644_z7ttfx",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f643_xqoxpi",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f641_eupbur",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f642_bj7h5f",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f640_nvqlma",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f639_zzu7w8",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f638_weyhvu",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f635_ell8pj",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f637_u77e64",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f634_ypv9ov",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f633_dnr22d",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f631_jicmpm",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f632_qeuba2",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f630_zz7qj0",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f627_rkhqpp",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f629_bar6is",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f626_ss9d6a",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f624_vt5uvg",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f625_iy45y1",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f620_ekjxke",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f623_mxczgz",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f622_hzyi3e",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f621_r49ht3",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f619_e0d0ww",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f617_azc7vr",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f616_ngf5zd",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f615_dybu7l",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f614_lxoj0v",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f610_ojfl87",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f613_pwfwah",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f612_im6ami",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f611_f4fhsd",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f609_fsrifp",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f607_wxd8qz",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f605_wvjs6r",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f606_h8xtsq",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f604_n92euo",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f603_nkmhyl",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f601_m3ouka",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f600_sr0863",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f596-1f3ff_ihu0cn",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f596-1f3fe_t5zfkt",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f596-1f3fd_fdqa1d",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f596-1f3fc_mfaj1b",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f596-1f3fb_oglomh",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f596_j70800",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f590-1f3fe_swjsx6",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f590-fe0f_r0awya",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f590-1f3ff_vjmy3l",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f590-1f3fd_tsc6dv",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f590-1f3fc_qv78fy",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f587-fe0f_l10ovg",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f579-fe0f_ft8v7g",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f590-1f3fb_pduwoc",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f578-fe0f_ldnpvc",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f577-fe0f_o4udov",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f575-1f3ff_unymcm",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f575-fe0f-200d-2640-fe0f_nxotek",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f575-fe0f_nwiuft",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f576-fe0f_f38mex",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f575-1f3fd_om5q36",
    "http://res.cloudinary.com/dbriqxpaa/image/upload/v1/java-script/task2/emojis/1f575-1f3fe_smp616"
];

var flip = new Audio("flip.mp3");

function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}

function getImages() {
    let result = [];
    let i = 0;
    let ic = cardCount / 2;
    while (i < ic) {
        var index = Math.floor(Math.random() * images.length);
        var element = images[index];
        if (result.indexOf(element) === -1) {
            result.push(element);
            result.push(element);
            i++;
        }
    }
    return shuffleArray(result);
}

function addCards() {
    let imgs = getImages();
    for (let i = 0; i < cardCount; i++) {
        let content = `
        <section id='${i + 1}' class="flip-card animate__animated">
            <section class="flip-card-inner">
                <section class="flip-card-front">
                </section>
                <section class="flip-card-back">
                    <img src="${imgs[i]}"
                    alt="Image">
                 </section>
            </section>
        </section>
        `;
        game.innerHTML += content;
    }
}

var flippedCards = [];
let lastId = 0;
let remainingCards = cardCount;

function flipCard() {
    if (flippedCards.length >= 2 || lastId == this.id) return;
    lastId = this.id;
    const flipCardInner = this.querySelector('.flip-card-inner');
    flipCardInner.style.transform = 'rotateY(180deg)';
    flip.play();
    flippedCards.push(this);

    if (flippedCards.length == 2) {
        // check similarity between flipped cards
        let img1 = flippedCards[0].querySelector(".flip-card-back img");
        let img2 = flippedCards[1].querySelector(".flip-card-back img");

        if (img1.src === img2.src) {
            setTimeout(() => {
                flippedCards.forEach(card => {
                    card.classList.add("animate__bounceOutLeft");
                    card.display = 'none';
                    flippedCards = [];
                });
                remainingCards -= 2;
                if (remainingCards === 0) {
                    modal.style.display = "block";
                }
            }, 300);

            console.log(remainingCards);

        }
        else {
            // flip back
            setTimeout(() => {
                flippedCards.forEach(card => {
                    const inner = card.querySelector('.flip-card-inner');
                    inner.style.transform = 'none';
                });
                flippedCards = [];
            }, 1100);
        }
    }
}

function addClickToCards() {
    const flipCards = document.querySelectorAll('.flip-card');

    flipCards.forEach(card => {
        card.addEventListener('click', flipCard);
    });
}

function startGame() {
    game.innerHTML = '';
    modal.style.display = "none";
    flippedCards = [];
    lastId = 0;
    remainingCards = cardCount;
    addCards();
    addClickToCards();
}

startGame();

