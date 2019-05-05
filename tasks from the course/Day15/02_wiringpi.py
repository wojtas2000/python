import time

import wiringpi

wiringpi.wiringPiSetupGpio()

wiringpi.pinMode(6, 1)       # Set pin 6 to 1 ( OUTPUT )
wiringpi.digitalWrite(6, 1)  # Write 1 ( HIGH ) to pin 6
