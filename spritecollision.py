import pygame
import random

# Constants for easier adjustments
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 72

# Initialize Pygame
pygame.init()

background_image= pygame.transform.scale(pygame.image.load("bg2.jpg"),(SCREEN_WIDTH, SCREEN_HEIGHT))
                                         
# Load font once at the beginning
font = pygame.font.SysFont("Times New Roman", FONT_SIZE)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color('dodgerblue'))  # Background color of sprite
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
    def move(self, x_change, y_change):
        self.rect.x=max(min(self.rect.x+ x_change,SCREEN_WIDTH- self.rect.width),0)
        self.rect.y=max(min(self.rect.y+ y_change,SCREEN_HEIGHT- self.rect.height),0)
        
        
# reference : https://replit.com/@Codingal/sprite-collision-SPCM6L4A1?v=1#main.py        


        
        
    
    
    

  
   
    
    
