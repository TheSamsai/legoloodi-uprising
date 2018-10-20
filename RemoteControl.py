#!/usr/bin/env python3

import sys, termios, tty, os, time
import movement as Movement
import claw as Claw

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
        Movement.right_turn(30)
        time.sleep(button_delay)

    elif (char == 'a'):
        print('Left')
        Movement.left_turn(30)
        time.sleep(button_delay)
    
    elif (char == 'w'):
        print('Forward')
        Movement.go_forward_slow()
        time.sleep(button_delay)

    elif (char == 's'):
        print('Backwards')
        Movement.go_backward_slow()
        time.sleep(button_delay)


    elif (char == 'z'):
        print('ClawClose')
        Claw.close()
        time.sleep(button_delay)
        
    elif (char == 'x'):
        print('ClawOpen')
        Claw.open()
        time.sleep(button_delay)