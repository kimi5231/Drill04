from pico2d import*

WIDTH, HEIGHT = 1280, 1024
open_canvas(WIDTH, HEIGHT)
background = load_image('TUK_GROUND.png')
character = load_image('sprite_sheet.png')

def handle_events():
    global running
    global x, y
    global dirX, dirY
    global frameY
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_LEFT:
                frameY = 2
                dirX = -1
            elif event.key == SDLK_RIGHT:
                frameY = 0
                dirX = 1
            elif event.key == SDLK_UP:
                frameY = 3
                dirY = 1
            elif event.key == SDLK_DOWN:
                frameY = 1
                dirY = -1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT or event.key == SDLK_RIGHT:
                dirX = 0
            elif event.key == SDLK_UP or event.key == SDLK_DOWN:
                dirY = 0

running = True
frameX, frameY = 0, 1
x, y = WIDTH//2, HEIGHT//2
dirX, dirY = 0, 0

while(running):
    clear_canvas()
    background.draw(WIDTH//2, HEIGHT//2)
    character.clip_draw(frameX * 64, frameY * 64, 64, 64, x, y)
    update_canvas()
    handle_events()
    frameX = (frameX + 1) % 9
    x += dirX * 10
    y += dirY * 10
    delay(0.05)

close_canvas()