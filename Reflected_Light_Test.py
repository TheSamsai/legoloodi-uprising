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
    print(sensors.reflected_light_intensity)

    if sensors.reflected_light_intensity < 30:
        tank_drive.on_for_rotations(50, 50, 1)
    else:
        tank_drive.off()
        tank_drive.on_for_rotations(100, -100, 0.8)
        tank_drive.on_for_rotations(50, 50, 200)
        time.sleep(60)
