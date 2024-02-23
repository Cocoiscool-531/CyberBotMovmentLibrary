# microbit-module: Movement Library By Cohen George@2.0
from cyberbot import *
import log
import math

distancePerDegree = 0
secondsPerDistance = 0
distancePerSecond = 0

inPerDegree = 0.00386514844
secondsPerIn = 0.14267772545
inPerSecond = 7.008802507992127

mmPerDegree = 0.09817477042
secondsPerMM = 0.00561723328
mmPerSecond =  178.023583703

botNum = 1

def changeUnit(unit):
    global distancePerDegree
    global distancePerSecond
    global secondsPerDistance
    if(unit == "mm" or unit == "Mm" or unit == "Mm" or unit == "MM"):
        distancePerDegree = mmPerDegree
        secondsPerDistance = secondsPerMM
        distancePerSecond = mmPerSecond
    elif(unit == "in" or unit == "In" or unit == "IN" or unit == "iN" or unit == "Inches" or unit == "inches" or unit == "INCHES" or unit == "Inch" or unit == "INCH" or unit == "inch"):
        distancePerDegree = inPerDegree
        secondsPerDistance = secondsPerIn
        distancePerSecond = inPerSecond

def accessBotNum():
    return botNum

def modifyBotNum(s):
    global botNum
    botNum = s

class Bot1:
    rpm = 50
    pin18ForwardSpeed = 67
    pin19ForwardSpeed = 75
    pin18ReverseSpeed = 67
    pin19ReverseSpeed = 75
    pin18TurnSpeed = 67
    pin19TurnSpeed = 75

class Bot2:
    # No Sticky
    pin18ForwardSpeed = 75
    pin19ForwardSpeed = 75
    pin18ReverseSpeed = 75
    pin19ReverseSpeed = 75
    pin18TurnSpeed = 75
    pin19TurnSpeed = 75

class Bot3:
    pin18ForwardSpeed = 74.25
    pin19ForwardSpeed = 75
    pin18ReverseSpeed = 74.25
    pin19ReverseSpeed = 75
    pin18TurnSpeed = 74.25
    pin19TurnSpeed = 75

class Bot4:
    pin18ForwardSpeed = 67
    pin19ForwardSpeed = 75
    pin18ReverseSpeed = 67
    pin19ReverseSpeed = 75
    pin18TurnSpeed = 67
    pin19TurnSpeed = 75

class Bot5:
    pin18ForwardSpeed = 75
    pin19ForwardSpeed = 75
    pin18ReverseSpeed = 75
    pin19ReverseSpeed = 75
    pin18TurnSpeed = 75
    pin19TurnSpeed = 75

class Bot6:
    pin18ForwardSpeed = 70.2
    pin19ForwardSpeed = 75
    pin18ReverseSpeed = 70.2
    pin19ReverseSpeed = 75
    pin18TurnSpeed = 70.2
    pin19TurnSpeed = 75

class Bot7:
    # No Sticky
    pin18ForwardSpeed = 75
    pin19ForwardSpeed = 75
    pin18ReverseSpeed = 75
    pin19ReverseSpeed = 75
    pin18TurnSpeed = 75
    pin19TurnSpeed = 75

class Bot8:
    pin18ForwardSpeed = 72.115
    pin19ForwardSpeed = 75
    pin18ReverseSpeed = 72.115
    pin19ReverseSpeed = 75
    pin18TurnSpeed = 72.115
    pin19TurnSpeed = 75

class Bot9:
    pin18ForwardSpeed = 67
    pin19ForwardSpeed = 75
    pin18ReverseSpeed = 67
    pin19ReverseSpeed = 75
    pin18TurnSpeed = 67
    pin19TurnSpeed = 75

class Bot10:
    pin18ForwardSpeed = 65
    pin19ForwardSpeed = 75
    pin18ReverseSpeed = 65
    pin19ReverseSpeed = 75
    pin18TurnSpeed = 65
    pin19TurnSpeed = 75

class Bot11:
    # Out Of Service: Values Untested, Unchanged
    pin18ForwardSpeed = 75
    pin19ForwardSpeed = 75
    pin18ReverseSpeed = 75
    pin19ReverseSpeed = 75
    pin18TurnSpeed = 75
    pin19TurnSpeed = 75

class Bot12:
    # Out Of Service: Values Untested, Unchanged
    pin18ForwardSpeed = 75
    pin19ForwardSpeed = 75
    pin18ReverseSpeed = 75
    pin19ReverseSpeed = 75
    pin18TurnSpeed = 75
    pin19TurnSpeed = 75

def forwardVals():
    botNum = accessBotNum()
    botNumber = str(botNum)
    speeds = []
    for i in range(18, 19):
        toRun = ("speeds.append(Bot" + botNumber + ".pin" + str(i) + "ForwardSpeed)")
        eval(toRun)
    return speeds
        
def reverseVals():
    global botNum
    botNumber = str(botNum)
    speeds = []
    for i in range(18, 19):
        toRun = ("speeds.append(Bot" + botNumber +".pin" + str(i) + "ReverseSpeed)")
        eval(toRun)
    return speeds
    
def turnVals():
    global botNum
    botNumber = str(botNum)
    speeds = []
    for i in range(18, 19):
        toRun = ("speeds.append(Bot" + botNumber +".pin" + str(i) + "TurnSpeed)")
        eval(toRun)
    return speeds

def spdVal():
    return secondsPerDistance
    
def dpdVal():
    return distancePerDegree

def distanceFormula(distance):
    return ((distance*spdVal())-spdVal())*1000

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
        bot(18).servo_speed(forwardVals()[0] * speed)
        bot(19).servo_speed(-forwardVals()[1] * speed)
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
        bot(18).servo_speed(-reverseVals()[0] * speed)
        bot(19).servo_speed(reverseVals()[1] * speed)
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
        distance = degreesToDistance(degrees)
        distance /= speed
        timer = 0
        if direction is "Right":
            log.add({"Right Turn Active": degrees})
            bot(18).servo_speed(turnVals()[0] * speed)
            bot(19).servo_speed(turnVals()[1] * speed)
            while timer < distanceFormula(distance):
                sleep(1)
                timer += 1
                if math.fmod(timer, 100 * speed) == 0:
                    bot(20).write_digital(0)
                    bot(21).write_digital(0)
                elif math.fmod(timer, 50 * speed) == 0:
                    bot(20).write_digital(1)
                    bot(21).write_digital(1)
        if direction is "Left":
            bot(18).servo_speed(-turnVals()[0] * speed)
            bot(19).servo_speed(-turnVals()[1] * speed)
            while timer < distanceFormula(distance):
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
