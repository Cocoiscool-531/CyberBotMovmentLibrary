from movement import *

m = Movement(
    64,
    75,
    75,
    75,
    75,
    75,
)

#Distance Inches, speed(0-1)
m.forward(4, 0.5)
#Degrees, Dirrection ("Left" or "Right"), speed(0-1)
m.turn(90, "Left", 0.5)
#Distance Inches, speed(0-1)
m.backward(9, 1)
#Degrees, Dirrection ("Left" or "Right"), speed(0-1)
m.turn(180, "Right", 0.5)
