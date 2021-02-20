# Color Game
import pygame, random, time, sys

# User-defined functions
def main():
   # initialize all pygame modules 
   pygame.init()
   # create a pygame display window
   pygame.display.set_mode((500, 400))
   # set the title of the display window
   pygame.display.set_caption('Color Game')   
   # get the display surface
   w_surface = pygame.display.get_surface() 
   # create a game object
   game = Game(w_surface)
   # start the main game loop by calling the play method on the game object
   game.play()  
   # quit pygame and clean up the pygame window
   pygame.quit() 
   
# User-defined classes
class Game:
   # An object in this class represents a complete game.

   def __init__(self, surface):
      # Initialize a Game.
      # - self is the Game to initialize
      # - surface is the display window surface object

      # === objects that are part of every game that we will discuss
      self.surface = surface
      self.bg_color = pygame.Color('black')
      self.FPS = 60
      self.game_Clock = pygame.time.Clock()
      self.close_clicked = False
      self.continue_game = True
      
      # === game specific objects
      self.default_color = 'white'
      self.tile1 = Tile(100, 100, 100, 200,self.default_color, self.surface)
      self.tile2 = Tile(300, 100, 100, 200,self.default_color, self.surface)
      self.colors = ['red', 'blue', 'green', 'yellow']
      self.tile1_clicked = False
      self.tile2_clicked= False
      self.match = 0
      self.mismatch = 0

   def play(self):
      # Play the game until the player presses the close box.
      # - self is the Game that should be continued or not.
      while not self.close_clicked:  # until player clicks close box
         # play frame 
         self.handle_events()
         self.draw()   
         self.white_tiles()
         if self.continue_game == True:
            self.update()
            self.decide_continue()            
         self.game_Clock.tick(self.FPS) # run at most with FPS Frames Per Second 

   def handle_events(self):
      # Handle each user event by changing the game state appropriately.
      # - self is the Game whose events will be handled
      events = pygame.event.get()
      for event in events:
         if event.type == pygame.QUIT:
            self.close_clicked = True
         if event.type == pygame.MOUSEBUTTONDOWN:
            self.handle_mousedown(event)
               
   def handle_mousedown(self, event):
      # - self is the Game whose events will be handled
      # - event is the pygame events   
      if event.button == 1 and self.tile1.collidepoint1(event.pos) and self.tile1_clicked == False:
         self.tile1.set_color(random.choice(self.colors))
         self.tile1_clicked = True
      if event.button == 1 and self.tile2.collidepoint2(event.pos) and self.tile2_clicked == False : 
         self.tile2.set_color(random.choice(self.colors))  
         self.tile2_clicked = True
    
         
   def update(self):
      # updates the match count and resets the tile colors
      # - self is the Game class
      if self.tile1_clicked and self.tile2_clicked == True: 
         time.sleep(1)
         if self.tile1.color == self.tile2.color:
            self.match += 1
         if self.tile1.color != self.tile2.color:
            self.mismatch += 1  
         self.tile1_clicked = False
         self.tile2_clicked = False
         self.tile1.set_color(self.default_color)
         self.tile2.set_color(self.default_color)            

   def white_tiles(self):
      # makes the tiles stay white after 5 mismatches
      # - self is the Game class
      if self.continue_game == False:
         self.tile1.set_color(self.default_color)
         self.tile2.set_color(self.default_color)            
         
   def decide_continue(self):
      # stops continue game loop is there are 5 mismatches
      if self.mismatch > 4:
         self.continue_game = False
         

   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      self.surface.fill(self.bg_color) # clear the display surface first
      # draw all text
      text_string = 'Match: '+ str(self.match)
      text_string2 = 'Mismatch: '+ str(self.mismatch)
      text_fg_color = pygame.Color('white')
      text_bg_color = pygame.Color('black')
      text_font = pygame.font.SysFont('',30)
      text_image = text_font.render(text_string, True, text_fg_color, text_bg_color)
      text_image2 = text_font.render(text_string2, True, text_fg_color, text_bg_color)
      text_top_left_corner = (10, 10)
      text_top_left_corner2 = (360, 10)
      self.surface.blit(text_image, text_top_left_corner)  
      self.surface.blit(text_image2, text_top_left_corner2)  
      self.tile1.draw()
      self.tile2.draw()
      pygame.display.update() # make the updated surface appear on the display
      
class Tile:
   def __init__(self, x, y, width, height, color, surface):
      # - self is the Tile class to initialize 
      # - x is the x-coor int
      # - y is the y-coor int
      # - width is the width int
      # - height is the height int
      # - color is the color string
      # - velocity is the speed list
      # - surface is the display window surface object
      self.rect = pygame.Rect(x, y, width, height) # "geometry" of the rectangle
      self.color = pygame.Color(color)
      self.surface = surface      
   
   def draw(self):
   # draws the tile
   # - self is the Tile class
      pygame.draw.rect(self.surface, self.color, self.rect)
   
   def set_color(self, color):
      # Changes the color of the dot
      # - self is the tile class
      # - color is a string object representing a color name
      self.color = pygame.Color(color)   
   
   def collidepoint1(self, point):
      # return True if the point is inside the Rect; False otherwise
      # - self is the tile
      # - point is a tuple or list representing a point
      if 100 < point[0] < 200 and 100 < point[1] < 300:
         return True

   def collidepoint2(self, point):
      # return True if the point is inside the Rect; False otherwise
      # - self is the tile
      # - point is a tuple or list representing a point
      if 300 < point[0] < 400 and 100 < point[1] < 300:
         return True
         
main()
