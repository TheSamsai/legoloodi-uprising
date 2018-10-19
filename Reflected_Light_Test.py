#!/usr/bin/env python3
import os
os.system('setfont Lat15-TerminusBold14')
from ev3dev2.button import Button
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.motor import MoveTank

import time

sensors = ColorSensor()
tank_drive = MoveTank("outA", "outD")

while True:
    inten = sensors.reflected_light_intensity
    
    print(inten)

    if inten < 10:
        tank_drive.on_for_rotations(20, 20, 0.5)
    else:
        tank_drive.off()
        tank_drive.on_for_rotations(100, -100, 0.8)
        tank_drive_on_for_rotations(100, 100, 200)
