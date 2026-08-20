"""
Copyright (c) 2026 TKJ製作所
Released under the MIT License.

2026/06/10
picoCar

電源を入れ BootSWを押されたら
その場で向きを変えて、距離を測り一番遠い方向に向く


def の場合は 引数は (45,0.1) 1ステップの角度と待機時間
角度は20度以上、180以下の整数なら、OK 

lib_faraway.py
"""

from machine import Pin, PWM
import time
import lib_LED
import lib_LED_pico
import config
import lib_bootSW
import lib_SR04
import lib_mode
import random

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

""" 180度回転時間 右回転 左回転 読み込み """
rigth_180rotate_time,left_180rotate_time = config.rotate_time()
dist = []

def left_lotate(deg):
    if deg > 180: deg=180
    lotate_deg = left_180rotate_time * (deg / 180)
    set_ligth(rigth_foward)
    set_left(left_back)
    time.sleep(lotate_deg)
    set_ligth(rigth_stop)
    set_left(left_stop)

def rigth_lotate(deg):
    if deg > 180: deg=180
    lotate_deg = rigth_180rotate_time * (deg / 180)
    set_ligth(rigth_back)
    set_left(left_foward)
    time.sleep(lotate_deg)
    set_ligth(rigth_stop)
    set_left(left_stop)
    
def run():
    print("前進",left_foward ,rigth_foward)
    set_ligth(rigth_foward)
    set_left(left_foward)

def stop():
    print("停止")
    set_ligth(rigth_stop)
    set_left(left_stop)


# 引数として (30 , 0.5 ) 
# 30度毎(ただし20度以上)、0.5秒停止しながら動作 向きはランダムに決定
# 向きを変えながら距離を測定し、遠い方を向く
def faraway(deg, stop_time):
    # ランダムで左右を決定
    direction_n =  random.randint(0, 1)
    direction = "left"
    if direction_n == 1:direction = "rigth"
    print(direction_n)
    dist = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    i = 0
    for deg_LR in range(0,360,deg):
        print(deg_LR)
        if direction == "left":
            left_lotate(deg)
        else:
            rigth_lotate(deg)
        dist[i] = lib_SR04.read()
        i = i + 1
        time.sleep(stop_time)
    # 一番大きい数字の位置を取得
    pos = dist.index(max(dist))
    # 一番遠い角度を取得
    faraway_deg = deg * pos + deg

    print(direction)
    print(dist)
    print(pos)
    print(faraway_deg) # 元位置一歩手前からなので、その分多い

    if faraway_deg != 360 : # 今向いている方向が最大なので、向き変しない
        if faraway_deg <= 180: # 180度以内なら同じ方向へ
            if direction == "left":
                left_lotate(faraway_deg)
                print(faraway_deg,"left_lotate")
            else:
                rigth_lotate(faraway_deg)
                print(faraway_deg,"rigth_lotate")
        else:
            faraway_deg = 360 - faraway_deg
            if direction == "left":
                rigth_lotate(faraway_deg)
                print(faraway_deg,"rigth_lotate")
            else:
                left_lotate(faraway_deg)
                print(faraway_deg,"left_lotate")
    else:
        print(0)


def main():
    while True:
        mode = lib_mode.mode_pin()
        time.sleep(0.5)
        if lib_bootSW.SW(): # bootSWが押されたら実行
            lib_LED_pico.LEDonoff(2)
            if mode == 0:
                faraway(20,0.5)
            if mode == 1:
                faraway(30,0.5)
            if mode == 2:
                faraway(45,0.5)
            if mode == 3:
                faraway(60,0.5)
            if mode == 4:
                faraway(90,0.5)
            time.sleep(5)

if __name__=='__main__':
    main()

