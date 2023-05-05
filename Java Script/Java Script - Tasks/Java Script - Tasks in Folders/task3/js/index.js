const canvas = document.getElementById("canvas");
const c = canvas.getContext('2d');

const SCMS = 50;
const CANVAS_WIDTH = 1264;
const CANVAS_HEIGHT = 846;
const PLAYER_RADIUS = 30;
const BALL_RADIUS = 20;
const PLAYER_HIT_POWER = 5;

canvas.width = CANVAS_WIDTH;
canvas.height = CANVAS_HEIGHT;

let kick = new Audio("Sounds\\kick.mp3");
let goal = new Audio("Sounds\\goal.mp3");

function handleKeyInput(keys, keyBooleans, value) {
    return function (event) {
        let code = event.code;
        switch (code) {
            case keys.up:
                keyBooleans[keys.up] = value;
                break;
            case keys.down:
                keyBooleans[keys.down] = value;
                break;
            case keys.left:
                keyBooleans[keys.left] = value;
                break;
            case keys.right:
                keyBooleans[keys.right] = value;
                break;
            default:
                break;
        }
    }
}

function playerMovementListener(keys, player, keyBooleans) {
    keyBooleans[keys.up] = false;
    keyBooleans[keys.down] = false;
    keyBooleans[keys.left] = false;
    keyBooleans[keys.right] = false;

    let myKeyDownHandler = handleKeyInput(keys, keyBooleans, true);
    document.addEventListener('keydown', myKeyDownHandler);

    let myKeyUpHandler = handleKeyInput(keys, keyBooleans, false);
    document.addEventListener('keyup', myKeyUpHandler);

    setInterval(() => {
        if (keyBooleans[keys.up]) {
            if (player.position.y - player.velocity.y > 0) {
                player.position.y -= player.velocity.y;
            }
        }
        if (keyBooleans[keys.down]) {
            if (player.position.y + player.velocity.y < CANVAS_HEIGHT) {
                player.position.y += player.velocity.y;
            }
        }
        if (keyBooleans[keys.left]) {
            if (player.position.x - player.velocity.x > 0) {
                player.position.x -= player.velocity.x;
            }
        }
        if (keyBooleans[keys.right]) {
            if (player.position.x + player.velocity.x < CANVAS_WIDTH) {
                player.position.x += player.velocity.x;
            }
        }

        c.clearRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
        drawGame();
        checkGoal();
        checkCollisionOfPlayer(player1);
        checkCollisionOfPlayer(player2);

    }, SCMS);
}

let trajectory = null;

function checkCollisionOfPlayer(player) {
    let playerX = player.position.x;
    let playerY = player.position.y;

    let ballX = ball.position.x;
    let ballY = ball.position.y;

    let leg1 = Math.abs(playerX - ballX);
    let leg2 = Math.abs(playerY - ballY);
    let distance = Math.sqrt(Math.pow(leg1, 2) + Math.pow(leg2, 2));

    if (distance <= PLAYER_RADIUS + BALL_RADIUS) {
        kick.play();
        let ballNewX = 0;
        if (ballX < playerX)
            ballNewX = ballX - (leg1 * PLAYER_HIT_POWER);
        else
            ballNewX = ballX + (leg1 * PLAYER_HIT_POWER);

        let ballNewY = 0;
        if (ballY < playerY)
            ballNewY = ballY - (leg2 * PLAYER_HIT_POWER);
        else
            ballNewY = ballY + (leg2 * PLAYER_HIT_POWER);

        let position = {
            x: ballNewX,
            y: ballNewY
        }

        console.log(ball.position.x + " " + ball.position.y);


        trajectory = getAllPointsBetween2Points({ x: ballX, y: ballY }, position);

        console.log(ball.position.x + " " + ball.position.y);


        const interval = setInterval(() => {
            moveBall();

            if (trajectory === null) {
                clearInterval(interval);
            }
        }, 30);
    }
}

function moveBall() {
    if (trajectory === null) return;

    if (trajectory[0].x < CANVAS_WIDTH - 20 && trajectory[0].x > 20)
        ball.position.x = trajectory[0].x;
    if (trajectory[0].y < CANVAS_HEIGHT - 20 && trajectory[0].y > 20)
        ball.position.y = trajectory[0].y;
    trajectory.shift();

    console.log(ball.position.x + " " + ball.position.y);
    if (trajectory.length === 0) trajectory = null;
}

function getAllPointsBetween2Points(point1, point2) {
    let trajectory = [];

    if (point1.x === point2.x) {
        let y_increment = 0;
        if (point1.y < point2.y)
            y_increment = 0.5;
        else
            y_increment = -0.5;

        let y = point1.y;
        while (true) {
            y += y_increment;

            trajectory.push({ x: point1.x, y: y });

            if (y_increment == 0.5) {
                if (y >= point2.y)
                    break;
            }
            else {
                if (y <= point2.y)
                    break;
            }
        }
    }
    else {
        let x_increment = 0;
        if (point1.x < point2.x)
            x_increment = 1.5;
        else
            x_increment = -1.5;

        let m = (point2.y - point1.y) / (point2.x - point1.x);
        let c = point1.y - m * point1.x;
        // linear equation : y = mx + c / point1.y = m * point.x + c
        let x = point1.x;
        while (true) {
            x += x_increment;
            let newY = m * x + c;
            let newX = x;
            trajectory.push({ x: newX, y: newY });
            if (x_increment == 1.5) {
                if (x >= point2.x)
                    break;
            }
            else {
                if (x <= point2.x)
                    break;
            }
        }
    }
    return trajectory;
}

function checkGoal() {
    if (ball.position.x < 40 && (ball.position.y > 370 && ball.position.y < 540) ||
        ball.position.x > 1176 && (ball.position.y > 370 && ball.position.y < 540)) {

        goal.play();

        setTimeout(() => {
            player1.position.x = (CANVAS_WIDTH / 3);
            player1.position.y = (CANVAS_HEIGHT / 2) + (PLAYER_RADIUS / 2);
            player2.position.x = (CANVAS_WIDTH / 3) * 2;
            player2.position.y = (CANVAS_HEIGHT / 2) + (PLAYER_RADIUS / 2);
            ball.position.x = (CANVAS_WIDTH / 2);
            ball.position.y = (CANVAS_HEIGHT / 2) + (PLAYER_RADIUS / 2);
        }, 1500);
    }
}
