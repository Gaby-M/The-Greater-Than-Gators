import pygame, sys, pickle
from pygame.locals import QUIT
from pygame.locals import *
from math_generator import *

question_generator = MathGenerator(3)
problem = question_generator.math_problem_generator(3)
print(problem)
RESTART_COLOR = (240, 178, 113)
pygame.init()
clock = pygame.time.Clock()
stop = False
fps = 60

screen_width = 1000
screen_height = 1000
DISPLAYSURF = pygame.display.set_mode((screen_width, screen_height), HWSURFACE|DOUBLEBUF|RESIZABLE)
                              
pygame.display.set_caption('Greater than Gator Game')
bgIMG = pygame.image.load('Sprites/red_brick.png')
DISPLAYSURF.blit(pygame.transform.scale(bgIMG,(1000,1000)),(0,0))

tile_size = 50

#BUTTON CLASS
class Button: 
  button_font = pygame.font. Font(None, 100)
  def __init__(self, x_position, y_position, x_size, y_size, text): 
    self.x_position = x_position
    self.y_position = y_position
    self.x_size = x_size
    self.y_size = y_size
    self.clicked = False
    self.text = text
    self.restart_rect = 0
   
  def draw_button(self): 
    restart_text = Button.button_font.render(self.text, 0, (255,255,255))
    restart_surface = pygame.Surface((self.x_size, self.y_size))
    restart_surface.fill(RESTART_COLOR),
    restart_surface.blit(restart_text, (screen_width // 4 - 130, screen_height//4))
    self.restart_rect = restart_surface.get_rect(center=(screen_width // 2,screen_height // 2))
    DISPLAYSURF.blit(restart_surface,self.restart_rect)
    
#PLAYER CLASS
class Player():
  def __init__(self,x,y,image):
    img = pygame.image.load(image)
    self.image = pygame.transform.scale(img,(110,110))
    
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.width = self.image.get_width()
    self.height = self.image.get_height()
    self.vel_y = 0
    self.jump = False
    self.in_air = True
 
    
  def update(self):
    dx = 0
    dy = 0
    
    #KEYBOARD FUNCTION
    key = pygame.key.get_pressed()
    
    if key[pygame.K_w] and self.jump == False:
      self.vel_y = -15
      self.jump = True
    if key[pygame.K_w] == False and self.in_air == False:
      self.jump = False
    if key[pygame.K_a]:
      dx -= 5
    if key[pygame.K_d]:
      dx += 5

    self.vel_y += 1
    if self.vel_y > 10:
      self.vel_y = 10
    dy += self.vel_y
    
    #CHECK FOR COLLISION
    self.in_air = True
    for tile in world.tile_list:
      
      if tile[1].colliderect(self.rect.x + dx,self.rect.y,self.width , self.height):
        dx = 0
        
      if tile[1].colliderect(self.rect.x,self.rect.y + dy, self.width,self.height):

        if self.vel_y < 0:
          dy = tile[1].bottom - self.rect.top
          
        elif self.vel_y >= 0:
          dy = tile[1].top - self.rect.bottom 
          self.vel_y = 0
          self.in_air = False
     
    #COLLISION WITH PLAYER AND ENEMY
      if pygame.sprite.spritecollide(self,dog_g,False):
        popup = Button(screen_width // 2, screen_height // 2, 500, 500, problem)
        popup.draw_button()
        
    #END COLLISION      
    self.rect.x += dx
    self.rect.y += dy
          
    if self.rect.bottom > screen_height:
      self.rect.bottom = screen_height
      dy = 0
      
    DISPLAYSURF.blit(self.image,self.rect)
    
#WORLD CLASS
class World():
	def __init__(self, data):
		self.tile_list = []

		#LOAD IMAGES
		dirt_img = pygame.image.load('Sprites/brickWall.png')
		grass_img = pygame.image.load('Sprites/grass.png')

		row_count = 0
    
		for row in data:
      
			col_count = 0
			for tile in row:
        
				if tile == 1:
					img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
          
				if tile == 2:
					img = pygame.transform.scale(grass_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
          
				if tile == 3:
					dog = Boss(col_count + tile_size + 300, row_count * tile_size + 40, "Sprites/enemy.png")
					dog_g.add(dog)
          
				col_count += 1
			row_count += 1
      
	def draw(self):
  		DISPLAYSURF.blit(pygame.transform.scale(bgIMG,(1000,1000)),(0,0))
  		for tile in self.tile_list:
    			DISPLAYSURF.blit(tile[0], tile[1])
        
#BOSS CLASS
class Boss(pygame.sprite.Sprite):
  def __init__(self,x,y,image):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(image)
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.move_direction = 1
    self.move_counter = 0
    
#MOVEMENT
  def update(self):
    self.rect.x += self.move_direction
    self.move_counter += 1
    if abs(self.move_counter) > 50:
      self.move_direction *= -1
      self.move_counter *= -1

#BLOCKS LOCATION
world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1], 
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 1], 
[1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1], 
[1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 2, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 1, 1], 
[1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1], 
[1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1], 
[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

player = Player(50, screen_height - 140, "Sprites/gator.png")

dog_g = pygame.sprite.Group()
#trying to load in world data
world = World(world_data)
#making the buttons


while True:

  clock.tick(fps)
  
  world.draw()
  
  player.update()

  dog_g.update()  
  dog_g.draw(DISPLAYSURF)
  
  #END GAME
  for event in pygame.event.get():
    if event.type == QUIT:
        pygame.quit()
        sys.exit()

  pygame.display.update()
