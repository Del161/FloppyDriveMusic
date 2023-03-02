from time import sleep
a = 1
i2 = 0
direction = "GPIO.HIGH"
while a == 1:

    if direction == "GPIO.HIGH" and i2 == 5:
        direction = "GPIO.LOW"
        i2 = 0
    elif direction == "GPIO.LOW" and i2 == 5:
        direction = "GPIO.HIGH"
        i2 = 0
    sleep(0.1)

    print(direction)
    print(i2)
    i2 += 1
