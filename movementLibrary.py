# microbit-module: movementlibrary@1.0.2
from cyberbot import *
import log

secondsPerInch = 0.21739130434
secondsPerDegree = 0.005


pin18ForwardSpeedFinal = 75
pin19ForwardSpeedFinal = 75
pin18ReverseSpeedFinal = 75
pin19ReverseSpeedFinal = 75
pin18TurnSpeedFinal = 75
pin19TurnSpeedFinal = 75

#Allows chaning global variables

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

class Movement:
    
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
    
    def forward(self, distance, speed):
        log.add({"Forward Active": distance})
        timer = 0
        bot(18).servo_speed(access18F() * speed)
        bot(19).servo_speed(-access19F() * speed)
        while timer < ((((distance*secondsPerInch)-secondsPerInch)*1000)):
            sleep(50)
            bot(20).write_digital(1)
            sleep(50)
            bot(20).write_digital(0)
            timer = timer + 100
        bot(18).servo_speed(None)
        bot(19).servo_speed(None)
    
    def backward(self, distance, speed):
        log.add({"Backward Active": distance})
        timer = 0
        bot(18).servo_speed(-access18R() * speed)
        bot(19).servo_speed(access19R() * speed)
        while timer < ((((distance*secondsPerInch)-secondsPerInch)*1000)):
            sleep(100)
            bot(21).write_digital(1)
            timer = timer + 100
            if timer > (((distance*secondsPerInch)-secondsPerInch)*1000):
                    bot(20).write_digital(0)
                    bot(21).write_digital(0)
                    break
            sleep(100)
            bot(21).write_digital(0)
            timer = timer + 200
        bot(18).servo_speed(None)
        bot(19).servo_speed(None)
    
    def turn(self, degrees, direction, speed):
        timer = 0
        if direction is "Right":
            log.add({"Right Turn Active": degrees})
            bot(18).servo_speed(access18T() * speed)
            bot(19).servo_speed(access19T() * speed)
            while timer < (((degrees*secondsPerDegree)-secondsPerDegree)*1000):
                sleep(10)
                bot(20).write_digital(1)
                bot(21).write_digital(1)
                sleep(10)
                bot(20).write_digital(0)
                bot(21).write_digital(0)
                timer = timer + 20
        if direction is "Left":
            log.add({"Left Turn Active": degrees})
            bot(18).servo_speed(-access18T() * speed)
            bot(19).servo_speed(-access19T() * speed)
            while timer < (((degrees*secondsPerDegree)-secondsPerDegree)*1000):
                sleep(10)
                bot(20).write_digital(1)
                bot(21).write_digital(0)
                sleep(10)
                bot(20).write_digital(0)
                bot(21).write_digital(1)
                timer = timer + 20
                
        log.add({"timer": timer})
        bot(21).write_digital(0)
        bot(18).servo_speed(None)
        bot(19).servo_speed(None)
