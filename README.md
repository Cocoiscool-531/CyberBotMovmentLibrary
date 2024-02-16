**Instalation**

Download the most recent version from the releases tab on the right, press open on [Micro Python](https://python.microbit.org/v/3/) and press the "movementLibrary.py" file.

**Usage**

In your main file, first import the library:

from movementLibrary import *

Then create a new object

m = Movement()

Next add the parameters

The following are such parameters:

m = Movement(
  pin18ForwardSpeed,
  pin19ForwardSpeed,
  pin18ReverseSpeed,
  pin19ReverseSpeed,
  pin18TurnSpeed,
  pin19TurnSpeed
)
