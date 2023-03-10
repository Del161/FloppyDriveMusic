import RPi.GPIO as GPIO          
from time import sleep
import time

# this is intended to become a python project that plays 
# music on floppy drives stepper motors
# 01/03/2023
# author Del161
# discord XDel #0982


# the 2 pins for 1 floppy drive
# in1 = direction in2 = steps
dirPin = 17
stepPin = 18
temp1=1
pins = [17, 18]

# all the midi notes on a piano, most will be too high for a floppy drive though    
midiNotes = {
127:12543.85,
126:11839.82,
125:11175.30,
124:10548.08,
123:9956.06,
122:9397.27,
121:8869.84,
120:8372.02,
119:7902.13,
118:7458.62,
117:7040.00,
116:6644.88,
115:6271.93,
114:5919.91,
113:5587.65,
112:5274.04,
111:4978.03,
110:4698.64,
109:4434.92,
108:4186.01,
107:3951.07,
106:3729.31,
105:3520.00,
104:3322.44,
103:3135.96,
102:2959.96,
101:2793.83,
100:2637.02,
99:2489.02,
98:2349.32,
97:2217.46,
96:2093.00,
95:1975.53,
94:1864.66,
93:1760.00,
92:1661.22,
91:1567.98,
90:1479.98,
89:1396.91,
88:1318.51,
87:1244.51,
86:1174.66,
85:1108.73,
84:1046.50,
83:987.77,
82:932.33,
81:880.00,
80:830.61,
79:783.99,
78:739.99,
77:698.46,
76:659.26,
75:622.25,
74:587.33,
73:554.37,
72:523.25,
71:493.88,
70:466.16,
69:440.00,
68:415.30,
67:369.99,
65:349.23,
64:329.63,
63:311.13,
62:293.66,
61:277.18,
60:261.63,
59:246.94,
58:233.08,
57:220.00,
56:207.65,
55:196.00,
54:185.00,
53:174.61,
52:164.81,
51:155.56,
50:138.59,
48:130.81,
47:123.47,
46:116.54,
45:110.00,
44:103.83,
43:98.00,
42:92.50,
41:87.31,
40:82.41,
39:77.78,
38:73.42,
37:69.30,
36:65.41,
35:61.74,
34:58.27,
33:55.00,
32:49.00,
30:46.25,
29:43.65,
28:41.20,
27:38.89,
26:36.71,
25:34.65,
24:32.70,
23:30.87,
22:29.14,
21:27.50,
20:25.96,
19:24.50,
18:23.12,
17:21.83,
16:20.60,
15:19.45,
14:18.35,
13:17.32,
12:16.35,
11:15.43,
10:14.57,
9:13.75,
8:12.98,
7:12.25,
6:11.56,
5:10.91,
4:10.30,
3:9.72,
2:9.18,
1:8.66,
0:8.18
}


def setup():
    # setup for the pins
    GPIO.cleanup()
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
        sleep(0.5)
    i = 0
    GPIO.output(dirPin,GPIO.HIGH)
    while i<6:
        GPIO.output(18,GPIO.HIGH)
        GPIO.output(18,GPIO.LOW)
        sleep(0.5)
        i+=1

def calculate_pause(notedata):
    print("calc")
    direction = GPIO.HIGH
    i2 = 0

    for index in range(len(notedata[1])):
        notetime = notedata[0]
        notepitch = notedata[1]
        note_time = notetime[index + 1]
        note_key = notepitch[index]

        i2 = 0
        # endtime is when the note should end
        endtime = time.time() + (int(note_time)/100)

        while time.time()<endtime:
            # send the pulse
            GPIO.output(stepPin,GPIO.HIGH)
            GPIO.output(stepPin,GPIO.LOW)

            # sleep the fequency of the note
            sleep(1/midiNotes[int(note_key)])

            print(time.time())
            print(endtime)
            print(midiNotes[int(note_key)])

            # change direction of the motor
            if direction == GPIO.HIGH and i2 == 5:
                    direction = GPIO.LOW
                    i2 = 0
            elif direction == GPIO.LOW and i2 == 5:
                direction = GPIO.HIGH
                i2 = 0
            
            GPIO.output(dirPin,direction)
            i2 += 1
    print("done")
    GPIO.cleanup()

def main():
    setup()
    reset()
    calculate_pause()

if __name__ == "__main__":
    main()