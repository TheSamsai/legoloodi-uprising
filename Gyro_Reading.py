#!/usr/bin/env python3
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.button import Button

button = Button()
gyro = GyroSensor()
while True:

    if button.any():
        exit(1)

    print (gyro.rate_and_angle)

    



    

