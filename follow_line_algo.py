#!/usr/bin/env python3
import os
os.system('setfont Lat15-TerminusBold14')
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.motor import MoveTank

import time

while True:
    follow_line(ColorSensor.COLOR_BLACK)

def go_forward_slow(drive):
    drive.on_for_rotations(20, 20, 0.5)

def left_turn_45(drive):
    drive.on_for_rotations(-50, 50, 1)

def right_turn_45(drive):
    drive.on_for_rotations(50, -50, 1)

def follow_line(line_color):
    sensor = ColorSensor()
    tank_drive = MoveTank("outA", "outD")
    
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



