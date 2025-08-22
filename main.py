bar_x = 0
ball_x = 0
ball_y = 0
ball_dx = 0
ball_dy = 0
# The ball's left/right SPEED / La VITESSE gauche/droite de la balle

def on_button_pressed_a():
    global bar_x
    # What happens if the player keeps pressing A?
    # Que se passe-t-il si le joueur continue d'appuyer sur A ?
    # Does anything stop the paddle at the wall?
    # Y a-t-il une règle pour arrêter la raquette au mur ?
    led.unplot(bar_x + 1, 4)
    bar_x = bar_x - 1
    led.plot(bar_x, 4)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global bar_x
    # Same question here for moving right.
    # Même question ici pour le mouvement vers la droite.
    led.unplot(bar_x, 4)
    bar_x = bar_x + 1
    led.plot(bar_x + 1, 4)
input.on_button_pressed(Button.B, on_button_pressed_b)

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
    global ball_x, ball_y, ball_dx, ball_dy, bar_x
    ball_x = randint(0, 3)
    # randint(0, 4)
    ball_y = 0
    ball_dx = 1
    ball_dy = 1
    bar_x = 0
    while True:
        led.unplot(ball_x, ball_y)
        # --- Ball Movement ---
        ball_y = ball_y + ball_dy
        ball_x = ball_x + ball_dx
        # One of these lines is 'commented out' with a #. The computer is ignoring it.
        # Should it be active for the game to work properly?
        # Une de ces lignes est 'commentée' avec un #. L'ordinateur l'ignore.
        # Devrait-elle être active pour que le jeu fonctionne bien ?
        # ball_? = ball_? + ball_d?
        # --- Wall Bounces ---
        if ball_y <= 0:
            # This code runs when the ball hits the TOP wall.
            # It should reverse the ball's UP/DOWN speed.
            # HINT: Look at the variable names. Is it changing the correct speed (dx or dy)?
            # Ce code s'exécute quand la balle frappe le mur du HAUT.
            # Il devrait inverser la VITESSE HAUT/BAS de la balle.
            # INDICE: Change-t-il la bonne variable de vitesse (dx ou dy) ?
            ball_dy = 1
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
basic.forever(on_forever)
