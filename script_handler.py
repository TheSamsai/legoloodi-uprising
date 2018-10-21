#!/usr/bin/env python3

import sys, termios, tty, os, time
import RemoteControl as remote_control
import simpler_follow_line as follow_line


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
    char = getch

    if (char == 'l'): 
        print('Activating line follower')
        while True:
            follow_line.follow_line(line_color1='white', line_color2='black')

    if (char == 'r'):
        print('Ativating remote control')
        remote_control.activate_remote_control()
