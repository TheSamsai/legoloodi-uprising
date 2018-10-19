#!/usr/bin/env python3
import os
os.system('setfont Lat15-TerminusBold14')
from ev3dev2.sensor.lego import ColorSensor
from ColorSensor import *
from ev3dev2.motor import MoveTank

import time

while True:
    follow_line(COLOR_BLACK)

def follow_line(line_color):
    sensor = ColorSensor()
    tank_drive = MoveTank("outA", "outD")
    
    color = sensor.color()

    if color == line_color:
        tank_drive.on_for_rotations(20, 20, 0.5)
    else:
        while color != line_color:
            tank_drive.off()
            tank_drive.on_for_rotations(50, -50, 1)
            color = sensor.color()

            if color != line_color:
                tank_drive.on_for_rotations(-50, 50, 1)
                tank_drive.on_for_rotations(-50, 50, 1)
                
                color = sensor.color()

                if color != line_color:
                    tank_drive.on_for_rotations(-50, 50, 1)



