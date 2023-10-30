# Simple code to read a message from the Dabble App over the DSDTech HM-10 bluetooth module
# Author: Eric Z. Ayers <ericzundel@gmail.com>

"""CircuitPython Example of how to read data from the Dabble app"""
import binascii #imports that are needed to run this code
import board
import busio
import digitalio
import time
import pwmio

from adafruit_motor import motor #Imports a function from the adafruit_moter libaries

Left_forward = board.GP12 # initializes the variable right_forward  and attaches it to GP12
Left_backward = board.GP13 # initalizes the varible right_backward and attaches it to GP13
Right_backward = board.GP14 # initalizes the varible right_backward and attaches it to GP14
Right_forward = board.GP15 # initalizes the varible right_backward and attaches it to GP15

right_forward = pwmio.PWMOut(Right_forward, frequency=10000) # Tells the controller that the moter is an output
right_backward = pwmio.PWMOut(Right_backward, frequency=10000) # Tells the controller that the moter is an output
left_forward = pwmio.PWMOut(Left_forward, frequency=10000) # Tells the controller that the moter is an output
left_backward = pwmio.PWMOut(Left_backward, frequency=10000) # Tells the controller that the moter is an output

Left_Motor = motor.DCMotor(left_forward, left_backward) #Configuration line (it is required)
Left_Motor_speed = 0 # Initiates the varible for the Left_motor_speed
Right_Motor = motor.DCMotor(right_forward, right_backward) #Configuration line (it is required)
Right_Motor_speed = 0  # Initiates the varible for the Right_motor_speed


from dabble import Dabble

dabble = Dabble(board.GP0, board.GP1, debug=True) #dedines the hardware varriable and attaches it to these pins
def Forward():
    Left_Motor_speed = .5 #Makes left motor roll forward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = .5 #Makes right motor roll forward
    Right_Motor.throttle = Right_Motor_speed

def Backward():
    Left_Motor_speed = -.5 #Makes left motor roll forward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = -.5 #Makes right motor roll forward
    Right_Motor.throttle = Right_Motor_speed

def Left():
    Left_Motor_speed = 0 #Makes left motor roll forward
    Left_Motor.throttle = Left_Motor_speed
    time.sleep(0)
    Right_Motor_speed = .5 #Makes right motor roll forward
    Right_Motor.throttle = Right_Motor_speed

def Right():
    Right_Motor_speed = 0 #Makes right motor roll forward
    Right_Motor.throttle = Right_Motor_speed
    time.sleep(0)
    Left_Motor_speed = .5 #Makes left motor roll forward
    Left_Motor.throttle = Left_Motor_speed

def Stop():
    Left_Motor_speed = 0 #Makes left motor roll forward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 0 #Makes right motor roll forward
    Right_Motor.throttle = Right_Motor_speed

while True:
    message = dabble.read_message()
    if (message != None):
        print("Message: " + str(message))
        # Implement tank steering on a 2 wheeled robot
        if (message.up_arrow_pressed):
            Forward()
            print("Move both motors forward")
        elif (message.down_arrow_pressed):
            Backward()
            print("Move both motors backward")
        elif (message.right_arrow_pressed):
            Right()
            print("Move right")
        elif (message.left_arrow_pressed):
            Left()
            print("Move left ")
        elif (message.no_direction_pressed):
            Stop()
            print("Stop both motors")
        else:
            print("Something crazy happened with direction!")

        if (message.triangle_pressed):
            print("Raise arm")
        elif (message.circle_pressed):
            print("Lower arm")
        elif (message.square_pressed):
            print("Squirt water")
        elif (message.circle_pressed):
            print("Fire laser")
        elif (message.start_pressed):
            print("Turn on LED")
        elif (message.select_pressed):
            print("Do victory dance")
        elif (message.no_action_pressed):
            print("No action")
        else:
            print("Something crazy happened with action!")
