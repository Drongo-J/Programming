class Sprite {
    constructor({ position, velocity, color }) {
        this.position = position;
        this.velocity = velocity;
        this.color = color;
    }

    draw() {
        c.beginPath();
        c.arc(this.position.x, this.position.y, PLAYER_RADIUS, 0, 2 * Math.PI);
        c.fillStyle = this.color;
        c.fill();
    }
}

class Player extends Sprite {
    constructor({ position, velocity, color }) {
        super({ position, velocity, color });
    }
}

class Ball extends Sprite {
    constructor({ position, velocity, color }) {
        super({ position, velocity, color });
    }

    draw() {
        c.beginPath();
        c.arc(this.position.x, this.position.y, BALL_RADIUS, 0, 2 * Math.PI);
        c.fillStyle = this.color;
        c.fill();
    }
}