#!/usr/bin/env python
import pygame
import random
import sys

pygame.init()

game_over = False


width = 800
hight = 600 
red = (255,0,0)
blue = (0,0,255)
yellow = (255,255,0)
player_size = 50
enemy_size = 50
enemy_speed = 10
font = pygame.font.SysFont("monospace", 35)

bg_color = (0,0,50)

player_position = [350,hight-2*player_size]
enemy_position = [random.randint(0,width-enemy_size),0]
enemy_list = []

screen = pygame.display.set_mode((width, hight))

score = 0

clock = pygame.time.Clock()

def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.09:
        x_pos = random.randint(0,width-enemy_size)
        y_pos = 0
        enemy_list.append([x_pos,y_pos])

def draw_enemies(enemy_list):
    for enemy_position in enemy_list:
        pygame.draw.rect(screen, blue,(enemy_position[0],enemy_position[1],enemy_size,enemy_size))


def update_enemy_positions(enemy_list, score):
    for idx, enemy_position in enumerate(enemy_list):
        if enemy_position[1] >= 0 and enemy_position[1] < hight:
            enemy_position[1] = enemy_position[1] + enemy_speed
        else:
            enemy_list.pop(idx)
            score = score + 1
    return score

def collision_check(enemy_list, player_position):
    for enemy_position in enemy_list:
        if detect_collision(enemy_position,player_position):
            return True
    return False


def detect_collision(player_position, enemy_position):
    p_x = player_position[0]
    p_y = player_position[1]

    e_x = enemy_position[0]
    e_y = enemy_position[1]

    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True
    return False


 
while not game_over:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x = player_position[0]
            y = player_position[1]
            if event.key == pygame.K_LEFT:
                x = x - player_size
            elif event.key == pygame.K_RIGHT:
                x = x + player_size
            player_position = [x , y] 


    screen.fill(bg_color)



    drop_enemies(enemy_list)
    score = update_enemy_positions(enemy_list, score)
    text = "score: " + str(score)
    label = font.render(text,1,yellow)
    screen.blit(label,(width-250,hight-40))


    if collision_check(enemy_list, player_position):
        game_over = True
        break
    draw_enemies(enemy_list)
    

    pygame.draw.rect(screen, red, (player_position[0], player_position[1], player_size, player_size))
    
    clock.tick(30)


    pygame.display.update()
