#! Python3
# Mockup of Snake - Made by JN ~1/30/2017

import pygame, random, sys
import pygame.locals

# Todo list
# Add ability to grow snake
# Add collision check with self;
# Make it so food won't appear on snake body or head

class Game():
    HORIZONTAL_SIZE, VERTICAL_SIZE = 300, 300 #Size of screen
    
    def __init__(self):    
        # Initialize screen
        pygame.init()
        self.screen = pygame.display.set_mode((Game.HORIZONTAL_SIZE, Game.VERTICAL_SIZE ))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 20)
        self.score = 0 #Player score
        pygame.display.set_caption('Snake')
        
    def display_update(self):
        # Update screen every frame
        self.screen.fill((0,0,0))
        self.screen.blit(snake.image, snake.position)
        self.screen.blit(food.image, food.position)
        self.text_score = self.font.render('Score is '+ str(self.score), True, (0,255,255)) #Score is updated every frame
        self.screen.blit(self.text_score, (220,0))
        pygame.display.flip()
        
        # For debugging
        # self.timer = font.render('timer is '+str(food.time), True, (0,255,255))
        # self.screen.blit(self.timer, (220,20))
        # pygame.display.flip()

    def caught_food(self):
        # Check if snake caught the food
        if snake.position == food.position:
            self.score +=1
            food.time = 0 # Reset food timer
            food.position = food.random_position()

    def game_over(self):
        # Display game over screen and stop game
        self.screen.fill((100,0,0))
        self.text = self.font.render('Game Over', True, (0,0,0))
        self.screen.blit(self.text, (120,130))
        self.text_finalscore = self.font.render('Your score is ' +str(self.score), True, (0,0,0))
        self.screen.blit(self.text_finalscore, (120,150))
                                                
        pygame.display.flip()

        sys.exit('Died')

class Snake():
    SPEED = 10 #Pixels per frame. Do not change. Change fps if you want to make it easier/harder
    
    def __init__(self):
        self.image = pygame.image.load('sprite2.png')
        self.position =  [0,0] # Starting position
        self.direction = 'right' #Initial direction
        self.head_size = (10,10)  # Size of the sprite of the head
        self.dead = False
 
    def move(self, direction):
        # Move snake Snake.SPEED units per frame
        if self.direction == 'right':
            self.position[0] += Snake.SPEED
        elif self.direction == 'left':
            self.position[0] -= Snake.SPEED
        elif self.direction == 'down':
            self.position[1] += Snake.SPEED
        elif self.direction == 'up':
            self.position[1] -= Snake.SPEED
            
    def is_dead(self):
        # Check if left screen; must also add to check if it hits itself
        if self.position[0] > Game.HORIZONTAL_SIZE - self.head_size[0]:
            self.dead = True
        elif self.position[0] < 0:
            self.dead = True
        elif self.position[1] > Game.VERTICAL_SIZE - self.head_size[1]:
            self.dead = True
        elif self.position[1] < 0:
            self.dead = True
        
        if self.dead:
            game.game_over()


class Food():
    LIFETIME = 250 # How many frames food will last
    
    def __init__(self):    
        self.image = pygame.image.load('food2.png') 
        self.time = 0
        self.position = self.random_position()
    
    def random_position(self):
        return [random.randint(0, Game.HORIZONTAL_SIZE/10-1)*10, random.randint(0,Game.VERTICAL_SIZE/10-1)*10]
        # !! Edit it so it never lands where I am at
    
    def timer(self):
        # Check to see if food has expired
        self.time += 1
        
        if self.time >= Food.LIFETIME:
            self.position = self.random_position()
            self.time = 0
        

game = Game()
snake = Snake()
food = Food()





while True:
    game.clock.tick(10)     # frames per second
    # User Input
    for event in pygame.event.get():
        if not hasattr(event, 'key'): continue
        down = event.type == pygame.locals.KEYDOWN
        if event.key == pygame.locals.K_RIGHT: snake.direction = 'right'
        elif event.key == pygame.locals.K_LEFT: snake.direction = 'left'
        elif event.key ==  pygame.locals.K_UP: snake.direction = 'up'
        elif event.key == pygame.locals.K_DOWN: snake.direction = 'down'
        elif event.key == pygame.locals.K_ESCAPE: sys.exit('hit esc key')
    
    snake.move(snake.direction)
    game.caught_food()
    food.timer()
    
    game.display_update()
    snake.is_dead()

