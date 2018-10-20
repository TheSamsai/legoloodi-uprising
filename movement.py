#!/usr/bin/env python3
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from ev3dev2.motor import MoveTank

import time

tank_drive = MoveTank("outA", "outD")
gyro = GyroSensor()

def go_forward_slow():
    tank_drive.on_for_rotations(20, 20, 0.5)

def left_turn(angle):
    start_degrees = gyro.angle
    desired_degrees = start_degrees - angle

    while gyro.angle > desired_degrees:
        tank_drive.on_for_rotations(-50, 50, 1, block = False)
    
    tank_drive.off()

def right_turn(angle):
    start_degrees = gyro.angle
    desired_degrees = start_degrees + angle

    while gyro.angle < desired_degrees:
        tank_drive.on_for_rotations(50, -50, 1, block = False)
    
    tank_drive.off()


