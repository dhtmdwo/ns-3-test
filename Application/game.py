from cProfile import run
from platform import platform
from numpy import character
import pygame
import random

pygame.init()
pygame.mixer.init()



screen_width = 480
screen_height = 640
pygame.display.set_caption("Network project") #caption 넣기 
screen = pygame.display.set_mode((screen_width,screen_height))#창크기 지정 


background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background,(480,640))
#배경 정보

player = pygame.image.load("player.jpg")
player_height = player.get_size()[1]
player_width = player.get_size()[0]
player_pos_x = (screen_width - player_width)/2
player_pos_y = screen_height - player_height
#player 정보

enemy = pygame.image.load("enemy.jpg")
enemy_height = enemy.get_size()[1]
enemy_width = enemy.get_size()[0]
enemy_pos_x = random.randint(0, screen_width - player_width + 1)
enemy_pos_y = 0
#enemy 정보

clock = pygame.time.Clock()
running = True
speed = 80


pygame.mixer.music.load( "song.mp3" )
pygame.mixer.music.play()

while running:
    clock.tick(60)
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT] ==1:
        player_pos_x -= speed * clock.get_time() / 1000 # 초당으로 하기 때문에 프레임별로 불규칙해질 걱정 없음 

    if key[pygame.K_RIGHT] ==1:
        player_pos_x += speed * clock.get_time() / 1000

    #방향키 눌렀을 때 움직이기 

    if player_pos_x < 0:
        player_pos_x = 0
    
    if player_pos_x > screen_width - player_width:
        player_pos_x = screen_width - player_width

    #화면 밖 나간경우 처리 


    enemy_pos_y += 150 * clock.get_time() / 1000

    if enemy_pos_y > screen_height - enemy_height:
        enemy_pos_x = random.randint(0, screen_width - player_width + 1)
        enemy_pos_y = 0

    #적 위치 처리 

    player_rect = player.get_rect()
    player_rect.x = player_pos_x
    player_rect.y = player_pos_y

    enemy_rect = enemy.get_rect()
    enemy_rect.x = enemy_pos_x
    enemy_rect.y = enemy_pos_y

    #충돌 위한 변수

    if player_rect.colliderect(enemy_rect):
        print('충돌')
        running = False
    #충돌 검사 

    screen.blit(background,(0,0))
    screen.blit(player,(player_pos_x,player_pos_y))
    screen.blit(enemy,(enemy_pos_x,enemy_pos_y))

    pygame.display.update()

pygame.mixer.quit()    
pygame.quit()
