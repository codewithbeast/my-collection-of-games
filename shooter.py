import pygame
import os


pygame.init()
pygame.mixer.init()
screen_width = 1200
screen_height = 600 
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)
os.chdir("D:\\vs code python\\assets")
print(os.getcwd())
# images
game_window = pygame.display.set_mode((screen_width,screen_height))
michel = pygame.image.load('main character R.png')
michel_left = pygame.image.load('main character L.png')
commander_left = pygame.image.load('commander L.png')
commander_right = pygame.image.load('commander R.png')
tank = pygame.image.load('tank R.png')
tank2 = pygame.image.load('tank L.png')
helicopter_left = pygame.image.load('helicopter L.png')
helicopter_right = pygame.image.load('helicopter R.png')
bullet_1 = pygame.image.load('bullet L.png')
bullet_2 = pygame.image.load('bullet R.png')
bullet_direction = 'right'
black_background = pygame.image.load('Untitled.png')


pygame.mixer.music.load('shooting sound.mp3')
width = 40
height = 44
player_x = 400
player_y = 555
commander_x = 500
commander_y = 551
tank_x = 30
tank_y = 500
tank2_x = 800
tank2_y = 500
run = True
vel_y = 15
jump = False
state = True
counter = 1
text_x = 395
text_y = 300
player_blit = False
clock = pygame.time.Clock()
can_move = False
play_music = False

x = 395
y = 200
x2 = 430
y2 = 600
x3 = 395
y3 = 300
sub_x = 10
sub_y = 50
can_start = False

draw = True
draw2 = True
text = True
text2 = True
game_starts = False
say_1 = False
check = False
state = False
sub_draw = False
sub2_x = 10
sub2_y = 50
direction = "right"
render = True
render2 = False
commander_direction = "left"
helicopter_direction = "left"
helicopter_x = 600
helicopter_y = 476
helicopter_width = 371
helicopter_height = 136
on_helicopter = False
can_enter_helicopter = False
can_eject = False
do = False
ejected = False
landing = False
helicopter_move_x = False
helicopter_disappear_y = 10
helicopter_disappear_x = 10
helicopter_disappear = False
mission_loaded = False
set_player_pos_to_helicopter = False
ammo = 4
total_reload = 60
reduce_ammo = False
draw_enemies = False
mission = 0
enemy_health = 75
enemy_x=70
enemy_y=555
enemy_direction = "right"

font = pygame.font.SysFont(None, 55)
# functions

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x,y])




def enter_check():
    global can_enter_helicopter
    global on_helicopter
    if can_enter_helicopter == True:
        if key[pygame.K_f]:
            on_helicopter = True
            

        if on_helicopter:
            can_enter_helicopter = False 


class vehicel:
    def come_out(self):
        global set_player_pos_to_helicopter
        global on_helicopter
        global can_enter_helicopter
        global can_eject
        global ejected
        global player_y
        global helicopter_y
        if can_eject:
            if on_helicopter:
                if key[pygame.K_e]:
                    on_helicopter = False
                    can_enter_helicopter = True
                    ejected = True
                    set_player_pos_to_helicopter = True

    def auto_eject(self):
        global set_player_pos_to_helicopter
        global on_helicopter
        global can_enter_helicopter
        global can_eject
        global ejected
        global player_y
        global helicopter_y
        if can_eject:
            if on_helicopter:
                on_helicopter = False
                can_enter_helicopter = True
                ejected = True
                set_player_pos_to_helicopter = True



