#!/usr/bin/env python3
from ev3dev2.motor import MediumMotor, OUTPUT_B

motor = MediumMotor('outB')

def open():
    motor.off(brake=False)
    motor.on_for_degrees(100,800, brake=False, block=False)



def close():
    motor.on_for_degrees(-100,800, block=False)