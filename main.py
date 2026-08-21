def on_button_pressed_a():
    global bar_x
    if bar_x >= 1:
        led.unplot(bar_x + 1, 4)
        bar_x = bar_x - 1
        led.plot(bar_x, 4)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global game_active, has_ball, ball_x, ball_y, ball_dx, ball_dy
    basic.clear_screen()
    game_active = True
    has_ball = True
    ball_x = randint(0, 3)
    ball_y = 0
    ball_dx = 1
    ball_dy = 1
    led.plot(ball_x, ball_y)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    global game_active, has_ball, ball_dx, ball_dy, players
    if receivedString == "start":
        images.create_image("""
            . # # . .
            # . . # .
            . . # . .
            . # . . .
            # # # # .
            """).show_image(0)
        game_active = True
        has_ball = False
        ball_dx = 0
        ball_dy = 0
        players = 2
        basic.pause(1000)
        basic.clear_screen()
        led.plot(bar_x, 4)
        led.plot(bar_x + 1, 4)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global bar_x
    if bar_x < 3:
        led.unplot(bar_x, 4)
        bar_x = bar_x + 1
        led.plot(bar_x + 1, 4)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_received_value(name, value):
    global ball_x, ball_dx, ball_dy, has_ball
    if name == "ball_x":
        ball_x = value
        ball_dx = 1
        ball_dy = 1
        has_ball = True
radio.on_received_value(on_received_value)

ball_dy = 0
ball_dx = 0
ball_y = 0
ball_x = 0
bar_x = 0
has_ball = False
game_active = False
players = 0
radio.set_group(0)
images.create_image("""
    . . # . .
    . # # . .
    . . # . .
    . . # . .
    . # # # .
    """).show_image(0)
players = 1
game_active = False
has_ball = False
bar_x = 2
basic.pause(1000)
basic.clear_screen()
led.plot(bar_x, 4)
led.plot(bar_x + 1, 4)

def on_forever():
    global ball_y, ball_x, ball_dy, has_ball, ball_dx, game_active
    while game_active and has_ball:
        led.unplot(ball_x, ball_y)
        ball_y = ball_y + ball_dy
        ball_x = ball_x + ball_dx
        if players == 1:
            if ball_y < 1:
                ball_dy = 1
        else:
            if ball_y < 0:
                has_ball = False
                continue
        if ball_x <= 0 or ball_x >= 4:
            ball_dx = ball_dx * -1
        # --- Paddle Check ---
        if ball_y >= 4:
            if ball_x == bar_x or ball_x == bar_x + 1:
                ball_dy = -1
            else:
                game_active = False
                game.game_over()
        led.plot(ball_x, ball_y)
        led.plot(bar_x, 4)
        led.plot(bar_x + 1, 4)
        basic.pause(400)
    basic.pause(400)
basic.forever(on_forever)