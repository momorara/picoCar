"""
Copyright (c) 2026 TKJ製作所
Released under the MIT License.

2026/06/04  SR04で距離を測定する
"""

from machine import Pin, time_pulse_us
import time

led  = Pin(17, Pin.OUT)
TRIG = Pin(14, Pin.OUT)
ECHO = Pin(15, Pin.IN)

def read():
    time.sleep(0.1)
    led.on()
    try:
        TRIG.low()
        time.sleep_us(2)
        TRIG.high()
        time.sleep_us(10)
        TRIG.low()
        duration = time_pulse_us(ECHO, 1, 30000)
        if duration < 0:
            print("測定失敗1")
            return 9 # 測定失敗したら　10cm以内の数字を返す。
        distance = int(duration * 0.0343 / 2)
    except:
        distance = 8 # errしたら　10cm以内の数字を返す。
    led.off()
    if distance is None:
        print("測定失敗2")
        distance = 7 # 測定失敗したら　10cm以内の数字を返す。
    return distance


def main():
    while True:
        d = read()
        if d is not None:
            print("距離 = {:.1f} cm".format(d))
        else:
            print("測定失敗")
        time.sleep(0.5)

if __name__=='__main__':
    main()