"""
Copyright (c) 2026 TKJ製作所
Released under the MIT License.

左右への回転を調整する。

180度回転する時間を見つける

PWMは直進時のPWMを流用

左右それぞれの前進時PWMと停止時の値からの差を逆回転のPWMとする。

左右に回転動作をさせて、180度回転する時間を測る。

adjust_rotate_left.py
"""

from machine import Pin, PWM
import time
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


""" 回転時間の調整 """
adj = []
adj = config.adjustment_rotate_time()
print(adj)

while True:
    time.sleep(0.5)
    if lib_bootSW.SW(): # bootSWが押されたら実行
        lib_LED_pico.LEDonoff(2)

        print("停止")
        set_ligth(rigth_stop)
        set_left(left_stop)

        # modeターミナルブロックの位置に対応した値回転する
        mode = lib_mode.mode_pin()
        print("左回転",left_back,rigth_foward)
        set_ligth(rigth_foward)
        set_left(left_back)
        print(adj[mode-1])
        time.sleep(adj[mode-1])

        print("停止")
        set_ligth(rigth_stop)
        set_left(left_stop)

