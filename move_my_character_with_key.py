from pico2d import*

WIDTH, HEIGHT = 1280, 1024
open_canvas(WIDTH, HEIGHT)
background = load_image('TUK_GROUND.png')
character = load_image('sprite_sheet.png')

def handle_events():
    global running
    global x, y
    global frameY
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

running = True
frameX, frameY = 0, 1
x, y = WIDTH//2, HEIGHT//2

while(running):
    clear_canvas()
    background.draw(WIDTH//2, HEIGHT//2)
    character.clip_draw(frameX * 64, frameY * 64, 64, 64, x, y)
    update_canvas()
    handle_events()
    frameX = (frameX + 1) % 9
    delay(0.05)

close_canvas()