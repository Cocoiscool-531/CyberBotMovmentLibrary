# microbit-module: movementlibrary@2.0
from cyberbot import *
import log
import math

botNum = 1

def accessBotNum():
    return botNum

def modifyBotNum(s):
    global botNum
    botNum = s

class Bot1:
    secondsPerInch = 0.21739130434
    secondsPerDegree = 0.005
    pin18ForwardSpeed = 67
    pin19ForwardSpeed = 75
    pin18ReverseSpeed = 67
    pin19ReverseSpeed = 75
    pin18TurnSpeed = 67
    pin19TurnSpeed = 75

class Bot2:
    # No Sticky
    secondsPerInch = 0.21739130434
    secondsPerDegree = 0.005
    pin18ForwardSpeed = 75
    pin19ForwardSpeed = 75
    pin18ReverseSpeed = 75
    pin19ReverseSpeed = 75
    pin18TurnSpeed = 75
    pin19TurnSpeed = 75

class Bot3:
    secondsPerInch = 0.21739130434
    secondsPerDegree = 0.005
    pin18ForwardSpeed = 74.25
    pin19ForwardSpeed = 75
    pin18ReverseSpeed = 74.25
    pin19ReverseSpeed = 75
    pin18TurnSpeed = 74.25
    pin19TurnSpeed = 75

class Bot4:
    secondsPerInch = 0.21739130434
    secondsPerDegree = 0.005
    pin18ForwardSpeed = 67
    pin19ForwardSpeed = 75
    pin18ReverseSpeed = 67
    pin19ReverseSpeed = 75
    pin18TurnSpeed = 67
    pin19TurnSpeed = 75

class Bot5:
    secondsPerInch = 0.21739130434
    secondsPerDegree = 0.005
    pin18ForwardSpeed = 75
    pin19ForwardSpeed = 75
    pin18ReverseSpeed = 75
    pin19ReverseSpeed = 75
    pin18TurnSpeed = 75
    pin19TurnSpeed = 75

class Bot6:
    secondsPerInch = 0.21739130434
    secondsPerDegree = 0.005
    pin18ForwardSpeed = 70.2
    pin19ForwardSpeed = 75
    pin18ReverseSpeed = 70.2
    pin19ReverseSpeed = 75
    pin18TurnSpeed = 70.2
    pin19TurnSpeed = 75

class Bot7:
    # No Sticky
    secondsPerInch = 0.21739130434
    secondsPerDegree = 0.005
    pin18ForwardSpeed = 75
    pin19ForwardSpeed = 75
    pin18ReverseSpeed = 75
    pin19ReverseSpeed = 75
    pin18TurnSpeed = 75
    pin19TurnSpeed = 75

class Bot8:
    secondsPerInch = 0.21739130434
    secondsPerDegree = 0.005
    pin18ForwardSpeed = 72.115
    pin19ForwardSpeed = 75
    pin18ReverseSpeed = 72.115
    pin19ReverseSpeed = 75
    pin18TurnSpeed = 72.115
    pin19TurnSpeed = 75

class Bot9:
    secondsPerInch = 0.21739130434
    secondsPerDegree = 0.005
    pin18ForwardSpeed = 67
    pin19ForwardSpeed = 75
    pin18ReverseSpeed = 67
    pin19ReverseSpeed = 75
    pin18TurnSpeed = 67
    pin19TurnSpeed = 75

class Bot10:
    secondsPerInch = 0.21739130434
    secondsPerDegree = 0.005
    pin18ForwardSpeed = 65
    pin19ForwardSpeed = 75
    pin18ReverseSpeed = 65
    pin19ReverseSpeed = 75
    pin18TurnSpeed = 65
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
def spiVal():
    global botNum
    botNumber = str(botNum)
    spd= []
    for i in range(18, 19):
        toRun = ("spi.append(Bot" + botNumber +".pin" + str(i) + "secondsPerInch)")
        eval(toRun)
    return spd
def spdVal():
    global botNum
    botNumber = str(botNum)
    spi = []
    for i in range(18, 19):
        toRun = ("spd.append(Bot" + botNumber +".pin" + str(i) + "secondsPerDegree)")
        eval(toRun)
    return spi

def distanceFormula(distance):
    return ((distance*spiVal())-spiVal())*1000

def degreeFormula(degrees):
    return ((degrees*spdVal())-spdVal())*1000

class Movement:
    
    def __init__(
        self,
        botNum
    ):
        modifyBotNum(botNum)
    
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
        degrees /= speed
        timer = 0
        if direction is "Right":
            log.add({"Right Turn Active": degrees})
            bot(18).servo_speed(turnVals()[0] * speed)
            bot(19).servo_speed(turnVals()[1] * speed)
            while timer < degreeFormula(degrees):
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
            while timer < degreeFormula(degrees):
                sleep(1)
                timer += 1
                if math.fmod(timer, 100 * speed) == 0:
                    bot(20).write_digital(0)
                    bot(21).write_digital(1)
                elif math.fmod(timer, 50 * speed) == 0:
                    bot(20).write_digital(1)
                    bot(21).write_digital(0)
        log.add({"timer": timer})
        bot(20).write_digital(0)
        bot(21).write_digital(0)
        bot(18).servo_speed(None)
        bot(19).servo_speed(None)
