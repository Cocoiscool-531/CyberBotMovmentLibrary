# microbit-module: Movement Library By Cohen George@2.0
from cyberbot import *
import log,math

speeds = []

secondsPerDegree = 0.005

distancePerDegree = 0
secondsPerDistance = 0
distancePerSecond = 0

inPerDegree = 0.00386514844
secondsPerIn = .19047619047
inPerSecond = 5.25

mmPerDegree = inPerDegree * 25.4
mmPerSecond =  inPerSecond * 25.4
secondsPerMM = 1/mmPerSecond

botNum = 1

def changeUnit(unit):
    global distancePerDegree
    global distancePerSecond
    global secondsPerDistance
    if(unit == "mm"):
        distancePerDegree = mmPerDegree
        secondsPerDistance = secondsPerMM
        distancePerSecond = mmPerSecond
    elif unit == "in":
        distancePerDegree = inPerDegree
        secondsPerDistance = secondsPerIn
        distancePerSecond = inPerSecond
    
def accessBotNum():
    return botNum

def modifyBotNum(s):
    global botNum
    botNum = s

class Bot1:
    pin18Speed = 67
    pin19Speed = 75

class Bot2:
    # No Sticky
    pin18Speed = 75
    pin19Speed = 75

class Bot3:
    pin18Speed = 74.25
    pin19Speed = 75

class Bot4:
    pin18Speed = 67
    pin19Speed = 75

class Bot5:
    pin18Speed = 75
    pin19Speed = 75

class Bot6:
    pin18Speed = 70.2
    pin19Speed = 75

class Bot7:
    # No Sticky
    pin18Speed = 75
    pin19Speed = 75

class Bot8:
    pin18Speed = 72.115
    pin19Speed = 75

class Bot9:
    pin18Speed = 67
    pin19Speed = 75

class Bot10:
    pin18Speed = 65
    pin19Speed = 75

class Bot11:
    # Out Of Service: Values Untested, Unchanged
    pin18Speed = 75
    pin19Speed = 75

class Bot12:
    # Out Of Service: Values Untested, Unchanged
    pin18Speed = 75
    pin19Speed = 75

def moveVals():
    botNum = accessBotNum()
    botNumber = str(botNum)
    global speeds
    for i in range(18, 19):
        toRun = ("speeds.append(Bot" + botNumber + ".pin" + str(i) + "Speed)")
        eval(toRun)
    return speeds

def spdVal():
    return secondsPerDistance
    
def dpdVal():
    return distancePerDegree

def distanceFormula(distance):
    return ((distance*spdVal())-spdVal())*1000

def degreeFormula(degrees):
    return (degrees*secondsPerDegree-secondsPerDegree*1000)

def degreesToDistance(degrees):
    return degrees * dpdVal()

class Movement:
    
    def __init__(
        self,
        botNum,
        unit
    ):
        modifyBotNum(botNum)
        changeUnit(unit)
    
    def forward(self, distance, speed):
        distance /= speed
        log.add({"Forward Active": distance})
        timer = 0
        bot(18).servo_speed(moveVals()[0] * speed)
        bot(19).servo_speed(-moveVals()[1] * speed)
        while timer < distanceFormula(distance):
            sleep(1)
            timer += 1
            if math.fmod(timer, 100 * speed) == 0:
                bot(20).write_digital(0)
            elif math.fmod(timer, 50 * speed) == 0:
                bot(20).write_digital(1)
        bot(20).write_digital(0)
        bot(21).write_digital(0)
        bot(18).servo_speed(None)
        bot(19).servo_speed(None)
    
    def backward(self, distance, speed):
        distance /= speed
        log.add({"Backward Active": distance})
        timer = 0
        bot(18).servo_speed(-moveVals()[0] * speed)
        bot(19).servo_speed(moveVals()[1] * speed)
        while timer < distanceFormula(distance):
            sleep(1)
            timer += 1
            if math.fmod(timer, 100 * speed) == 0:
                bot(20).write_digital(0)
            elif math.fmod(timer, 50 * speed) == 0:
                bot(20).write_digital(1)
        bot(20).write_digital(0)
        bot(21).write_digital(0)
        bot(18).servo_speed(None)
        bot(19).servo_speed(None)
    
    def turn(self, degrees, direction, speed):
        degrees /= speed
        timer = 0
        if direction is "Right" or direction is "right":
            log.add({"Right Turn Active": degrees})
            bot(18).servo_speed(moveVals()[0] * speed)
            bot(19).servo_speed(moveVals()[1] * speed)
            while timer < degreeFormula(degrees):
                sleep(1)
                timer += 1
                if math.fmod(timer, 100 * speed) == 0:
                    bot(20).write_digital(0)
                    bot(21).write_digital(0)
                elif math.fmod(timer, 50 * speed) == 0:
                    bot(20).write_digital(1)
                    bot(21).write_digital(1)
        if direction is "Left" or direction is "left":
            bot(18).servo_speed(-moveVals()[0] * speed)
            bot(19).servo_speed(-moveVals()[1] * speed)
            while timer < degreeFormula(degrees):
                sleep(1)
                timer += 1
                if math.fmod(timer, 100 * speed) == 0:
                    bot(20).write_digital(0)
                    bot(21).write_digital(1)
                elif math.fmod(timer, 50 * speed) == 0:
                    bot(20).write_digital(1)
                    bot(21).write_digital(0)
        bot(20).write_digital(0)
        bot(21).write_digital(0)
        bot(18).servo_speed(None)
        bot(19).servo_speed(None)
