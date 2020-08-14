import turtle

# I didn't use a function since...
# a) When I put my code under whole function it didn't work 
# (as in, I create a function and simply copy-paste my code into it, my code didn't work)

# b) I tried to call a function and that didn't work either.

t = turtle.Turtle()
t.speed(10)

limit = input("Input a limit: ")

count = 0

while count < int(limit):
    t.forward(250)
    t.left(100 + count/100)
    count += 1