#!/usr/bin/env python3
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from ev3dev2.motor import MoveTank
import movement as movement
import time


class LineFollower:
    def __init__(self):
        self.gyro = GyroSensor()
        
        self.gyro.mode = 'GYRO-RATE'
        self.gyro.mode = 'GYRO-ANG'
        self.gyro.mode = 'GYRO-RATE'
        self.gyro.mode = 'GYRO-ANG'
        self.gyro.MODE_GYRO_CAL
        self.gyro.MODE_GYRO_CAL        
        self.move = movement.Movement(GyroSensor())

        self.LEFT = self.move.left_turn
        self.RIGHT = self.move.right_turn

        while True:
            self.follow_line(ColorSensor.COLOR_WHITE, line_color2=ColorSensor.COLOR_YELLOW)

    def follow_line(self, line_color1, line_color2 = None):
        last_turn = self.RIGHT
        sensor = ColorSensor()
        angle = 3
    
        color = sensor.color
        print(color)

        if (line_color2 != None):
            if color == line_color2:
                self.move.stop()

        if color == line_color1:
            self.move.go_forward_slow()
            print("found")
        
        else:
            while True:
                print("lost")
            
                print(color)
            
                try:
                    if color != line_color1:
                        print("isn't " + str(line_color1))
                        angle += 5
                        angle = min(angle, 90)
                        
                        if last_turn == self.LEFT:
                           self.RIGHT(angle)
                           last_turn = self.RIGHT
                        else:
                            self.LEFT(angle)
                            last_turn = self.LEFT
                        color = sensor.color

                    else:
                        break
                except:
                    self.move = movement.Movement(GyroSensor())
                    self.LEFT = self.move.left_turn
                    self.RIGHT = self.move.right_turn

solve = LineFollower()
