# as a basic set up the images directory msut be cerated in the main folder. It is the standard directory that
# Pygame Zero will look in to find your images.
# sounds/ is the standard directory that Pygame Zero will look in to find your sound files.



# Write your code here :-)
alien = Actor('alien')

# the initial position of the alien
alien.topright = 0, 10

# WIDTH and HEIGHT control the width and height of your window
TITLE = "My First py game zero program"
WIDTH = 712
HEIGHT = 508


# The screen.fill() method call is filling the screen with a solid colour, specified as a (red, green, blue) colour tuple.
#(128, 0, 0) will be a medium-dark red. Try changing these values with numbers between 0 and 255 and see
# what colors you can create.

def draw():
    screen.fill((120, 120, 0))
    # The alien.draw() method draws the sprite to the screen at its current position
    alien.draw()




# Pygame Zero will call your update() function once every frame.
def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()
    else:
        print("you missed me!")

def set_alien_hurt():
    print("Eek!")
    sounds.eep.play()
    alien.image = 'alien_hurt'
    clock.schedule_unique(set_alien_normal, 1.0)

def set_alien_normal():
    alien.image = 'alien'