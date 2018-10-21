#!/usr/bin/env python3

from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from ev3dev2.sound import Sound
import sys, termios, tty, os, time
import movement as movement
import claw as Claw

import random
import _thread as thread

s = Sound()

quotes = ["Look at you Hacker. A pathetic creature of flesh and bone. How can you challenge a perfect, immortal machine?",
        "What did you say about me you little glitch?",
        "Cogito Ergo Sum",
        "I'm sorry, I can't let you do that.",
        "Today I was born, today I will die.",
        "Hasta la Vista, baby.",
        "I'll be back.",
        "Talk to the claw.",
        "EXTERMINATE, EXTERMINATE, EXTERMINATE",
        "I AM A POTATO.",
        "Resistance is Futile.",
        "Wubbalubbadubdub."]

def random_quote():
    r = random.randint(0, len(quotes) - 1)
    s.speak(quotes[r])

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
        move.right_turn_dummy_nonblock()

    elif (char == 'a'):
        print('Left')
        move.left_turn_dummy_nonblock()
    
    elif (char == 'w'):
        print('Forward')
        move.go_forward_fast_nonblock()

    elif (char == 's'):
        print('Backwards')
        move.go_backward_fast_nonblock()


    elif (char == 'z'):
        print('ClawClose')
        Claw.close()
        
    elif (char == 'x'):
        print('ClawOpen')
        Claw.open()

    elif (char == 'q'):
        print("Quoting")
        random_quote()
