#!/usr/bin/env python3
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.motor import MoveTank

import time


class Movement:
    def __init__(self, gyro):
        self.gyro = gyro
        self.tank_drive = MoveTank("outA", "outD")

    def go_forward_slow(self):
        self.tank_drive.on_for_rotations(20, 20, 0.5)

    def go_backward_slow(self):
        self.tank_drive.on_for_rotations(-20, -20, 0.5)

    def left_turn(self, angle):
        start_degrees = self.gyro.angle
        desired_degrees = start_degrees - angle

        while self.gyro.angle > desired_degrees:
            self.tank_drive.on_for_rotations(10, -10, 1, block = False)
    
        self.tank_drive.off()

    def right_turn(self, angle):
        start_degrees = self.gyro.angle
        desired_degrees = start_degrees + angle

        while self.gyro.angle < desired_degrees:
            self.tank_drive.on_for_rotations(-10, 10, 1, block = False)
    
        self.tank_drive.off()

    
    def left_turn_dummy(self):
        self.tank_drive.on_for_rotations(10, -10, 0.2)

    def right_turn_dummy(self):
        self.tank_drive.on_for_rotations(-10, 10, 0.2)
