#!/usr/bin/env python3
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from ev3dev2.motor import MoveTank

import time

tank_drive = MoveTank("outA", "outD")
gyro = GyroSensor()

def go_forward_slow():
    drive.on_for_rotations(20, 20, 0.5)

def left_turn(angle):
    start_degrees = gyro.angle
    desired_degrees = start_degrees - angle

    while gyro.angle > desired_degrees:
        drive.on_for_rotations(-50, 50, 1, block = False)
    
    drive.off()

def left_turn(angle):
    start_degrees = gyro.angle
    desired_degrees = start_degrees + angle

    while gyro.angle < desired_degrees:
        drive.on_for_rotations(50, -50, 1, block = False)
    
    drive.off()

def follow_line(line_color):
    sensor = ColorSensor()
    
    color = sensor.color

    if color == line_color:
        go_forward_slow(tank_drive)
    else:
        while color != line_color:
            tank_drive.off()
            left_turn_45(tank_drive)

            color = sensor.color

            if color != line_color:
                right_turn_45(tank_drive)
                right_turn_45(tank_drive)
                
                color = sensor.color

                if color != line_color:
                    right_turn_45(tank_drive)


