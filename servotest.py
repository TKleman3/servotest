import time
from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
from adafruit_servokit import ServoKit

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c, address=0x40)

#Head servo channels
kit = ServoKit(channels=16)
head_01 = kit.servo[0]
head_02 = kit.servo[1]
head_03 = kit.servo[2]
head_05 = kit.servo[3]

print("angle 0")
head_01.angle = 0
time.sleep(10)


GPIO.cleanup()
pca.deinit()
pca.reset()