#!/usr/bin/env python3

from ev3dev2.sensor.lego import ColorSensor, GyroSensor
import sys, termios, tty, os, time
import movement as movement
import claw as Claw

move = movement.Movement(GyroSensor())

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    
button_delay = 0.05

while True:
    char = getch()

    if (char == 'p'):
        exit(0)


    if (char == 'd'):
        print('Right')
        move.right_turn_dummy()

    elif (char == 'a'):
        print('Left')
        move.left_turn_dummy()
    
    elif (char == 'w'):
        print('Forward')
        move.go_forward_fast()

    elif (char == 's'):
        print('Backwards')
        move.go_backward_fast()


    elif (char == 'z'):
        print('ClawClose')
        Claw.close()
        
    elif (char == 'x'):
        print('ClawOpen')
        Claw.open()