import pygame
pygame.init()
window= pygame.display.set_mode((500,500))
window.fill((255,255,255))
RED= (255,0,0)
pygame.draw.circle(window,RED,(300,300),50)
pygame.draw.circle(window,RED,(100,100),50,3)
pygame.display.update()
running= True 
while running:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running= False
pygame.quit()

