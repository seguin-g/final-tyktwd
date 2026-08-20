radio.set_group(1)

bar_x = 1
ball_x = 0
ball_y = 0
ball_dx = 0
ball_dy = 0
has_ball = False
game_active = True

def on_button_pressed_a():
    global bar_x
    if bar_x > 0:
        led.unplot(bar_x + 1, 4)
        bar_x -= 1
        led.plot(bar_x, 4)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global bar_x
    if bar_x < 3:
        led.unplot(bar_x, 4)
        bar_x += 1
        led.plot(bar_x + 1, 4)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_ab():
    global has_ball, ball_x, ball_y, ball_dx, ball_dy
    if not has_ball and game_active:
        ball_x = randint(1, 3)
        ball_y = 3
        ball_dx = 1
        ball_dy = -1
        has_ball = True
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_value(name, value):
    global has_ball, ball_x, ball_y, ball_dx, ball_dy, game_active
    if name == "bx":
        ball_x = 4 - value
        ball_y = 0
        ball_dy = 1
    elif name == "bdx":
        ball_dx = -value
        has_ball = True
    elif name == "over":
        game_active = False
        basic.show_icon(IconNames.HAPPY)
radio.on_received_value(on_received_value)

def on_forever():
    global ball_x, ball_y, ball_dx, ball_dy, bar_x, has_ball, game_active
    
    led.plot(bar_x, 4)
    led.plot(bar_x + 1, 4)

    if not game_active or not has_ball:
        basic.pause(50)
        return

    led.unplot(ball_x, ball_y)
    
    ball_y += ball_dy
    ball_x += ball_dx

    # Horizontal wall bounce
    if ball_x <= 0 or ball_x >= 4:
        ball_dx *= -1

    # Send ball to the other device
    if ball_y <= 0:
        has_ball = False
        radio.send_value("bx", ball_x)
        radio.send_value("bdx", ball_dx)
        return

    # Paddle collision
    if ball_y >= 4:
        if ball_x == bar_x or ball_x == bar_x + 1:
            ball_dy = -1
        else:
            game_active = False
            radio.send_value("over", 1)
            basic.show_icon(IconNames.SAD)
            return

    led.plot(ball_x, ball_y)
    basic.pause(400)

basic.forever(on_forever)