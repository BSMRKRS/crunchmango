import RoboPiLib as RPL
import setup
import time
#so for this one, I was thinking that we could make the robot turn based on...
#...direction from the magnetometer

#setting up the motor pins
mL = 0
mR = 2

#setting up the motor speeds
spl = 2000
spr = 100
st = 0

#setting up the magnetometer pins
pwr = 1
data = 2
clock = 3
boardposit = 4
