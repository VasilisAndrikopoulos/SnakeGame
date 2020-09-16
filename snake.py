import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def score(scr):
    value = score_font.render("Your Score: " + str(scr), True, yellow)
    dis.blit(value, [0, 0])

def snake_body(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])


def gameLoop():
    game_over = False
    game_close = False

    hor = dis_width / 2
    ver = dis_height / 2

    hor_change = 0
    ver_change = 0

    snake_list = []
    snake_length = 1

    food_hor = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    food_ver = round(random.randrange(0, dis_height - snake_block) /10.0) * 10.0

    while not game_over:
        while game_close == True:
            dis.fill(white)
            message("You lost! Press Q-Quit or C-Play Again", red)
            score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    hor_change = -snake_block
                    ver_change = 0
                elif event.key == pygame.K_RIGHT:
                    hor_change = snake_block
                    ver_change = 0
                elif event.key == pygame.K_UP:
                    hor_change = 0
                    ver_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    hor_change = 0
                    ver_change = snake_block

            
        hor += hor_change
        ver += ver_change
        if hor >= dis_width:
                hor = 0
                ver = ver
        elif hor <= 0:
                hor = dis_width
                ver = ver
        elif ver >= dis_height:
                hor = hor
                ver = 0
        elif ver <= 0:
                hor = hor
                ver = dis_height

        dis.fill(blue)    
        pygame.draw.rect(dis, green, [food_hor, food_ver, snake_block, snake_block])
        snake_head = []
        snake_head.append(hor)
        snake_head.append(ver)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        snake_body(snake_block, snake_list)
        score(snake_length - 1)

        pygame.display.update()

        if hor == food_hor and ver == food_ver:
            food_hor = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            food_ver = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
