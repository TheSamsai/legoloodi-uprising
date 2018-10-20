#!/usr/bin/env python3
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.motor import MoveTank
import movement as movement
import time


LEFT = movement.left_turn
RIGHT = movement.right_turn



def follow_line(line_color1, line_color2 = None):
    last_turn = RIGHT
    sensor = ColorSensor()
    tank_drive = MoveTank("outA", "outD")
    angle = 10
    
    color = sensor.color

    if color == line_color1:
        movement.go_forward_slow()

    if (line_color2 != None):
        if color == line_color2:
            tank_drive.off()
        
    else:

        tank_drive.off()

        while True:

            
            if color != line_color1:
                angle += 10
                angle = min(angle, 90)
                if last_turn == LEFT:
                   RIGHT(angle)
                   last_turn = RIGHT
                else:
                    LEFT(angle)
                   last_turn = LEFT

            else:
                break

           



while True:
    follow_line(ColorSensor.COLOR_WHITE, line_color2=ColorSensor.COLOR_YELLOW)