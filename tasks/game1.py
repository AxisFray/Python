


import pygame
import pygame_gui
import sys
import colorama
from game1class import *
import time
# - - - Settings - - - 
bwidth = 800
bheight = 800

money = 0
pygame.init()
window = pygame.display.set_mode((bwidth,bheight))
x = 0
y = 0
font = pygame.font.Font(None, 25)
#text = font.render("You win!", True, BLACK)
#text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
#screen.blit(text, text_rect)
background = pygame.image.load("assets/background1.png")
moneyPic = pygame.image.load("assets/money.png")
font1 = pygame.font.Font(None,20)
font2 = pygame.font.Font(None,30)
font3 = pygame.font.Font(None,40)

BLACK = (0,0,0)
RED = (250,0,0)
BLUE = (0,0,250)
GREEN = (1,43,0)




def main():
    global money
    player = Player()
    
    sunflower_draw = False
    window.blit(background, (0, 0))
    clock_cash = 0
    sunflower = 0
    clock_sunflower = 0
    sunflowers = []
    farmlands = []
    banknotes = []
    while True:
        clock_sunflower += pygame.time.Clock().tick(60)/1000
        clock_cash += pygame.time.Clock().tick(60) / 1000
        pygame.time.Clock().tick(440)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_q or event.type == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            
        keys = pygame.key.get_pressed()
       
        if clock_cash >= 2:
           clock_cash = 0
           banknotes.append(Cash())
        if clock_sunflower >= 2:
            clock_sunflower = 0
            sunflower_draw = True
            
          
        
        # - - - tick - - - 
               
        player.tick(keys)
        
        if keys[pygame.K_1]:
            
            if  farmlands == []:
                farmlands.append(Farmland())
                sunflowers.append(Sunflower())
                farmlands[-1].xcord = player.xcord+(player.width/2)
                farmlands[-1].ycord = player.ycord+(player.height/2)
                sunflowers[-1].xcord = farmlands[-1].xcord
                sunflowers[-1].ycord = farmlands[-1].ycord
                

            else:
                for farmlandd in farmlands:
                    if player.hitbox.colliderect(farmlandd.hitbox):
                        pass
                    else:
                        farmlands.append(Farmland())
                        sunflowers.append(Sunflower())
                        farmlands[-1].xcord = player.xcord+player.width/2
                        farmlands[-1].ycord = player.ycord+player.height/2
                        sunflowers[-1].xcord = farmlands[-1].xcord
                        sunflowers[-1].ycord = farmlands[-1].ycord
                        
                    
        for banknote in banknotes:  #draw hitbox for every banknote
            banknote.tick()
        for farmland1 in farmlands:
            farmland1.tick()
        for sunflower1 in sunflowers:
            sunflower1.tick()
        for banknote in banknotes:  #check collision player and banknote
            if player.hitbox.colliderect(banknote.hitbox):
                banknotes.remove(banknote)
                money += 1
        for sunflower1 in sunflowers: #check collision player and sunflower
            if player.hitbox.colliderect(sunflower1.hitbox):
                sunflowers.remove(sunflower1)
                sunflower +=1

        

        
        # - - - texts and images - - - 
        text1 = str(player.xcord)+" "+str(player.ycord)
        text1_pack = font2.render(text1,True,BLACK)
        text2 = str(money)
        text2_pack = font3.render(text2,True,GREEN)

        
        
        
        
        
        # - - - draw on screen - - - 
        
        window.blit(background,(0,0))
        
        
        window.blit(text1_pack,(0.85*bwidth,10))
        window.blit(text2_pack,(0.75*bwidth,10))
        window.blit(moneyPic,(0.72*bwidth,5))
        for banknote in banknotes:  #drawing generated banknotes
            banknote.draw()
        for farmland2 in farmlands:
            farmland2.draw()
        if sunflower_draw == True:
            for sunflower1 in sunflowers:
                sunflower1.draw()
                sunflower_draw = False
        player.draw()
        pygame.display.update()

if __name__ == "__main__":
    main()