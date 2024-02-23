from movementLibrary import *
from cyberbot import *

m = Movement(4,"mm")
i = Movement(4,"in")

# Movements in mm:

# Distance, Speed
m.forward(5, 1)
# Angle, Direction, Speed
m.turn(90, "right", .5)
# Distance, Speed
m.backward(10, 1)
# Angle, Direction, Speed
m.turn(90, "left", 1)
# Distance, Speed
m.forward(10, 1)
# Angle, Direction, Speed
m.turn(90, "right", 1)
# Distance, Speed
m.forward(10, 1)
# Angle, Direction, Speed
m.turn(90, "left", 1)
# Distance, Speed
m.backward(15, 1)


# Same as above, but in inches
i.forward(5, 1)
i.turn(90, "right", .5)
i.backward(10, 1)
i.turn(90, "left", 1)
i.forward(10, 1)
i.turn(90, "right", 1)
i.forward(10, 1)
i.turn(90, "left", 1)
i.backward(15, 1)
