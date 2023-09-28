from pico2d import*

WIDTH, HEIGHT = 1280, 1024
open_canvas(WIDTH, HEIGHT)
background = load_image('TUK_GROUND.png')
character = load_image('sprite_sheet.png')

def handle_events():
    global running
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
                dirX -= 1
            elif event.key == SDLK_RIGHT:
                frameY = 0
                dirX += 1
            elif event.key == SDLK_UP:
                frameY = 1
                dirY += 1
            elif event.key == SDLK_DOWN:
                frameY = 3
                dirY -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                dirX += 1
            elif event.key == SDLK_RIGHT:
                dirX -= 1
            elif event.key == SDLK_UP:
                dirY -= 1
            elif event.key == SDLK_DOWN:
                dirY += 1

running = True
frameX, frameY = 0, 3
x, y = WIDTH//2, HEIGHT//2
dirX, dirY = 0, 0

while(running):
    clear_canvas()
    background.draw(WIDTH//2, HEIGHT//2)
    character.clip_draw(frameX * 96, frameY * 104, 96, 104, x, y)
    update_canvas()
    handle_events()
    frameX = (frameX + 1) % 10
    x += dirX * 10
    y += dirY * 10
    delay(0.05)

close_canvas()