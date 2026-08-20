"""
Copyright (c) 2026 TKJ製作所
Released under the MIT License.

GPIOのLEDを点滅させる
"""

import machine
import time
led = machine.Pin(17, machine.Pin.OUT)

def LEDonoff(num=1):
    for _ in range(num):
        led.on()
        time.sleep(.2)
        led.off()
        time.sleep(.5)
    
def end_LED():
    for _ in range(4):
        led.on()
        time.sleep(.5)
        led.off()
        time.sleep(.1)
    led.on()
    time.sleep(3)
    led.off()

def main():
    for i in range(5):
         LEDonoff()

if __name__=='__main__':
    main()
