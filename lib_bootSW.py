"""
Copyright (c) 2026 TKJ製作所
Released under the MIT License.

2026/06/16
PicoのLEDをPWM点滅させながらBootスイッチを監視
bootスイッチを押すと終了し、1を返す

2026/06/19  Cds機能を追加
            引数として、
              non or 0:特に何もしない
                     1:関数に来た時のCds値を取得し、30%以上明るくなったら  終了し、1を返す
"""
from machine import Pin, PWM
from time import sleep_ms
import rp2


# 基板上LED
led = PWM(Pin(25))

# PWM周波数
led.freq(1000)

def SW(Cds=None):
    if Cds != None:
        import lib_Cds
        Cds_lv = lib_Cds.read() * 1.3
        if Cds_lv > 999:
            Cds_lv = 970
    sw = 0
    while sw == 0:
        # 明るくする
        for duty in range(0, 65535, 800):
            led.duty_u16(duty)
            sleep_ms(5)
            if rp2.bootsel_button(): # bootSWが押されたら PWM点滅から帰る
                sw = 1
                break

        # 暗くする
        for duty in range(65535, 0, -1000):
            led.duty_u16(duty)
            sleep_ms(5)
            if rp2.bootsel_button(): # bootSWが押されたら PWM点滅から帰る
                sw = 1
                break

        # Cdsが30%以上明るくなった
        if Cds != None and Cds_lv < lib_Cds.read():
            sw = 1
            break
                
    # bootSWが押されたら LEDを消して　1を返す
    led.duty_u16(0)
    return 1

def main():
    print(SW()) # or print(SW(1))

if __name__=='__main__':
    main()
