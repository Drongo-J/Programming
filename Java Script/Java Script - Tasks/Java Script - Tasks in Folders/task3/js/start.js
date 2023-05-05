function startGame() {
    drawGame();

    player1KeyBools = [];
    player2KeyBools = [];

    let player1Keys = {
        up: "KeyW",
        down: "KeyS",
        left: "KeyA",
        right: "KeyD"
    };
    let player2Keys = {
        up: "ArrowUp",
        down: "ArrowDown",
        left: "ArrowLeft",
        right: "ArrowRight"
    };

    playerMovementListener(player1Keys, player1, player1KeyBools);
    playerMovementListener(player2Keys, player2, player2KeyBools);

}

function drawGame() {
    player1.draw();
    player2.draw();
    ball.draw();
}

var player1 = new Player({
    position: {
        x: (CANVAS_WIDTH / 3),
        y: (CANVAS_HEIGHT / 2) + (PLAYER_RADIUS / 2)
    },
    velocity: {
        x: 15,
        y: 15   
    },
    color: "red"
});

var player2 = new Player({
    position: {
        x: (CANVAS_WIDTH / 3) * 2,
        y: (CANVAS_HEIGHT / 2) + (PLAYER_RADIUS / 2)
    },
    velocity: {
        x: 15,
        y: 15
    },
    color: "blue"
});

var ball = new Ball({
    position: {
        x: (CANVAS_WIDTH / 2),
        y: (CANVAS_HEIGHT / 2) + (PLAYER_RADIUS / 2)
    },
    velocity: {
        x: 30,
        y: 30   
    },
    color: "black"
});

try {
    startGame(); 
} catch (error) {
    console.log(error);
}