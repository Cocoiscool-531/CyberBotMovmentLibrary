**NOTE: BETA BRANCH MAY BE UNSTABLE, USE AT YOUR OWN RISK**


**Instalation**

Download the most recent version from the releases tab on the right, press open on [Micro Python](https://python.microbit.org/v/3/) and press the "movementLibrary.py" file.

You may also download the hex file to get a full template already set up, open it in the same way.

**Usage**

In your main file, first import the library:

from movementLibrary import *

Then create a new object

m = Movement()

The Movement class takes 2 parameters, the bot number, and the unit. For bot number, input an int between 1 and 12. 
After that put either "in" or "mm" for selecting a unit. An example main.py is shown below.
```python
from movementLibrary import *
from cyberbot import *

m = Movement(4,"in")

m.forward(5, 1)```
