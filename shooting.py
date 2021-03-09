import pygame
import time

pygame.init()
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
game_window = pygame.display.set_mode((1200,600))
player_x = 38
player_y = 554
player2_y = 554
player2_x = 913
bullet_x = player_x
bullet_y = player_y+20
bullet2_x = player2_x
bullet2_y = player2_y+20
enemy_x = 725
shooter = pygame.image.load('shooter.png')
shooter2 = pygame.image.load('shooter2.png')
health_player_1 = pygame.image.load('1.png')
health_player_2 = pygame.image.load('2.png')
health_player_3 = pygame.image.load('3.png')
player_health = 3
game_over = pygame.image.load('game over1.png')
game_over_check = False

health_player2_1 = pygame.image.load('player2 h1.png')
health_player2_2 = pygame.image.load('player2 h2.png')
health_player2_3 = pygame.image.load('player2 h3.png')
player1_wins = pygame.image.load('game over 2.png')
player2_health = 3
state = False
state2 = False
lock = False
run = True
jump = False
vel_y = 15
vel2_y = 15
jump2 = False
enemy_y = 583
clock = pygame.time.Clock()
while run:
    clock.tick(60)
    for event in pygame.event.get():
        key = pygame.key.get_pressed()

    game_window.fill(white)
    
    player = pygame.draw.rect(game_window,white,[player_x,player_y,63,45])
    # enemy = pygame.draw.rect(game_window,black,[enemy_x,enemy_y,15,29])
    game_window.blit(shooter,(player_x+2,player_y+2))

    player2 = pygame.draw.rect(game_window,white,[player2_x,player2_y,63,45])
    game_window.blit(shooter2,(player2_x+2,player2_y+2))
    
    if player_health == 3:
        game_window.blit(health_player_3,(0,0))

    elif player_health == 2:
        game_window.blit(health_player_2,(0,0))

    elif player_health == 1:
        game_window.blit(health_player_1,(0,0))

    else:
        game_window.fill(white)
        game_window.blit(game_over,(400,150))
        game_over_check = True

    if player2_health == 3:
        game_window.blit(health_player2_3,(1130,0))

    elif player2_health == 2:
        game_window.blit(health_player2_2,(1130,0))

    elif player2_health == 1:
        game_window.blit(health_player2_1,(1130,0))

    

    else:
        game_window.fill(white)
        game_window.blit(player1_wins,(400,150))
        game_over_check = True
        


        

        

    enemy_x -=1
    
    if not state: 
        if key[pygame.K_RCTRL]:
            state = True
            bullet_y = player_y+20
            bullet_x = player_x+1
            
    if not game_over_check:   
        if state:
            bullet = pygame.draw.rect(game_window,(255,0,0),[bullet_x,bullet_y,15,5])
            bullet_x +=47.8
            if bullet.colliderect(player2):
                bullet_x = player_x
                bullet2_y = player2_y+20
                state = False
                player2_health -=1
            
        
    


    if bullet_x>=1180:
        bullet_x = player_x
        bullet2_y = player2_y+20
        state = False


    if key[pygame.K_RIGHT]:
        player_x = player_x+5
      
    if key[pygame.K_LEFT]:
        player_x = player_x-5

    if key[pygame.K_o]:
        print(player_x)

    if key[pygame.K_UP]:
        jump = True

    if jump:
        player_y -= vel_y
        vel_y = vel_y-1
        if vel_y< -15:
            jump = False
            vel_y = 15 

    if key[pygame.K_a]:
        player2_x -=5

    if key[pygame.K_d]:
        player2_x +=5

    if not jump2:
        if key[pygame.K_w]:
            jump2 = True

    if jump2:
        player2_y -= vel2_y
        vel2_y -= 1
        if vel2_y<-15:
            jump2 = False
            vel2_y = 15

    if not state2:
        if not game_over_check:
            if key[pygame.K_SPACE]:
                bullet2_y = player2_y+20
                bullet2_x = player2_x+1
                state2 = True

    if state2:
        bullet_2 = pygame.draw.rect(game_window,red,[bullet2_x,bullet2_y,15,5])
        bullet2_x -=47.8

        if bullet_2.colliderect(player):
            bullet2_x = player2_x
            bullet2_y = player2_y+20
            state2 = False
            player_health -=1

    if bullet2_x<=-17:
        bullet2_y = player2_y+20
        bullet2_x = player2_x
        state2 = False

    
        

    

    pygame.time.delay(15)
    
    pygame.display.update()

