def on_logo_touched():
    radio.send_string("start")
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

# The ball's left/right SPEED / La VITESSE gauche/droite de la balle

def on_button_pressed_a():
    global bar_x
    if bar_x >= 1:
        led.unplot(bar_x + 1, 4)
        bar_x = bar_x - 1
        led.plot(bar_x, 4)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global game_active, has_ball, ball_x, ball_y, ball_dx, ball_dy
    radio.send_string("start")
    game_active = True
    has_ball = True
    ball_x = randint(0, 3)
    ball_y = 1
    ball_dx = 1
    ball_dy = 1
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    global game_active, has_ball, ball_dx, ball_dy
    if receivedString == "start":
        game_active = True
        has_ball = False
        ball_dx = 0
        ball_dy = 0
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global bar_x
    if bar_x < 3:
        led.unplot(bar_x, 4)
        bar_x = bar_x + 1
        led.plot(bar_x + 1, 4)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_received_value(name, value):
    if True:
        pass
radio.on_received_value(on_received_value)

ball_dy = 0
ball_dx = 0
ball_y = 0
ball_x = 0
bar_x = 0
has_ball = False
game_active = False
radio.set_group(0)
game_active = False
has_ball = False
bar_x = 2
led.plot(bar_x, 4)
led.plot(bar_x + 1, 4)
# The ball's up/down SPEED / La VITESSE haut/bas de la balle
# --- PADDLE MOVEMENT / MOUVEMENT DE LA RAQUETTE ---
# // --- Engineer's Note --- //
# I wrote the instructions for what the buttons should DO,
# but I'm not sure I ever told the micro:bit to LISTEN for the button presses.
# Something feels like it's missing here...
# // --- Note de l'ingénieur --- //
# J'ai écrit les instructions pour ce que les boutons DOIVENT faire,
# mais je ne suis pas sûr d'avoir dit au micro:bit d'ÉCOUTER les appuis sur les boutons.
# Il me semble qu'il manque quelque chose ici...
# --- MAIN GAME LOOP / BOUCLE DE JEU PRINCIPALE ---
# // TEAM LEAD NOTE: The overall structure of this loop is good.
# // The bugs are small mistakes inside the 'if' statements.
# // NOTE DU CHEF D'ÉQUIPE: La structure générale de cette boucle est bonne.
# // Les bogues sont de petites erreurs à l'intérieur des conditions 'if'.

def on_forever():
    global ball_y, ball_x, has_ball, ball_dx, ball_dy
    while game_active and has_ball:
        serial.write_line("avant ball_y=" + convert_to_text(ball_y))
        led.unplot(ball_x, ball_y)
        ball_y = ball_y + ball_dy
        ball_x = ball_x + ball_dx
        if ball_y < 0:
            radio.send_value("ball_x", ball_x)
            has_ball = False
            continue
        if ball_x <= 0 or ball_x >= 4:
            ball_dx = ball_dx * -1
        # --- Paddle Check ---
        if ball_y >= 4:
            if ball_x == bar_x or ball_x == bar_x + 1:
                # This code runs when the ball hits the paddle.
                # HINT: This math is wrong. It stops the ball instead of bouncing it.
                # What math would make the ball go the other way?
                # Ce code s'exécute quand la balle touche la raquette.
                # INDICE: Ce calcul est faux. Il arrête la balle au lieu de la faire rebondir.
                # Quel calcul ferait aller la balle dans l'autre sens ?
                ball_dy = -1
            else:
                game.game_over()
        led.plot(ball_x, ball_y)
        led.plot(bar_x, 4)
        led.plot(bar_x + 1, 4)
        basic.pause(400)
    basic.pause(400)
basic.forever(on_forever)
