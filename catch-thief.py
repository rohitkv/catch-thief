import pygame, sys, random
from pygame import *

pygame.init()

def game():
    #make window called screen and initialize the background
    width, height = 800, 500
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Star Catcher Game')
    
    #background image... give your own path to an image file
    background = pygame.image.load('d.jpg')
    
    background = pygame.transform.scale(background, (width, height))
   
    #load target in array and load player size
    playerwidth, playerheight = 40, 40
    targetwidth, targetheight = 20, 20
    targetnum = 10
    target = []

    for i in range(targetnum):
        
        #thief image... give your own path to an image file
        targetimage = pygame.image.load('t.gif')
        targetimage = pygame.transform.scale(targetimage, (20, 20))
        target.append([])
        target[i] = targetimage

    targetpos = []
    targetspace = height/targetnum-targetheight/2
    for i in range(targetnum):
        targetpos.append([])
        for j in range(2):
            targetpos[i].append(i*j*targetspace+targetwidth)

    #target visible setup of the array
    targetvisible = []
    for i in range(targetnum):
        targetvisible.append(True)

    #load player image
    player = pygame.image.load('man.jpg')
    player = pygame.transform.scale(player, (playerwidth, playerheight))
    px, py = (width-playerwidth)/2, (height-playerheight)/2

    #speed of game and other variable initiated
    clock = pygame.time.Clock()
    gamespeed = 100
    movex = movey = 0

    speed = []
    for i in range(targetnum):
        speed.append([])
        for j in range(2):
            speed[i].append(gamespeed*random.randint(1,5))
            
    score = 0
    timer = 0
    
    #this is score text loading
    gamefont = pygame.font.Font(None, 30)
    scoretext = gamefont.render('Player Score: '+str(score), 1, [100, 80, 130])
    boxsize = scoretext.get_rect()
    scoreXpos = (width-boxsize[2])/2
    timertext = gamefont.render('Timer: '+str(timer), 1, [55, 75, 150])
    boxsize = timertext.get_rect()
    timerXpos = (width-boxsize[2])/2
    
    startscreen = True
    while startscreen:
        pygame.mouse.set_visible(0)
        screen.blit(background, [0, 0])
        screen.blit(player, (px, py))
        scoretext = gamefont.render('Player Score: '+str(score), 1, [100, 80, 140])
        screen.blit(scoretext, [scoreXpos, 20])
        timertext = gamefont.render('Timer: '+str(timer), 1, [55, 80, 160])
        screen.blit(timertext, [timerXpos, 50])

        for i in range(targetnum):
            targetimage = target[i]
            x = targetpos[i][0]
            y = targetpos[i][1]
            screen.blit(targetimage, (x, y))
        instructtext = gamefont.render('Use the mouse to colllect the stars',1,[25,90,20])
        screen.blit(instructtext, [targetwidth*3, 80])
        instructtext2 = gamefont.render('Hit the spacebar to start', 1, [200,10,25])
        screen.blit(instructtext2, [targetwidth*3, 160])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    startscreen = False
    
    #running of the game loop
    while True:


        #keyboard/mouse movements
        pygame.mouse.set_visible(0)
        playerleft, playertop = pygame.mouse.get_pos()
        px, py = playerleft-playerwidth/2, playertop-playerheight/2
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

##            elif event.type == KEYDOWN:
##                if event.key == K_RIGHT:
##                    movex = 2
##                if event.key == K_LEFT:
##                    movex = -2
##                if event.key == K_UP:
##                    movey = -2
##                if event.key == K_DOWN:
##                    movey = 2
##                    
##            elif event.type == KEYUP:
##                if event.key == K_RIGHT:
##                    movex = 0
##                if event.key == K_LEFT:
##                    movex = 0
##                if event.key == K_UP:
##                    movey = 0
##                if event.key == K_DOWN:
##                    movey = 0
##
##        px = px + movex
##        py = py + movey

        #test for the sides of the screen
        for i in range(targetnum):        
            if targetpos[i][0]>width or targetpos[i][0]<0:
                speed[i][0] = -speed[i][0]
                targetpos[i][0] += seconds*speed[i][0]

            if targetpos[i][1]>height or targetpos[i][1]<0:
                speed[i][1] = -speed[i][1]
                targetpos[i][1] += seconds*speed[i][1]

        #this is collision test
        for i in range(targetnum): 
            if abs(targetpos[i][0]-px)<20 and abs(targetpos[i][1]-py)<20:
                targetvisible[i] = False
                score += 10
                targetpos[i] = [width + 100, height + 100]

        #timer increment
        seconds = clock.tick()/1000.0
        timer += seconds
        displaytimer = timer
        
        #image display updates
        screen.blit(background, (0, 0))
        screen.blit(player, (px, py))
        scoretext = gamefont.render('Player Score: '+str(score), 2, [255, 0, 0])
        screen.blit(scoretext, [scoreXpos, 20])
        timertext = gamefont.render('Timer: '+str(displaytimer), 1, [255, 0, 0])
        screen.blit(timertext, [timerXpos, 50])

        #targets blitted through a for loop
        for i in range(targetnum):
            if targetvisible[i]:
                targetpos[i][0] += seconds*speed[i][0]
                targetpos[i][1] += seconds*speed[i][1]
                targetimage = target[i]
                x = targetpos[i][0]
                y = targetpos[i][1]
                screen.blit(targetimage, (x, y))
            else:
                targetimage = target[i]
                x = width-50
                y = height-(i+1)*targetspace
                screen.blit(targetimage, (x, y))
        pygame.display.update()


        #loop back through game() if collect all stars
        if score == targetnum*10:
            pygame.time.delay(2000)
            game()
                
#python's way of running the main routine
if __name__=='__main__':
    game()

