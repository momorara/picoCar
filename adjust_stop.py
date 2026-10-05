"""
2026/10/05
サーボは個体差があり、config.pyの設定値を調整する必要があります。
その基本となるのが、サーボが停止する値です。
これがズレていると車の直進性を出すのに苦労します。
まずは、停止値を家訓してください。

左右のサーボそれぞれに以下のプログラムを使って、停止値を求めます。
止まった値と動き出した値を記録して、その中間値を停止値とします。

"""

from machine import Pin, PWM
from time import sleep

"""
右車輪　0
左車輪　1
を設定してください。
"""
servo = PWM(Pin(0))

servo.freq(50)

servo.duty_ns(1300 * 1000)
sleep(1)

# 1450～1550usを5us刻みで確認
for us in range(1450, 1551, 5):

    servo.duty_ns(us * 1000)

    print("PWM =", us, "us")
    print("この値でサーボが止まっているか確認してください")

    sleep(2)

# 最後は停止
servo.duty_ns(1500 * 1000)

print("終了")

print("止まっていた、中間値を停止値としてください。")