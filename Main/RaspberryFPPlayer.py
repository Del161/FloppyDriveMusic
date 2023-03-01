import RPi.GPIO as GPIO          
from time import sleep

# this is intended to become a python project that plays music on floppy drives
# stepper motors
# 01/03/2023
# author Del161


# the 2 pins for 1 floppy drive
# in1 = direction in2 = steps
dirPin = 17
stepPin = 18
temp1=1
pins = [17, 18]



def setup():
    # setup for the pins

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pins,GPIO.OUT)
    GPIO.output(dirPin,GPIO.LOW)
    GPIO.output(stepPin,GPIO.LOW)

def reset():
    #reset the motor to the correct position
    i=0
    print("resetting")
    GPIO.output(dirPin,GPIO.LOW)
    while i<10:
        GPIO.output(stepPin,GPIO.HIGH)
        GPIO.output(stepPin,GPIO.LOW)
        i+=1
        sleep(0.01)
    i = 0
    GPIO.output(dirPin,GPIO.HIGH)
    while i<6:
        GPIO.output(18,GPIO.HIGH)
        GPIO.output(18,GPIO.LOW)
        sleep(0.01)
        i+=1

def calculate_pause():
    #placeholder list
    print("calc")
    direction = ""
    notes = ["G3", "A3", "B3", "C3", "B3", "C3"]
    frequencies = {
        "C2":65.81,
        "D2":73.00,
        "E2":82.00,
        "F2":87.00,
        "G2":98.00,
        "A2":110.00,
        "B2":123.00,

        "C3":130.81,
        "D3":146.00,
        "E3":164.00,
        "F3":174.00,
        "G3":196.00,
        "A3":220.00,
        "B3":246.00,
    }
    
    for note in notes:
        i = 0

        if direction == GPIO.HIGH:
            direction = GPIO.LOW
        else:
            direction = GPIO.HIGH
        
        GPIO.output(dirPin,direction)
        while i<50:
            GPIO.output(stepPin,GPIO.HIGH)
            GPIO.output(stepPin,GPIO.LOW)
            i+=1
            print(frequencies[note])
            sleep(1/frequencies[note])
        i = 0
    print("done")
    GPIO.cleanup()

def main():
    setup()
    reset()
    calculate_pause()

if __name__ == "__main__":
    main()