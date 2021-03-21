import pygame

pygame.init()
screen_width = 1200
screen_height = 600
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)

game_window = pygame.display.set_mode((screen_width,screen_height))
michel = pygame.image.load('main character R.png')
michel_left = pygame.image.load('main character L.png')
commander_left = pygame.image.load('commander L.png')
commander_right = pygame.image.load('commander R.png')
base = pygame.image.load('base.png')

width = 40
height = 44
player_x = 26
player_y = 555
commander_x = 200
commander_y = 551
run = True
vel_y = 15
jump = False
counter = 1
text_x = 395
text_y = 300
player_blit = False
clock = pygame.time.Clock()
can_move = False
x = 395
y = 200
x2 = 430
y2 = 600
x3 = 395
y3 = 300

draw = True
draw2 = True
text = True
text2 = True
game_starts = False
direction = "right"
commander_direction = "left"

font = pygame.font.SysFont(None, 55)



def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x,y])

while run:
    clock.tick(60)
    for event in pygame.event.get():
        key = pygame.key.get_pressed()
   
    game_window.fill(black)
    if text:
        text_screen('1940 world war 2',white,text_x,text_y)
    if draw:
        pygame.draw.rect(game_window,black,[x,y,15,15])
    x +=4
    if x>=1190:
        draw = False


    if event.type == pygame.QUIT:
        run = False
    
    if not draw:
        text_y -=3
        #-30
        if text_y<=-15:
            text = False
            if text2:
                text_screen('made by oss',white,x2,y2)
                y2 -=3
                

            if y2<=-15:
                text2 = False
                if draw2:
                    pygame.draw.rect(game_window,black,[x3,y3,15,15])
                    x3 +=7
                    if x3>=1190:
                        draw2 = False

                if not draw2:
                    game_window.fill(white)
                    pygame.draw.rect(game_window,white,[player_x,player_y,40,46])
                    if direction == 'right':
                        game_window.blit(michel,(player_x,player_y))
    
                    if direction == "left":
                        game_window.blit(michel_left,(player_x,player_y))
                        
                    if commander_direction == "left":
                        game_window.blit(commander_left,(commander_x,commander_y))

                    if commander_direction == "right":
                        game_window.blit(commander_right,(commander_x,commander_y))
                    


    if can_move:
        if key[pygame.K_RIGHT]:
            direction = "right"
            player_x +=6

        if key[pygame.K_LEFT]:
            direction = "left" 
            player_x -=6

        if not jump:
            if key[pygame.K_UP]:
                jump = True
               
        if jump:
            player_y = player_y - vel_y
            vel_y = vel_y-1
            if vel_y <-15:
                jump = False
                vel_y = 15

    
    
            

    pygame.time.delay(15)
    pygame.display.update()