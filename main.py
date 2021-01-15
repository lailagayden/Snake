import pygame
from pygame.locals import *

pygame.init()

screen_width = 400
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")

#define game variables 
cell_size = 10

#create snake
snake_pos=[[int(screen_width/2), int(screen_height/2)]]
snake_pos.append([int(screen_width/2), int(screen_height/2)+cell_size])
snake_pos.append([int(screen_width/2), int(screen_height/2)+cell_size*2])
snake_pos.append([int(screen_width/2), int(screen_height/2)+cell_size*3])



#define colors
bg=((255,200,150))
body_inner=(50,175,25)
body_outer=(100,100,200)

def draw_screen():
  screen.fill(bg)


run=True
while run:
  draw_screen()
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      run=False
  pygame.display.update()

  #draw snake 
  for x in snake_pos:
    pygame.draw.rect(screen,body_outer,(x[0],x[1],cell_size,cell_size))
    pygame.draw.rect(screen,body_inner,(x[0]+1,x[1]-2,cell_size,cell_size))

pygame.quit()