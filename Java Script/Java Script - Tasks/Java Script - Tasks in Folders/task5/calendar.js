const offset = 69;
const angles = []; //in deg
for (let i = 0; i <= 360; i += 45) {
    angles.push((i * Math.PI) / 180);
}
let nearBy = [];

function clearNearBy() {
    nearBy.splice(0, nearBy.length).forEach((e) => (e.style.borderImage = null));
}

calendar.addEventListener("mousemove", (e) => {
    const x = e.x; //x position within the element.
    const y = e.y; //y position within the element.

    clearNearBy();
    nearBy = angles.reduce((acc, rad, i, arr) => {
        const cx = Math.floor(x + Math.cos(rad) * offset);
        const cy = Math.floor(y + Math.sin(rad) * offset);
        const element = document.elementFromPoint(cx, cy);

        if (element !== null) {
            if (
                element.classList.contains("win-btn") &&
                acc.findIndex((ae) => ae.id === element.id) < 0
            ) {
                const brect = element.getBoundingClientRect();
                const bx = x - brect.left; //x position within the element.
                const by = y - brect.top; //y position within the element.
                if (!element.style.borderImage)
                    element.style.borderImage = `radial-gradient(${offset * 2}px ${offset * 2}px at ${bx}px ${by}px ,rgba(255,255,255,0.7),rgba(255,255,255,0.1),transparent ) 9 / 1px / 0px stretch `;
                return [...acc, element];
            }
        }
        return acc;
    }, []);
});

calendar.onmouseleave = (e) => {
    clearNearBy();
};
