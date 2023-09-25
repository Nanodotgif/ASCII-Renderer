import asciirenderer as ar
import keyboard as kb
import os

ar.FRAME_RATE = 30
debug_info = ''
top_bar = ar.create_renderable(0,0, [' '])
ball_vel_x = 1
ball_vel_y = 0

paddle_left = ar.create_renderable(0,0, ['█', '█', '█'], visible=True, color=3)
paddle_right = ar.create_renderable(0,0, ['█', '█', '█'], visible=True, color=2)
ball = ar.create_renderable(0,0, ['•'])

def terminate():
    ar.stop()
    os._exit(1)

def place_objects():
    paddle_left.set_position(5, ar.get_center()[1]-1)
    paddle_right.set_position(ar.WIDTH - 5, ar.get_center()[1]-1)
    ball.set_position(ar.get_center()[0], ar.get_center()[1])

def player_move(paddle, direction):
    if direction == 'up' and paddle.y-1 > 0:
        paddle.set_position(paddle.x, paddle.y-1)
    elif direction == 'down' and paddle.y+1 < ar.HEIGHT-2:
        paddle.set_position(paddle.x, paddle.y+1)

def check_collisions():
    global ball_vel_x
    global ball_vel_y
    for paddle in (paddle_left, paddle_right):
        if ball.x == paddle.x :
            if ball.y == paddle.y:
                ball.color = paddle.color
                ball_vel_x *= -1
                ball_vel_y = -1
                pass
            elif ball.y == paddle.y+1:
                ball.color = paddle.color
                ball_vel_x *= -1
                ball_vel_y = 0
                pass
            elif ball.y == paddle.y+2:
                ball.color = paddle.color
                ball_vel_x *= -1
                ball_vel_y = 1
                pass
    if ball.y == 0 or ball.y == ar.HEIGHT:
        ball_vel_y *= -1
    if ball.x == 0 or ball.x == ar.WIDTH:
        ball.set_position(ar.get_center()[0], ar.get_center()[1])
        ball.set_color(1)



kb.add_hotkey("q", terminate)

def frame_update():
    global debug_info
    debug_info = f"Seconds: {int(ar.frame_id / ar.FRAME_RATE)} || Frame: {ar.frame_id} || Center: {ar.get_center()} || Delta Time: {ar.DELTA_TIME():.2f} || Frame Time = {ar.frame_delta:.5f} || ball vel: {ball_vel_x, ball_vel_y}"
    top_bar.visual = [f'===[q: quit | o: options]{"".join(["=" for _ in range(ar.WIDTH - (27+len(debug_info)))])}[{debug_info}]']
    if kb.is_pressed('w'):
        player_move(paddle_left, 'up')
    elif kb.is_pressed('s'):
        player_move(paddle_left, 'down')
    if kb.is_pressed('up arrow'):
        player_move(paddle_right, 'up')
    elif kb.is_pressed('down arrow'):
        player_move(paddle_right, 'down')

    check_collisions()

    ball.set_position(ball.x+ball_vel_x, ball.y+ball_vel_y)

    pass

ar.create_event(1, place_objects) # need to do on first frame and not before because ar.HEIGHT and ar.WIDTH are calculated after start.
ar.start(frame_update)

# [ ] Scoring
# [ ] Normalize ball movement
# [ ] Sounds
# [ ] Win and lose
# [ ] AI?