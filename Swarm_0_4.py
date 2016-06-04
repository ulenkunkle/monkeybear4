import pygame
import random
import time
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
 
 
class Block(pygame.sprite.Sprite):
    """
    This class represents the ball
    It derives from the "Sprite" class in Pygame
    """
 
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super(Block,self).__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
 
        # Instance variables that control the edges of where we bounce
        self.left_boundary = 0
        self.right_boundary = 0
        self.top_boundary = 0
        self.bottom_boundary = 0
 
        # Instance variables for our current speed and direction
        self.change_x = 0
        self.change_y = 0
 
    def update(self):
        """ Called each frame. """
        seek_x = 0
        seek_y=0
        pos = pygame.mouse.get_pos()
        r_rangex = random.randrange(-1, 1)
        r_rangey = random.randrange(-1, 1)
        # seek_x =  ((pos[0]*1000)/self.rect.x+1)
        # seek_y =  (pos[1]/(self.rect.y+10))
        if int(pos[0] - self.rect.x) <200:
			if pos[0] <self.rect.x:
				 seek_x = -1
			if pos[1] < self.rect.y:
				 seek_y = -1		
			if pos[0] >self.rect.x:
				 seek_x = 1
			if pos[1] > self.rect.y:
				 seek_y = 1	 
        if int(pos[0] - self.rect.x) <50:
            if pos[0] <self.rect.x:			 
				 seek_x = -2
            if pos[1] <self.rect.y:			 
				 seek_y = -2		 
            if pos[0] >self.rect.x:
				 seek_x = 4
            if pos[1] > self.rect.y:
				 seek_y = 4	 
				 
        if int(pos[0] - self.rect.x) >200: 
			seek_x = r_rangex
			seek_y = r_rangey
			 
        # self.rect.x +=  (r_rangex) +  seek_x
        # self.rect.y +=  (r_rangey )+ seek_y
        self.rect.x +=  seek_x + self.change_x
        self.rect.y +=  seek_y + self.change_y
       # print seek_x,seek_y
        if self.rect.right >= self.right_boundary or self.rect.left <= self.left_boundary:
            self.change_x *= -1
 
        if self.rect.bottom >= self.bottom_boundary or self.rect.top <= self.top_boundary:
            self.change_y *= -1
 
class Player(Block):
    """ The player class derives from Block, but overrides the 'update'
    functionality with new a movement function that will move the block
    with the mouse. """
    def update(self):
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()
 
        # Fetch the x and y out of the list,
        # just like we'd fetch letters out of a string.
        # Set the player object to the mouse location
        self.rect.x = pos[0]
        self.rect.y = pos[1]
 
class Bullet(pygame.sprite.Sprite):
   """ This class represents the bullet . """
   def __init__(self):
       # Call the parent class (Sprite) constructor
       super(Bullet,self).__init__()

       self.image = pygame.Surface([4, 10])
       self.image.fill(BLACK)

       self.rect = self.image.get_rect()

   def update(self):
       """ Move the bullet. """
       self.rect.y -= 3

class splashscreen():


    pygame.init()
    font2 = pygame.font.Font(None,84)
    font3 = pygame.font.Font(None,64)
    screen_width = 1300
    screen_height =700
    screen = pygame.display.set_mode([screen_width, screen_height])
    screen.fill(WHITE)
    scoreprint = "Play swarm ver.0.4: "
    text = font2.render(scoreprint, 1, BLACK)
    textpos = (100,100)
    screen.blit(text,textpos)
    scoreprint = "you are being chased by super nanobots,,,"
    sp2 = "kill them with your crapware rocket launcher"
    text2 = font3.render(sp2, 1, BLACK)
    text = font3.render(scoreprint, 1, BLACK)
    textpos = (100,200)
    screen.blit(text, textpos)
    textpos = (100,250)
    screen.blit(text2,textpos)
#event = pygame.event.wait()
    pygame.display.flip()
done = False		
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
	        done = True
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 1300
screen_height =700
screen = pygame.display.set_mode([screen_width, screen_height])
 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()
 
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
bullet_list = pygame.sprite.Group()
 
for i in range(250):
    # This represents a block
    block = Block(BLACK, 10, 7)
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width-900)
    block.rect.y = random.randrange(screen_height-500)
 
    block.change_x = random.randrange(-3, 4)
    block.change_y = random.randrange(-3, 4)
    block.left_boundary = 0
    block.top_boundary = 0
    block.right_boundary = screen_width
    block.bottom_boundary = screen_height
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
 
# Create a red player block
player = Player(RED, 20, 15)
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
font = pygame.font.Font(None, 24)
font2 = pygame.font.Font(None,84)
b_score = 0
score = 0
B_score = 0
# -------- Main Program Loop -----------


splashscreen()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Fire a bullet if the user clicks the mouse button
            bullet = Bullet()
            # Set the bullet so it is where the player is
            bullet.rect.x = player.rect.x
            bullet.rect.y = player.rect.y
            # Add the bullet to the lists
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
    # Clear the screen
    screen.fill(WHITE)
 
    # Calls update() method on every sprite in the list
    all_sprites_list.update()
    for bullet in bullet_list:
 
        # See if it hit a block
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
 
        # For each block hit, remove the bullet and add to the score
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            B_score += 1
            print('bullet score: ' +str(B_score))
            
            #pygame.display.flip()
        # Remove the bullet if it flies up off the screen
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
 
    # Check the list of collisions.
    for block in blocks_hit_list:
        score += 1
        #print(score)
        #print time.clock()
    scoreprint = "Player 1 (all humans): "+str(B_score) + "   vs:"
    text = font.render(scoreprint, 1, RED)
    textpos = (10,00)
    screen.blit(text, textpos)	
    scoreprint = "Player 2 (all bots + machines): "+str(score)
    text = font.render(scoreprint, 1, BLACK)
    textpos = (250, 0)
    screen.blit(text, textpos)
    scoreprint = "(Machine Clock): "+str(time.clock())
    text = font.render(scoreprint, 1, BLACK)
    textpos = (650, 0)
    screen.blit(text, textpos)
    # Draw all the spites
    all_sprites_list.draw(screen)
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
pygame.quit()