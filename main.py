from utils import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Drawing Program')

run = True

while run:
   for event in pygame.event.get():
      if(event.type) == pygame.QUIT:
         run = False

pygame.quit()