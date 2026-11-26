from turtle import Turtle, Screen
import random

window = Screen()
window.setup(width= 1000, height=1000)
window.bgcolor("black")
sam = Turtle()
sam.color("red")
sam.shape("turtle")
sam.speed("fastest")


def circles():
   for x in range(10) :
     sam.left(36)
     for _ in range  (36):
      
        sam.forward(15)
        sam.left(10)
        
   sam.penup()
   sam.goto(300,300)    

    
def squares():
   sam.pendown()
   for x in range (10):
      sam.left(36)
      for _ in range (4):
         sam.forward(70)
         sam.left(90)
   sam.penup()      
   sam.goto(-300,-300)



def triangles():
   sam.pendown()
   for x in range (10):
      sam.left(36)
      for _ in range(3):
         sam.forward(70)
         sam.left(120)




circles()
squares()
triangles()

            
window.exitonclick()    
  

    
    




     