import time
from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(SCL, SDA)

pca = PCA9685(i2c, address=0x42)

pca.frequency = 50
#servo1 = servo.Servo(pca.channels[0])
#servo16 = servo.Servo(pca.channels[15])
servo1 = servo.ContinuousServo(pca.channels[0])
#test1= servo.Servo(pca.channels[0])
#sneezy = servo.Servo(pca.channels[6])# 80 down, 100 up, 2
'''def moveServo(start,stop,delta):
    incMove = (stop-start)/100.0
    incTime = delta/100.0
    #using start angle(first value in moveServo) plus incremental moves(incMove) to rotate servo to stop angle in time(delta) increments(incTime) specified
    for x in range(100):
        witch.angle = start + x*incMove 
        doc.angle = stop+10 - x*(incMove + .3) # 0.3 to account for incTime and incMove to keep servo in line with start/stop values,
                                               # otherwise servo will jump at endpoints. stop used in this line to rotate servo opposite direction
        happy.angle = start+15 + x*(incMove - .35)
        dopey.angle = start+20 + x*(incMove - .35)
        sleepy.angle = start+5 + x*(incMove - .35)
        grumpy.throttle = -.125 # minus is a forward rotation, positive is a backwards rotatoin. 1 and -1 are full throttle in either direction
        sneezy.angle = start+20 + x*(incMove - .30)#the .3 adjustment here makes him lunge forward like he is sneezing / .4 for smooth operation
        bashful.angle = stop-30 - x*(incMove - .40)
        snow.angle = start + x*incMove
        time.sleep(incTime)
    #grumpy.throttle = 0 #This will br used if we want to change the direction of rotation.
    for x in range(100):
        witch.angle = stop - x*incMove
        doc.angle = start-20 + x*(incMove + .3)
        happy.angle = stop-20 - x*(incMove - .35)
        dopey.angle = stop-15 - x*(incMove - .35)
        sleepy.angle = stop-30 - x*(incMove - .35)
        #grumpy.throttle = .125  This will be used if we want to change the direction of rotation.
        sneezy.angle = stop-30 - x*(incMove - .40)
        bashful.angle = start+10 + x*(incMove - .40)
        snow.angle = stop - x*incMove
        time.sleep(incTime)
#grumpy.throttle = 0
'''
def testCR():
    print("Starting test")
    print("Setting throttle to 0")
    servo1.throttle = .13#0
    #test1.angle = 30
    time.sleep(0)#3
    print("Set throttle to .13 minimum allowable speed")
    servo1.throttle = .13#.13
    #test1.angle = 90
    time.sleep(0)
    print("Setting throttle to 0")
    servo1.throttle = .13#0
    #test1.angle = 0
    time.sleep(0)#3

'''
def moveServo(start,stop,delta):
    incMove = (stop-start)/100.0
    incTime = delta/100.0
    print("start test")
    for x in range(100):
        #If statement moves servo faster for servos that want to move to end in half the delta time of other servos
        if servo16.angle <= 90:
            print("inside if statement")
            servo1.angle = start + x*incMove 
            servo16.angle = start + 2*x*incMove
        else:
            servo1.angle = start + x*incMove             
        time.sleep(incTime)
    for x in range(100):
        if servo16.angle > 0:
            servo1.angle = stop - x*incMove
            servo16.angle = stop - 2*x*incMove
        else:
            servo1.angle = stop - x*incMove            
        time.sleep(incTime)


moveServo(0,90,5)
'''
while True:
    testCR()
pca.deinit()
pca.reset()