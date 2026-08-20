"""
Copyright (c) 2026 TKJ製作所
Released under the MIT License.

2026/06/06
picoCar　前進時の直進性の調整 
左にズレた場合、左サーボの回転数が右より少ない事となり、右にズレた場合は回転数が右より多いためである。
config.pyの
def rigth_duty():
    # 右車輪　前進 , 後退 ,停止
    return 4420,5400,4900

def left_duty():
    # 左車輪　前進 , 後退 ,停止
    return 5312,4450,4900

の前進数値を調整し、picoCarにアップロードする。

起動すると8秒間前進するので、その直進性を見て右に曲がるようなら右のサーボが遅いので、
rigth_duty　前進の値を調整する。

この調整を行うことで、若干の誤差が残るが、概ね前進時の直進性が得られる。

mode 1 前進
mode 2 後退
がテストできます。

adjust_run.py
"""

from machine import Pin, PWM
import time
import lib_LED
import lib_LED_pico
import config
import lib_bootSW
import lib_mode

# GPIO pin設定
rigth_PIN = 0
left_PIN  = 1
ligth = PWM(Pin(rigth_PIN))
ligth.freq(50)
left = PWM(Pin(left_PIN))
left.freq(50)

# duty設定関数
def set_ligth(duty):
    ligth.duty_u16(duty)
def set_left(duty):
    left.duty_u16(duty)

""" 左右のサーボに対するPWM値を取得 """
rigth_foward,rigth_back,rigth_stop = config.rigth_duty()
left_foward,left_back,left_stop = config.left_duty()
print(rigth_foward,rigth_back,rigth_stop)
print(left_foward,left_back,left_stop)


# modeの数だけ点滅
mode = lib_mode.mode_pin()
if mode !=0:
    lib_LED.LEDonoff(mode)
while True:
    time.sleep(0.5)
    if lib_bootSW.SW(): # bootSWが押されたら実行
        lib_LED_pico.LEDonoff(2)

        print("停止")
        set_ligth(rigth_stop)
        set_left(left_stop)
            
        if mode == 1:
            print("前進")
            set_ligth(rigth_foward)
            set_left(left_foward)
            time.sleep(8)

        if mode == 2:
            print("後退")
            set_ligth(rigth_back)
            set_left(left_back)
            time.sleep(8)

        print("停止")
        set_ligth(rigth_stop)
        set_left(left_stop)

        # modeの数だけ点滅
        mode = lib_mode.mode_pin()
        if mode !=0:
            lib_LED.LEDonoff(mode)
