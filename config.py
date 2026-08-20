# -*- coding: utf-8 -*-
#!/usr/bin/python3
"""
Copyright (c) 2026 TKJ製作所
Released under the MIT License.

v1.1
2026/06/06  picoCar用の設定ファィル
2026/08/20
"""

def rigth_duty():
    # 右車輪　前進 , 後退 ,停止
    return 4420,5250,4900

def left_duty():
    # 左車輪　前進 , 後退 ,停止
    return 5312,4450,4900

def adjustment_rotate_time():
    # 回転時　右回転　左回転 
    return 1.3,1.4,1.5,1.7

def rotate_time():
    # 回転時間　右回転　左回転 180度
    return 1.6,1.65

def main():
    print(rigth_duty())
    print(left_duty())
    print(adjustment_rotate_time())
    print(rotate_time())

if __name__=='__main__':
    main()