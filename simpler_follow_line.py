from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from ev3dev2.motor import MoveTank
import movement as movement
import time

sensor = ColorSensor()
gyro = GyroSensor()
move = movement.Movement(gyro)
LEFT = move.left_turn
RIGHT = move.right_turn


def follow_line(self, line_color1, line_color2 = None):
        angle = 3
        last_turn = RIGHT
    
        color = sensor.color
        print(color)

        if line_color2 != None:
            if color == line_color2:
                move.stop

        elif color == line_color1:
            move.go_forward_slow()
            print("found")
        
        else:
            while True:
                color = sensor.color
                print("lost")
            
                print(sensor.color_name)

                if last_turn == self.LEFT:
                    self.RIGHT(angle)
                    last_turn = self.RIGHT
                else:                       
                    self.LEFT(angle)    
                    last_turn = self.LEFT
                    color = self.sensor.color

                if color == line_color1 or line_color2:
                    break
                    
                else:
                    angle += 2
                    angle = min(angle, 90)