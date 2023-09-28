from pico2d import*

WIDTH, HEIGHT = 1100, 600
open_canvas(WIDTH, HEIGHT)
background = load_image('TUK_GROUND.png')
character = load_image('sprite_sheet.png')

def handle_events():
    global running
    global dirX, dirY
    global frameY, frameLen
    global sec
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_LEFT:
                frameY = 2
                frameLen = 10
                dirX -= 1
                sec = 0.05
            elif event.key == SDLK_RIGHT:
                frameY = 0
                frameLen = 10
                dirX += 1
                sec = 0.05
            elif event.key == SDLK_UP:
                frameY = 1
                frameLen = 10
                dirY += 1
                sec = 0.05
            elif event.key == SDLK_DOWN:
                frameY = 3
                frameLen = 10
                dirY -= 1
                sec = 0.05
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                frameY = 6
                frameLen = 3
                sec = 0.1
                dirX += 1
            elif event.key == SDLK_RIGHT:
                frameY = 4
                frameLen = 3
                sec = 0.1
                dirX -= 1
            elif event.key == SDLK_UP:
                frameY = 5
                frameLen = 1
                sec = 0.1
                dirY -= 1
            elif event.key == SDLK_DOWN:
                frameY = 7
                frameLen = 3
                sec = 0.1
                dirY += 1

def check_point():
    global x, y
    if x < 50:
        x = 50
    elif x > WIDTH - 50:
        x = WIDTH - 50
    if y < 50:
        y = 50
    elif y > HEIGHT - 50:
        y = HEIGHT - 50

running = True
frameX, frameY, frameLen = 0, 7, 3
sec = 0.1
x, y = WIDTH//2, HEIGHT//2
dirX, dirY = 0, 0

while(running):
    clear_canvas()
    background.draw(WIDTH//2, HEIGHT//2)
    character.clip_draw(frameX * 96, frameY * 104, 96, 104, x, y)
    update_canvas()
    handle_events()
    frameX = (frameX + 1) % frameLen
    x += dirX * 10
    y += dirY * 10
    check_point()
    delay(sec)

close_canvas()