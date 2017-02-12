#Step 1: create a square
#Step 2: replicate the square at an angle divisble by 360 degrees
import turtle

def draw_square(first,second,third):
    first.color("yellow")
    second.color("red")
    third.color("green")
    for e in range(4):
        first.left(90)
        second.left(90)
        first.forward(200)
        second.forward(100)
    third.circle(40)    

def main():
    window=turtle.Screen()
    window.bgcolor("blue")

    first=turtle.Turtle()
    second=turtle.Turtle()
    third=turtle.Turtle()
    first.speed(000)
    second.speed(000)
    third.speed(000)
    for e in range(300):
        draw_square(first,second,third)
        first.left(5)
        second.left(5)
        third.left(5)

    
    window.exitonclick()      
main()
    

