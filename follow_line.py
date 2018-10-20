#!/usr/bin/env python3
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from ev3dev2.motor import MoveTank
import movement as movement
import time


move = movement.Movement(GyroSensor())

LEFT = move.left_turn
RIGHT = move.right_turn

def follow_line(line_color1, line_color2 = None):
    last_turn = RIGHT
    sensor = ColorSensor()
    angle = 10
    
    color = sensor.color
    print(color)

    if color == line_color1:
        move.go_forward_slow()
        print("found")

    #elif (line_color2 != None):
    #    if color == line_color2:
    #        tank_drive.off()
        
    else:
        while True:
            print("lost")

            if color != line_color1:
                angle += 10
                angle = min(angle, 90)
                if last_turn == LEFT:
                   RIGHT(angle)
                   last_turn = RIGHT
                else:
                    LEFT(angle)
                    last_turn = LEFT
                color = sensor.color

            else:
                break


while True:
    follow_line(ColorSensor.COLOR_WHITE, line_color2=ColorSensor.COLOR_YELLOW)
