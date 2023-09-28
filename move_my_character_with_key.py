from pico2d import*

WIDTH, HEIGHT = 1280, 1024
open_canvas(WIDTH, HEIGHT)
background = load_image('TUK_GROUND.png')
character = load_image('sprite_sheet.png')

running = True
frameX, frameY = 0, 1
x, y = WIDTH//2, HEIGHT//2

while(running):
    clear_canvas()
    background.draw(x, y)
    character.clip_draw(frameX * 64, frameY * 64, 64, 64, x, y)
    update_canvas()
    frameX = (frameX + 1) % 9
    delay(0.05)

close_canvas()