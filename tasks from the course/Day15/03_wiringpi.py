import time

import wiringpi

wiringpi.wiringPiSetupGpio()

wiringpi.pinMode(6, 1)       # Set pin 6 to 1 ( OUTPUT )
wiringpi.digitalWrite(6, 0)  # Write 1 ( HIGH ) to pin 6

stan = 0
while True:
    print(stan)
    wiringpi.digitalWrite(6, stan)
    if stan == 0:
        stan = 1
    else:
        stan = 0
    time.sleep(1)
