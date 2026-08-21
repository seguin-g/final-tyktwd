input.onButtonPressed(Button.A, function () {
    if (bar_x >= 1) {
        led.unplot(bar_x + 1, 4)
        bar_x = bar_x - 1
        led.plot(bar_x, 4)
    }
})
input.onButtonPressed(Button.AB, function () {
    basic.clearScreen()
    game_active = true
    has_ball = true
    ball_x = randint(0, 3)
    ball_y = 0
    ball_dx = 1
    ball_dy = 1
    led.plot(ball_x, ball_y)
})
radio.onReceivedString(function (receivedString) {
    if (receivedString == "start") {
        images.createImage(`
            . # # . .
            # . . # .
            . . # . .
            . # . . .
            # # # # .
            `).showImage(0)
        game_active = true
        has_ball = false
        ball_dx = 0
        ball_dy = 0
        players = 2
        basic.pause(1000)
        basic.clearScreen()
        led.plot(bar_x, 4)
        led.plot(bar_x + 1, 4)
    }
})
input.onButtonPressed(Button.B, function () {
    if (bar_x < 3) {
        led.unplot(bar_x, 4)
        bar_x = bar_x + 1
        led.plot(bar_x + 1, 4)
    }
})
radio.onReceivedValue(function (name, value) {
    if (name == "ball_x") {
        ball_x = value
        ball_dx = 1
        ball_dy = 1
        has_ball = true
    }
})
let ball_dy = 0
let ball_dx = 0
let ball_y = 0
let ball_x = 0
let bar_x = 0
let has_ball = false
let game_active = false
let players = 0
radio.setGroup(0)
images.createImage(`
    . . # . .
    . # # . .
    . . # . .
    . . # . .
    . # # # .
    `).showImage(0)
players = 1
game_active = false
has_ball = false
bar_x = 2
basic.pause(1000)
basic.clearScreen()
led.plot(bar_x, 4)
led.plot(bar_x + 1, 4)
basic.forever(function () {
    while (game_active && has_ball) {
        led.unplot(ball_x, ball_y)
        ball_y = ball_y + ball_dy
        ball_x = ball_x + ball_dx
        if (players == 1) {
            if (ball_y < 1) {
                ball_dy = 1
            }
        } else if (ball_y < 0) {
            has_ball = false
            continue;
        }
        if (ball_x <= 0 || ball_x >= 4) {
            ball_dx = ball_dx * -1
        }
        // --- Paddle Check ---
        if (ball_y >= 4) {
            if (ball_x == bar_x || ball_x == bar_x + 1) {
                ball_dy = -1
            } else {
                game_active = false
                game.gameOver()
            }
        }
        led.plot(ball_x, ball_y)
        led.plot(bar_x, 4)
        led.plot(bar_x + 1, 4)
        basic.pause(400)
    }
    basic.pause(400)
})
