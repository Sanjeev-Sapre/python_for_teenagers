# step 5 move pipes
# 
# 
import pgzrun
import random

TITLE = 'My Flappy Bird Game'
WIDTH = 400
HEIGHT = 600
highscore = 0
GAP = 130
SPEED = 4
GRAVITY= 0.1
KEY_JUMP = 5

def reset_pipes():
    # randomly choose where the gap should appear
    pipe_gap_y = random.randint(200, HEIGHT - 200)
    #
    pipe_top.pos = (WIDTH, pipe_gap_y - GAP // 2)
    pipe_bottom.pos = (WIDTH, pipe_gap_y + GAP // 2)

bird = Actor('bird1', (75, 200))
bird.score = 0
bird.speed = 0
bird.dead = False
pipe_top = Actor('top', anchor=('left', 'bottom'))
pipe_bottom = Actor('bottom', anchor=('left', 'top'))
reset_pipes()

def draw():
    screen.blit('background', (0, 0))
    pipe_bottom.draw()
    pipe_top.draw()
    bird.draw()
    screen.draw.text( 'Score:'+str(bird.score), (100,10) , color='white', fontsize=50)
    screen.draw.text( 'Best: '+ str(highscore), (100, HEIGHT -40), color='blue', fontsize=50)

def update_pipes():
    pipe_top.left -= SPEED
    pipe_bottom.left -= SPEED
    if pipe_top.right < 0:
        reset_pipes()
        bird.score = bird.score + 1

def update_bird():
    bird.speed = bird.speed + GRAVITY
    bird.y = bird.y + (bird.speed/2)
    bird.x = 75
    if bird.colliderect(pipe_top) or bird.colliderect(pipe_bottom):
        bird.dead = True
        bird.image = 'birddead'

    if bird.dead == False:
        bird.image = 'bird1'


    if bird.y < 0 or bird.y > 750:
        bird.y = 200
        bird.dead = False
        bird.score = 0
        bird.speed = 0
        reset_pipes()


def update():
    update_pipes()
    update_bird()
    
def on_key_down():
    if not bird.dead:
        bird.speed = - KEY_JUMP

pgzrun.go()