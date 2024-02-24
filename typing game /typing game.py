import pgzrun
from helper import *
WIDTH = 650
HEIGHT = 650

run_img = [
    'zombie/run/tile002',
    'zombie/run/tile003',
    'zombie/run/tile004',
    'zombie/run/tile005',           
]
zombie_die = [
    'zombie/die/tile014',
    'zombie/die/tile015',
    'zombie/die/tile016',
    'zombie/die/tile017',
    'zombie/die/tile018',
    'zombie/die/tile019',
    'zombie/die/tile020',
    'zombie/die/tile021',
    'zombie/die/tile022',
    'zombie/die/tile023',
    'zombie/die/tile024',
]
zombie = Actor(run_img[0])
zombie.images = run_img
zombie.scale = 6
zombie.bottom = HEIGHT
zombie.right = WIDTH
zombie.fps = 10


wizard_img = [
    'wizard/idle/tile000',
    'wizard/idle/tile001',
    'wizard/idle/tile002',
    'wizard/idle/tile003',
    'wizard/idle/tile004',
    'wizard/idle/tile005',
]
wizard = Actor(wizard_img[0])
wizard.images = wizard_img
wizard.scale = 2
wizard.bottom = 350
wizard.left = 10

question = "qwertyuiop"
typed = ''
def update():
    zombie.animate()
    wizard.animate()

def on_key_down(key):
    global typed
    print(key, chr(key))
    if key in range(97, 1222+1):
        typed+=chr(key)
    if key == 32:
        typed += ''
    if key == 8:
        typed = typed[0:-1]
    if typed == question:
        typed == ''
        zombie.images = zombie_die
    if zombie.images == zombie_die[-1]:             
        zombie.images =run_img

    

def draw():
    screen.clear()
    zombie.draw()
    wizard.draw()
    screen.draw.text(question, (WIDTH/3, HEIGHT/10),fontsize=60)
    screen.draw.text(typed,(WIDTH/3, HEIGHT/10), color='orange', fontsize=60)
pgzrun.go()
