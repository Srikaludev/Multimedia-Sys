import pyglet

window = pyglet.window.Window(800, 600, "Bouncing Ball Animation")
ball_image = pyglet.image.load('ball.jpg')
ball = pyglet.sprite.Sprite(ball_image, x=window.width//2, y=window.height//2)

ball_velocity_x = 200  
ball_velocity_y = 200

def update(dt):
    global ball_velocity_x, ball_velocity_y

    ball.x += ball_velocity_x * dt
    ball.y += ball_velocity_y * dt

    # Bounce off the walls
    if ball.x <= 0 or ball.x + ball.width >= window.width:
        ball_velocity_x *= -1
    if ball.y <= 0 or ball.y + ball.height >= window.height:
        ball_velocity_y *= -1

@window.event
def on_draw():
    window.clear()
    ball.draw()

pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()
