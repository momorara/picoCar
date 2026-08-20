# -*- coding: utf-8 -*-
#!/usr/bin/python3
"""
Copyright (c) 2026 TKJ製作所
Released under the MIT License.

2026/06/09  Modeを読み込みます

"""
from machine import Pin

""" mode pinの読み込み """
# プラグが入っていれば 0 なければ 1
# 返り値が 0でmodeプラグなし、それ以外でmode番号
mode1 = Pin(21, Pin.IN, Pin.PULL_UP)
mode2 = Pin(20, Pin.IN, Pin.PULL_UP)
mode3 = Pin(19, Pin.IN, Pin.PULL_UP)
mode4 = Pin(18, Pin.IN, Pin.PULL_UP)
def mode_pin():
    if mode1.value() == 0:
        return 1
    if mode2.value() == 0:
        return 2
    if mode3.value() == 0:
        return 3
    if mode4.value() == 0:
        return 4
    return 0


def main():
    print(mode_pin())


if __name__=='__main__':
    main()