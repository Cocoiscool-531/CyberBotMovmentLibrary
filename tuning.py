# microbit-module:Tuning Library For Movement Library - Cohen Georgee@2.0
from movement import *

pin18ForwardSpeedFinal = 75
pin19ForwardSpeedFinal = 75
pin18ReverseSpeedFinal = 75
pin19ReverseSpeedFinal = 75
pin18TurnSpeedFinal = 75
pin19TurnSpeedFinal = 75

def accessSPI():
    return secondsPerInch

def accessSPD():
    return secondsPerDegree

def modifySPI(value):
    global secondsPerInch
    secondsPerInch = value

def modifySPD(value):
    global secondsPerDegree
    secondsPerDegree = value

def access18F():
    return pin18ForwardSpeedFinal
    
def access19F():
    return pin19ForwardSpeedFinal
    
def access18R():
    return pin18ReverseSpeedFinal
    
def access19R():
    return pin19ReverseSpeedFinal
    
def access18T():
    return pin18TurnSpeedFinal
    
def access19T():
    return pin19TurnSpeedFinal
    
def modify18F(value):
    global pin18ForwardSpeedFinal
    pin18ForwardSpeedFinal = value
    
def modify19F(value):
    global pin19ForwardSpeedFinal
    pin19ForwardSpeedFinal = value
    
def modify18R(value):
    global pin18ReverseSpeedFinal
    pin18ReverseSpeedFinal = value
    
def modify19R(value):
    global pin19ReverseSpeedFinal
    pin19ReverseSpeedFinal = value
    
def modify18T(value):
    global pin18TurnSpeedFinal
    pin18TurnSpeedFinal = value
    
def modify19T(value):
    global pin19TurnSpeedFinal 
    pin19TurnSpeedFinal = value


class TuningModes:
    
    def __init__(
        self,
        pin18ForwardSpeed,
        pin19ForwardSpeed,
        pin18ReverseSpeed,
        pin19ReverseSpeed,
        pin18TurnSpeed,
        pin19TurnSpeed,
        SPI=accessSPI(),
        SPD=accessSPD()
    ):
        modify18F(pin18ForwardSpeed)
        modify18R(pin18ReverseSpeed)
        modify18T(pin18TurnSpeed)
        modify19F(pin19ForwardSpeed)
        modify19R(pin19ReverseSpeed)
        modify19T(pin19TurnSpeed)
        if SPI != accessSPI():
            modifySPI(SPI)
        if SPD != accessSPD():
            modifySPD(SPD)


    # Set a marker on the spoke at the top of each wheel, point this up vertically up
    # run this, moves the bot forward for 5 seconds, both wheels should be facing up again
    # If they are not, adjust the first 2 values until they are.
    def forwardSpeedTunerBlind(self):
        bot(18).servo_speed(access18F())
        bot(19).servo_speed(-access19F())
        sleep(5000)
        bot(18).servo_speed(None)
        bot(19).servo_speed(None)

    # Same intructions as above, but reverses. Change the 3rd and 4th values to tune
    def reverseSpeedTunerBlind(self):
        bot(18).servo_speed(access18F())
        bot(19).servo_speed(-access19F())
        sleep(5000)
        bot(18).servo_speed(None)
        bot(19).servo_speed(None)


    # Set a marker on the spoke at the top of each wheel, point this up vertically up
    # run this, turns the bot for 5 seconds, both spokes should be facing in oposite
    # directions. If they are not, adjust values 5 and 6 until it works
    def turnSpeedTunerBlind(self):
        bot(18).servo_speed(access18T())
        bot(19).servo_speed(access19T())
        sleep(5000)
        bot(18).servo_speed(None)
        bot(19).servo_speed(None)


        
    # Runs bot forward for 5 seconds, measure distance traveled in inches 
    # as acurate as possible, then divide the seconds by the distance and
    # make that your SPI when creating the Movement object in main.py
    def spiTuner(self):
        bot(18).servo_speed(access18F())
        bot(19).servo_speed(-access19F())
        sleep(5000)
        bot(18).servo_speed(None)
        bot(19).servo_speed(None)

    # Turns bot right for 5 seconds, measure degrees traveled 
    # as acurate as possible, then divide the seconds by the degrees and
    # make that your SPD when creating the Movement object in main.py
    def spdTuner(self):
        bot(18).servo_speed(access18T())
        bot(19).servo_speed(access19T())
        sleep(5000)
        bot(18).servo_speed(None)
        bot(19).servo_speed(None)


    # Run to verify spi value, input multiple distances and check that it traveled the right distance
    def spiChecker(self, distance):
        timer = 0
        bot(18).servo_speed(access18F())
        bot(19).servo_speed(-access19F())
        while timer < ((((distance*secondsPerInch)-secondsPerInch)*1000)):
            sleep(1)
            timer += 1
            if math.fmod(timer, 50) == 0:
                bot(20).write_digital(1)
            if math.fmod(timer, 100) == 0:
                bot(20).write_digital(0)
        bot(20).write_digital(0)
        bot(21).write_digital(0)
        bot(18).servo_speed(None)
        bot(19).servo_speed(None)


        
    # Run to verify spd value, input multiple degree values and check that it turned the right distance
    def spdChecker(self, degrees):
        timer = 0
        bot(18).servo_speed(access18T())
        bot(19).servo_speed(access19T())
        while timer < (((degrees*secondsPerDegree)-secondsPerDegree)*1000):
            sleep(1)
            timer += 1
            if math.fmod(timer, 50) == 0:
                bot(20).write_digital(1)
                bot(21).write_digital(1)
            if math.fmod(timer, 100) == 0:
                bot(20).write_digital(0)
                bot(21).write_digital(0)
    

    # Bot will move forward 10 inches, if this is not complety correct, change the spi until it is.
    # Bot will output time in ms that it took to preform action.
    def forwardSpeedTunerClosed(self):
        distance = 10
        timer = 0
        bot(18).servo_speed(access18F())
        bot(19).servo_speed(-access19F())
        while timer < ((((distance*secondsPerInch)-secondsPerInch)*1000)):
            sleep(1)
            timer += 1
            if math.fmod(timer, 50) == 0:
                bot(20).write_digital(1)
            if math.fmod(timer, 100) == 0:
                bot(20).write_digital(0)
        bot(20).write_digital(0)
        bot(21).write_digital(0)
        bot(18).servo_speed(None)
        bot(19).servo_speed(None)
        display.scroll(timer)
                        
                        
    # Bot should move 90 degrees exactly, if it doesn't, adjust spd until it does.
    # Bot will output time in ms that it took to preform action.
    def turnSpeedTunerClosed(self):
        degrees = 90
        timer = 0
        bot(18).servo_speed(access18T())
        bot(19).servo_speed(access19T())
        while timer < (((degrees*secondsPerDegree)-secondsPerDegree)*1000):
            sleep(1)
            timer += 1
            if math.fmod(timer, 50) == 0:
                bot(20).write_digital(1)
                bot(21).write_digital(1)
            if math.fmod(timer, 100) == 0:
                bot(20).write_digital(0)
                bot(21).write_digital(0)
        display.scroll(timer)
    
        
