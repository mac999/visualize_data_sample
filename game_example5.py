import pygame 
import pandas as pd

pygame.init()   
window = pygame.display.set_mode((600, 600)) 
pygame.display.set_caption("Drawing Design") 

df = pd.read_csv('config.csv')
print(df)

x = df.iloc[0][0]  # 300
y = df.iloc[0][1]  # 300
width = df.iloc[0][2]  # 20
height = df.iloc[0][3]  # 20
vel = df.iloc[0][4]  # 10
run = True

color_red = 0
while run:  
    pygame.time.delay(10)  
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT] and x > 0: 
        x -= vel 
    if keys[pygame.K_RIGHT] and x < 600 - width: 
        x += vel 
    if keys[pygame.K_UP] and y > 0: 
        y -= vel 
    if keys[pygame.K_DOWN] and y < 600 - height: 
        y += vel 
    color_red = color_red + 1
    color_red = color_red % 256
    pygame.draw.rect(window, (color_red, 128, 0), (x, y, width, height)) 
    pygame.display.update() 
pygame.quit()  