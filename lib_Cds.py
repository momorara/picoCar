# -*- coding: utf-8 -*-
#!/usr/bin/python3
"""
Copyright (c) 2026 TKJ製作所
Released under the MIT License.

2023/5/8    lib化
            キャリブレーション方法
            このプログラムを起動
            0:オリジナルデータが見える
            最大明るい、最大暗い時のデータをCds max,minに代入する。
2023/05/21  設定値をconfig.pyから取得
v1.0
2026/06/04  picoCar用Cdsの2個対応に改造
2026/06/16  Cdsは1個のみの使用に仕様変更

"""
from machine import ADC, Pin
import time

# 明暗の範囲
Cds_max = 60000
Cds_min = 1500

# ADCオブジェクトを作成
adc1 = ADC(Pin(26))

def read(flag=0):
    # Cds1 読み取り
    analog1_value_org = adc1.read_u16()
    analog1_value = analog1_value_org
    # %に変換
    if analog1_value_org > Cds_max:
        analog1_value = Cds_max
    if analog1_value_org < Cds_min:
        analog1_value = Cds_min
    analog1_100 = int((analog1_value - Cds_min) / (Cds_max - Cds_min) * 1000)
    # 読み取った値を表示 flag = 0
    if flag == 0:
        print("Analog1 Value: ",analog1_value_org,analog1_value , analog1_100)
    return analog1_100

def main():
    Cds1 = read(0)
    Cds_lv = Cds1
    for i in range(60):
        Cds1 = read(0)
        print(Cds_lv,Cds1)
        time.sleep(1)

if __name__=='__main__':
    main()