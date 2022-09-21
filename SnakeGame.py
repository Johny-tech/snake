import pygame
import time 
from random import randint as rd
from pygame.locals import *

SIZE = 40
class Snake:
    def __init__(self,surface):
        self.parent_screen = surface
        self.block = pygame.image.load("block.jpg").convert()
        self.length = 3
        self.x = [SIZE]*self.length
        self.y = [SIZE]*self.length 
        self.direction = "down"

    def move_right(self):
        self.direction = "right"
        
    def move_up(self):
        self.direction="up"

    def move_down(self):
        self.direction = "down"

    def move_left(self):
        self.direction = "left"

    def increaseLength(self):
        self.length+=1
        self.x.append(-1)
        self.y.append(-1)
        print(self.x)
        print(self.y)
        
    def walk(self):
        
        for i in range(self.length-1,0,-1):
            self.x[i]=self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction=="right":
            self.x[0]+=SIZE
        if self.direction=="left":
            self.x[0]-=SIZE
        if self.direction=="up":
            self.y[0]-=SIZE
        if self.direction=="down":
            self.y[0]+=SIZE    

        self.draw()    

    def draw(self):
        self.parent_screen.fill((100,225,125))
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
        pygame.display.flip() 


class Apple:

    def __init__(self,surface):
        self.parent_screen= surface
        self.block = pygame.image.load("apple.jpg").convert()
        self.x = SIZE*3
        self.y = SIZE*3

    def draw(self):
        # self.parent_screen.fill((100,225,125))
        self.parent_screen.blit(self.block,(self.x,self.y))
        pygame.display.flip() 

    def moveToRandomPoint(self):
        self.x = rd(50,950)
        self.y = rd(50,450)





class Game:
    def __init__(self):
        pygame.init()
        # pygame.font.init()
        # self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.surface = pygame.display.set_mode((1000,500))
        self.snake = Snake(self.surface)
        self.snake.draw()
        self.apple = Apple(self.surface)
        # self.apple.draw()


    def collision(self,x1,y1,x2,y2):
        if x1 >= x2 and x1<= x2 + SIZE:
            if y1 >= y2 and y1 <= y2 + SIZE:
                return True
                

        return False 
    

    def play(self):

        if self.collision(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y):
            self.apple.moveToRandomPoint()
            self.snake.increaseLength()
            # for i in range(self.length-1,0,-1):
            #     self.x[i]=self.x[i-1]
            #     self.y[i] = self.y[i-1]
                


        self.snake.walk()
        self.apple.draw()

    def run(self):
            # time.sleep(12)
        running = True

        # self.font.render("text", False, (0,0,0))

        while running:

            
            for event in pygame.event.get():
                
                if event.type == KEYDOWN:
                    if event.key==K_LEFT:
                        self.snake.move_left()

                    if event.key==K_RIGHT:
                        self.snake.move_right()

                    if event.key==K_UP:
                        self.snake.move_up()


                    if event.key==K_DOWN:
                        self.snake.move_down() 

                    if event.key==K_ESCAPE:
                        running=False

                    # if self.collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
                        # print("collision")

                        
                elif event.type==QUIT:
                    running = False

            # self.surface.blit(self.font, (100,0))
            # pygame.display.flip() 
            
            # time.sleep(2)
            # self.snake.walk()
            # self.apple.draw()
            # # self.snake.walk()
            print(self.snake.x)
            print(self.snake.y)
            self.play()
            time.sleep(0.3)


if __name__=="__main__":
    game = Game()
    game.run()
