import turtle

turtle.bgcolor('black')
t=turtle.Turtle()

t.shape('turtle')
t.color('red')
t.circle(150)
t.penup() #podniesienie pisaka do następnego miejsca, zeby nie rysowac z tego miejsca do następnego
t.goto(-300,0)
t.pendown()
t.color('white')
t.write("Hi there, hello", font=("Arial",25,"bold"))
t.hideturtle()

turtle.exitonclick()
