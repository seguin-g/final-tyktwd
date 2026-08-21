input.onLogoEvent(TouchButtonEvent.Touched, function () {
    radio.sendString("start")
    nb_joueurs = 2
})
// The ball's left/right SPEED / La VITESSE gauche/droite de la balle
input.onButtonPressed(Button.A, function () {
    if (bar_x >= 1) {
        led.unplot(bar_x + 1, 4)
        bar_x = bar_x - 1
        led.plot(bar_x, 4)
    }
})
input.onButtonPressed(Button.AB, function () {
    if (nb_joueurs == 2) {
        radio.sendString("start")
    }
    game_active = true
    has_ball = true
    ball_x = randint(0, 3)
    ball_y = 1
    ball_dx = 1
    ball_dy = 1
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
        nb_joueurs = 2
        basic.pause(1000)
        basic.clearScreen()
        led.plot(bar_x, 4)
        led.plot(bar_x + 1, 4)
    }
    if (receivedString == "you_won") {
        images.iconImage(IconNames.Heart).showImage(0)
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
let nb_joueurs = 0
radio.setGroup(0)
images.createImage(`
    . . # . .
    . # # . .
    . . # . .
    . . # . .
    . # # # .
    `).showImage(0)
nb_joueurs = 1
game_active = false
has_ball = false
bar_x = 2
basic.pause(1000)
basic.clearScreen()
led.plot(bar_x, 4)
led.plot(bar_x + 1, 4)
// The ball's up/down SPEED / La VITESSE haut/bas de la balle
// --- PADDLE MOVEMENT / MOUVEMENT DE LA RAQUETTE ---
// // --- Engineer's Note --- //
// I wrote the instructions for what the buttons should DO,
// but I'm not sure I ever told the micro:bit to LISTEN for the button presses.
// Something feels like it's missing here...
// // --- Note de l'ingénieur --- //
// J'ai écrit les instructions pour ce que les boutons DOIVENT faire,
// mais je ne suis pas sûr d'avoir dit au micro:bit d'ÉCOUTER les appuis sur les boutons.
// Il me semble qu'il manque quelque chose ici...
// --- MAIN GAME LOOP / BOUCLE DE JEU PRINCIPALE ---
// // TEAM LEAD NOTE: The overall structure of this loop is good.
// // The bugs are small mistakes inside the 'if' statements.
// // NOTE DU CHEF D'ÉQUIPE: La structure générale de cette boucle est bonne.
// // Les bogues sont de petites erreurs à l'intérieur des conditions 'if'.
basic.forever(function () {
    while (game_active && has_ball) {
        led.unplot(ball_x, ball_y)
        ball_y = ball_y + ball_dy
        ball_x = ball_x + ball_dx
        if (nb_joueurs == 1) {
            if (ball_y < 1) {
                ball_dy = 1
            }
        } else {
            if (ball_y < 0) {
                radio.sendValue("ball_x", ball_x)
                has_ball = false
                continue;
            }
        }
        if (ball_x <= 0 || ball_x >= 4) {
            ball_dx = ball_dx * -1
        }
        // --- Paddle Check ---
        if (ball_y >= 4) {
            if (ball_x == bar_x || ball_x == bar_x + 1) {
                // This code runs when the ball hits the paddle.
                // HINT: This math is wrong. It stops the ball instead of bouncing it.
                // What math would make the ball go the other way?
                // Ce code s'exécute quand la balle touche la raquette.
                // INDICE: Ce calcul est faux. Il arrête la balle au lieu de la faire rebondir.
                // Quel calcul ferait aller la balle dans l'autre sens ?
                ball_dy = -1
            } else {
                if (nb_joueurs == 2) {
                    radio.sendString("you_won")
                }
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
