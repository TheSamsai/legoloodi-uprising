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
    
button_delay = 0.1

while True:
    char = getch()

    if (char == 'p'):
        exit(0)


    if (char == 'd'):
        print('Right')
        move.right_turn_dummy()
        time.sleep(button_delay)

    elif (char == 'a'):
        print('Left')
        move.left_turn_dummy()
        time.sleep(button_delay)
    
    elif (char == 'w'):
        print('Forward')
        move.go_forward_fast()
        time.sleep(button_delay)

    elif (char == 's'):
        print('Backwards')
        move.go_backward_fast()
        time.sleep(button_delay)


    elif (char == 'z'):
        print('ClawClose')
        Claw.close()
        time.sleep(button_delay)
        
    elif (char == 'x'):
        print('ClawOpen')
        Claw.open()
        time.sleep(button_delay)