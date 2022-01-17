import pygame
import random

pygame.init()

dis_width = 800
dis_height = 600
char_size = 24
dog = pygame.image.load('./images/dog.png')
food = pygame.image.load('./images/pizza.png')
clock = pygame.time.Clock()
dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption("Food hunt by Yato")

score_font = pygame.font.SysFont("comicsansms", 25)
font_style = pygame.font.SysFont("bahnschrift", 25)

def your_score(score):
    value = score_font.render("Your Score: " + str(score),True, (0,150,0))
    dis.blit(value, [5,5])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [(dis_width // 2) - 60, dis_height // 2])

def game_loop():
    speed = 10
    game_over = False
    xd = round(dis_width//2 / 24) * 24
    yd = round(dis_height//2 / 24) * 24
    xd_change = 0
    yd_change = 0
    foodx = round(random.randrange(0,dis_width - char_size) / 24) * 24
    foody = round(random.randrange(0,dis_height - char_size) / 24) * 24
    score = 0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xd_change = -24
                    yd_change = 0
                elif event.key == pygame.K_RIGHT:
                    xd_change = 24
                    yd_change = 0
                elif event.key == pygame.K_UP:
                    xd_change = 0
                    yd_change = -24
                elif event.key == pygame.K_DOWN:
                    xd_change = 0
                    yd_change = 24
        if xd < 0 or xd > dis_width-char_size or yd < 0 or yd > dis_height-char_size:
            game_over = True
        xd += xd_change
        yd += yd_change
        dis.fill((255,255,255))
        dis.blit(food,(foodx,foody))
        dis.blit(dog,(xd,yd))
        your_score(score)
        if xd == foodx and yd == foody:
            foodx = round(random.randrange(0,dis_width - char_size) / 24) * 24
            foody = round(random.randrange(0,dis_height - char_size) / 24) * 24
            score += 1
        pygame.display.update()
        clock.tick(speed+score)
    dis.fill((255,255,255))
    message("Game Over!",(150,0,0))
    your_score(score)
    pygame.display.update()
    pygame.time.delay(2500)

game_loop()
