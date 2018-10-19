#!/usr/bin/env python3
import os
os.system('setfont Lat15-TerminusBold14')
from ev3dev2.button import Button
from ev3dev2.sensor.lego import ColorSensor

button = Button()
sensors = ColorSensor()
bool = True

while bool: 
    
    print(sensors.reflected_light_intensity)

    if button.any():
        exit

  