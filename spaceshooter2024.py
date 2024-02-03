import pgzrun
import random
from helper import *

WIDTH=1024
HEIGHT=768


player = Actor("png/playership1_red")
player.pos = (WIDTH / 2,HEIGHT / 2)
player.hp = 100

enemies = []
enemies = []
player_lasers = []
enemy_lasers = []

def update():
    if keyboard.up:
        player.y -= 5
    if keyboard.down:
        player.y +=5
    if keyboard.left:
        player.x -= 5
    if keyboard.right:
        player.x += 5
    

    if player.left < 0:
        player.left = 0
    if player.right > WIDTH:
        player.right = WIDTH
    if player.top < 0:
        player.top = 0
    if player.bottom > HEIGHT:
        player.bottom = HEIGHT 


    if random.randint(0,100) < 5:
        enemy = Actor("png/enemies/enemyblack1")
        enemy.x = random.randint(0,WIDTH)
        enemies.append(enemy)

    if keyboard.space: 
        laser = Actor("png/lasers/laserred01")
        laser.pos = player.pos
        if enemies:
            laser.point_towards(random.choice(enemies))
        else:
            laser.angle = 90
        player_lasers.append(laser)
        
    for l in player_lasers:
        l.move_forward(5)
        if l.bottom < 0:
            player_lasers.remove(l)
        else:   
            for e in enemies:
                if l.colliderect(e):
                    player_lasers.remove(l)
                    enemies.remove(e)
                    break
                

    for  e in enemies:
        e.point_towards(player)
        e.move_forward(3)
        if e.colliderect(player):
            enemies.remove(e)
            player.hp -= 5
        else:          
            if random.randint(0,100) < 1:
                l = Actor("png/lasers/lasergreen13")
                l.pos = e.pos
                l.point_towards(player)
                enemy_lasers.append(l)

    for l in enemy_lasers:
        l.move_forward(5)
        if l.top > HEIGHT:
            enemy_lasers.remove(l)
        else:
            if l.colliderect(player):
                enemy_lasers.remove(l)
                player.hp -= 1

                
        

def draw():
    screen.clear()
    if player.hp > 0:
        player.draw()
        for e in enemies:
            e.draw()
        for l in player_lasers:
            l.draw()
        for l in enemy_lasers:
            l.draw()
        hp_bar = Rect(0,0,WIDTH*player.hp/100, 20)
        screen.draw.filled_rect(hp_bar, 'green')
    else:
        screen.draw.text("YOU LOSE", (WIDTH/2, HEIGHT/2), fontsize=100)
        


pgzrun.go()
