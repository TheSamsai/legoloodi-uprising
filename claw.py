#!/usr/bin/env python3
from ev3dev2.motor import MediumMotor, OUTPUT_B


def open():

    motor = MediumMotor('outB')

    motor.on_for_degrees(100,800, block=False)



def close():

    motor = MediumMotor('outB')

    motor.on_for_degrees(-100,800, block=False)