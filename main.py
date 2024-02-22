from movement import *
from cyberbot import *
from tuning import *

# TUNING MODE FOR CYBERBOT

# Values below: 
# Forward Speed for Pin 18
# Forward Speed for Pin 19
# Reverse Speed for Pin 18
# Reverse Speed for Pin 19
# Turn Speed for Pin 18
# Turn Speed for Pin 19
# SPI
# SPD

m = TuningModes(
    64,
    75,
    75,
    75,
    75,
    75,
    #SPI, leave blank for default
    #SPD, leave blank for default
)
