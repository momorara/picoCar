"""
Copyright (c) 2026 TKJ製作所
Released under the MIT License.

20260604
   iR センサーの 受信状態でLED を点灯させる。
   ただし、リモコンの信号はパルス上の点滅です
   信号によっては短くて感知できない場合があるので
   長めの信号を出すリモコンボタンを確認してください。

赤外線を感知して、0を返す

"""
import machine
import time

SW   = machine.Pin(16, machine.Pin.IN)
led  = machine.Pin(17, machine.Pin.OUT)

def read():
    return SW.value()

def main():

    while True:
        sense = 0
        sense = read()
        if sense == 1:
            led.off()
        if sense == 0:
            led.on()        

        print(sense)
        time.sleep(0.01)

if __name__=='__main__':
    main()
