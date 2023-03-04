import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
coil_A_1_pin = 3  # black
coil_A_2_pin = 4  # blue
coil_B_1_pin = 27 # green
coil_B_2_pin = 22 # red
enable_pin   = 2  # maybe needed 
 
                                    # may change for other motors
StepCount = 4
Seq = []
Seq.append([0,1,0,1])
Seq.append([1,0,0,1])
Seq.append([1,0,1,0])
Seq.append([0,1,1,0])

 
GPIO.setup(enable_pin, GPIO.OUT)   # enable when "enable_pin" is active 
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)
 
GPIO.output(enable_pin, GPIO.HIGH) # enable when "enable_pin" is active 
 
def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)
 
def forward(delay, steps):
    for i in range(steps):
        for j in range(StepCount):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)
 
def backwards(delay, steps):
    for i in range(steps):
        for j in reversed(range(StepCount)):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)
            
if __name__ == '__main__':
    while True:
        #delay = raw_input("time delay (ms)?")
        delay = 30    # fixed delay delete and enable line 49 to use variable delay
        steps = input("How many steps? ")
        forward(float(delay) / 1000.0, int(steps))
        steps = input("How many backward steps? ")
        backwards(float(delay) / 1000.0, int(steps))
