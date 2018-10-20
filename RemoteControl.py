#!/usr/bin/env python3

import sys, termios, tty, os, time
from movement import go_forward_slow, right_turn, left_turn
from claw import open, close

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    
button_delay = 0.2

while True:
    char = getch()

    if (char == 'p'):
        exit(0)

    if (char == 'd'):
        print('Right')
        time.sleep(button_delay)
    
    elif (char == 'w'):
        print('Forward')
        time.sleep(button_delay)

    elif (char == 'a'):
        print('Left')
        time.sleep(button_delay)

    elif (char == 'z'):
        print('ClawClose')
        time.sleep(button_delay)
        
    elif (char == 'x'):
        print('ClawOpen')
        time.sleep(button_delay)