# objects of classes
vehicel = vehicel()




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
                    
                    if direction == 'right':
                        if not on_helicopter:
                            player = pygame.draw.rect(game_window,red,[player_x,player_y,40,44])
                            game_window.blit(michel,(player_x,player_y))
    
                    if direction == "left":
                        if not on_helicopter:
                            player = pygame.draw.rect(game_window,white,[player_x,player_y,40,44])
                            game_window.blit(michel_left,(player_x,player_y))
                        
                    if commander_direction == "left":
                        if not can_move:
                            game_window.blit(commander_left,(commander_x,commander_y))

                    if commander_direction == "right":
                        if not can_move:
                            game_window.blit(commander_right,(commander_x,commander_y))
                    
                    if not can_move:
                        game_window.blit(tank,(tank_x,tank_y))
                        game_window.blit(tank2,(tank2_x,tank2_y))
                        render = True
                        font = pygame.font.SysFont(None,35)
                        sub_draw = True

                    if not set_player_pos_to_helicopter:
                        if helicopter_disappear:
                            game_window.blit(black_background,(0,0)) 
                            
                        
                        

    if sub_draw:
        a = pygame.draw.rect(game_window,white,[sub_x,sub_y,15,15])
        sub_x+=6
        if sub_x>=1150:
            render = False
            if not sub2_x>=1150:
                render2 = True

        if render:
            text_screen('commander: hey joans i have a misson for you',red,20,10)
            

        if render2:
            text_screen('commander: your mission is to steal the secret documents of enemy now go',red,20,10)
            b = pygame.draw.rect(game_window,white,[sub2_x,sub2_y,15,15])
            sub2_x+=6

        if sub2_x>=1150:
            can_move = True
            render2 = False
                

    

                    
    if can_move:
        if key[pygame.K_RIGHT]:
            if not state:
                direction = "right"
            player_x +=6

        if key[pygame.K_LEFT]:
            if not state:
                direction = "left" 
            player_x -=6

        if not jump:
            if not landing:
                if key[pygame.K_UP]:
                    jump = True
               
        if jump:
            player_y = player_y - vel_y
            vel_y = vel_y-1
            if vel_y <-15:
                jump = False
                vel_y = 15

        if not helicopter_disappear: 
            helicopter = pygame.draw.rect(game_window,red,[helicopter_x,helicopter_y,helicopter_width,helicopter_height])
            if helicopter_direction == "right":
                game_window.blit(helicopter_right,(helicopter_x,helicopter_y))

            else:
                game_window.blit(helicopter_left,(helicopter_x,helicopter_y))
        if not ejected:  
            if player.colliderect(helicopter):
                if not on_helicopter:
                    text_screen('press f to enter the helicopter',red,10,10)
                if direction == 'right':
                    player_x = 574
                    can_enter_helicopter = True
                

            else:
                can_enter_helicopter = False
                

        if key[pygame.K_o]:
            print(player_x,player_y)
    
        
        if not state:
            if not on_helicopter:
                if key[pygame.K_SPACE]:
                    if ammo>0:
                        state = True
                    if direction == "right":
                        bullet_x = player_x+20

                    else:
                        bullet_x = player_x-20
                    bullet_y = player_y+20

                
                    

        if state:
            bullet = pygame.draw.rect(game_window,red,[bullet_x,bullet_y,27,10],2)
            if direction == "right":
                game_window.blit(bullet_2,(bullet_x,bullet_y))
                bullet_x +=35


            if direction == "left":
                game_window.blit(bullet_1,(bullet_x,bullet_y))
                bullet_x -=35


            if bullet_x>=1150:
                state = False
                reduce_ammo = True
                if reduce_ammo:
                    ammo-=1
                    reduce_ammo = False

                pygame.mixer.music.play()



            if bullet_x<=4:
                state = False
                reduce_ammo = True
                if reduce_ammo:
                    ammo -= 1
                    reduce_ammo = False

                pygame.mixer.music.play()


          
        enter_check()
        vehicel.come_out()

        if on_helicopter:
            if helicopter_y>=84:
                helicopter_y -=1
                player_y -= 1
                

            if not helicopter_y>=84:
                helicopter_move_x = True

            landing = True



        if ejected:
            player_y +=1
            # print(player_y)

        if player_y>=556:
            ejected = False
            landing = False
            player_y = 555
            draw_enemies = True



        if helicopter_move_x:
            if not helicopter_x<= -40:
                helicopter_x -=1
                if not set_player_pos_to_helicopter:
                    player_x -=0.5 
                    

            

        if helicopter_x<= -40:
            helicopter_disappear = True
            pygame.draw.rect(game_window,black,[helicopter_disappear_x,helicopter_disappear_y,15,15])
            helicopter_disappear_x +=5
         


        if helicopter_disappear_x>=1160:
            helicopter_disappear = False
            mission_loaded = True


        if helicopter_disappear:
            # font = pygame.font.SysFont(None,55)
            # text_screen('loading mission',white,450,270)
            helicopter_direction = "right"
            helicopter_x = -380
        

            

        if helicopter_disappear:
            font = pygame.font.SysFont(None,55)
            text_screen('loading mission...',white,460,300)
            
        if mission_loaded:
            helicopter_x +=2
            if not set_player_pos_to_helicopter:
                player_x +=0.5

            if helicopter_x>=30:
                can_eject = True

        if state:
            if bullet.colliderect(helicopter):
                state = False
                reduce_ammo = True
                if reduce_ammo:
                    ammo -= 1
                    reduce_ammo = False

                pygame.mixer.music.play()



        if total_reload>0:
            if ammo <= 0:
                # print(ammo)
                if key[pygame.K_r]:
                    ammo += 4
                    total_reload -=4

            

        if key[pygame.K_g]:
            print(f"you have {ammo},ammo left in your gun")
            print(f"you have{total_reload} ammo left with you to reload")


        if (can_eject):
            if helicopter_x>=400:
                vehicel.auto_eject()


        if (draw_enemies):
            if (enemy_health>0):
                enemy1 = pygame.draw.rect(game_window,red,[enemy_x,enemy_y,20,50])
                if not enemy_x>=1150:
                    if not enemy_direction == "left": 
                        enemy_direction = "right"

                
                

                else:
                    if enemy_direction == "right":
                        enemy_direction = "left"

                if enemy_x<=-4:
                    if enemy_direction == "left":
                        enemy_direction = "right"
                        
                
                    



            if enemy_direction == "right":
                enemy_x+=5

            elif enemy_direction == "left":
                enemy_x-=5

            


            if state:
                if enemy1.colliderect(bullet):
                    enemy_health -=1
                    state = False
                    reduce_ammo = True
                    print(f"enemy health is {enemy_health}")


        if reduce_ammo:
            ammo -=1
            reduce_ammo = False
        




    pygame.time.delay(18)
    pygame.display.update()