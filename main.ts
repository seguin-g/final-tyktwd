radio.setGroup(1)
let bar_x = 1
let ball_x = 0
let ball_y = 0
let ball_dx = 0
let ball_dy = 0
let has_ball = false
let game_active = true
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (bar_x > 0) {
        led.unplot(bar_x + 1, 4)
        bar_x -= 1
        led.plot(bar_x, 4)
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (bar_x < 3) {
        led.unplot(bar_x, 4)
        bar_x += 1
        led.plot(bar_x + 1, 4)
    }
    
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    if (!has_ball && game_active) {
        ball_x = randint(1, 3)
        ball_y = 3
        ball_dx = 1
        ball_dy = -1
        has_ball = true
    }
    
})
radio.onReceivedValue(function on_received_value(name: string, value: number) {
    
    if (name == "bx") {
        ball_x = 4 - value
        ball_y = 0
        ball_dy = 1
    } else if (name == "bdx") {
        ball_dx = -value
        has_ball = true
    } else if (name == "over") {
        game_active = false
        basic.showIcon(IconNames.Happy)
    }
    
})
basic.forever(function on_forever() {
    
    led.plot(bar_x, 4)
    led.plot(bar_x + 1, 4)
    if (!game_active || !has_ball) {
        basic.pause(50)
        return
    }
    
    led.unplot(ball_x, ball_y)
    ball_y += ball_dy
    ball_x += ball_dx
    //  Horizontal wall bounce
    if (ball_x <= 0 || ball_x >= 4) {
        ball_dx *= -1
    }
    
    //  Send ball to the other device
    if (ball_y <= 0) {
        has_ball = false
        radio.sendValue("bx", ball_x)
        radio.sendValue("bdx", ball_dx)
        return
    }
    
    //  Paddle collision
    if (ball_y >= 4) {
        if (ball_x == bar_x || ball_x == bar_x + 1) {
            ball_dy = -1
        } else {
            game_active = false
            radio.sendValue("over", 1)
            basic.showIcon(IconNames.Sad)
            return
        }
        
    }
    
    led.plot(ball_x, ball_y)
    basic.pause(400)
})
