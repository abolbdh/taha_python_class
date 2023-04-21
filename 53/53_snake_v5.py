#  barkhord bomb ba worm

import pygame , sys , random , time


pygame.init()


# variables 
win_w = 800
win_h = 600
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
worm_x = random.randrange(0,win_w - 20,20)
worm_y = random.randrange(0,win_h - 20,20)
speed_worm_x = 0
speed_worm_y = 0
clock = pygame.time.Clock()
fps = 6
food_x = random.randrange(0,win_w -20,20)
food_y = random.randrange(0,win_h -20,20)
worm_list = []
worm_length = 0
game_over = False 
a = ['r','l','u','d'] 
score = 0
font_score = pygame.font.Font(None,40)
scr = 0
bomb_x = random.randrange(0,win_w -20,20)
bomb_y = random.randrange(0,win_h -20,20)

#  make display 
win = pygame.display.set_mode((win_w,win_h))
pygame.display.set_caption('Snake')

# make function for change length of worm   --> tagiir andaze worm
def worm(worm_x,worm_y,worm_list):
    g_over = False
    worm_head = [worm_x,worm_y]
    worm_list.append(worm_head)
    # print(worm_list)
    for item in worm_list:
        pygame.draw.rect(win,green,(item[0],item[1] ,20,20))

    for section in worm_list[:-1]:
        if worm_head == section:
            g_over = True
    return g_over


#  make bomb
def bomb(bomb_x , bomb_y):
    img1 = pygame.image.load('bomb.png')
    IMG1 = pygame.transform.scale(img1,(20,20))
    win.blit(IMG1,(bomb_x,bomb_y))


#  main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT  and 'r' in a:
                speed_worm_x = 20
                speed_worm_y = 0
                a.clear()
                a.append('u')
                a.append('r')
                a.append('d')
            if event.key == pygame.K_LEFT and 'l' in a:
                speed_worm_x = -20
                speed_worm_y = 0
                a.clear()
                a.append('u')
                a.append('l')
                a.append('d')
            if event.key == pygame.K_UP and 'u' in a:
                speed_worm_y = -20
                speed_worm_x = 0
                a.clear()
                a.append('u')
                a.append('r')
                a.append('l')
            if event.key == pygame.K_DOWN and 'd' in a:
                speed_worm_y = 20
                speed_worm_x = 0
                a.clear()
                a.append('l')
                a.append('r')
                a.append('d')

    win.fill(black) 
    # jehat harakat   
    worm_x += speed_worm_x
    worm_y += speed_worm_y    
    # barhgasht be safheh
    if worm_x < 0:
        worm_x = win_w -20
    if worm_x > win_w -20:
        worm_x = 0
    if worm_y > win_h -20:
        worm_y = 0
    if worm_y < 0:
        worm_y= win_h-20     
    # make hit ya barkbhord 
    if score % 5 != 0 or score == 0:
        if worm_x == food_x and worm_y == food_y:
            food_x = random.randrange(0,win_w,20)
            food_y = random.randrange(0,win_h,20)
            score += 1
            worm_length += 1
            scr += 1
            bomb_x = random.randrange(0,win_w -20,20)
            bomb_y = random.randrange(0,win_h -20,20)

    else:
         if worm_x <= food_x + 20 <= worm_x + 20 and worm_y <= food_y + 20 <= worm_y + 20:
            food_x = random.randrange(0,win_w,20)
            food_y = random.randrange(0,win_h,20)
            score += 1
            worm_length += 1
            scr += 5
            bomb_x = random.randrange(0,win_w -20,20)
            bomb_y = random.randrange(0,win_h -20,20)

    # shart afzayesh tool worm
    if len(worm_list) > worm_length:
        worm_list.pop(0)
    # make snake
    game_over = worm(worm_x,worm_y,worm_list)
    #  add big food
    if score % 5 != 0 or score == 0:
        pygame.draw.rect(win,red,(food_x,food_y ,20,20))
    else :
        pygame.draw.rect(win,red,(food_x,food_y ,40,40))

    #  barkord bomb ba worm
    if worm_x == bomb_x and worm_y == bomb_y:
        win.fill(black)
        ex_image = pygame.image.load('explosion.png')
        EX_image = pygame.transform.scale(ex_image,(100,100))
        win.blit(EX_image,(bomb_x- 50,bomb_y-50))
        music = pygame.mixer.music.load('a.mp3')
        pygame.mixer.music.play()
        pygame.display.update()
        time.sleep(3)
        game_over = True

    clock.tick(fps)
    font_score_s = font_score.render(f'score: {str(scr)}', True,green)
    win.blit(font_score_s,(30,30))
    bomb(bomb_x, bomb_y)
    pygame.display.update()        

