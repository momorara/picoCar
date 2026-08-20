"""
Copyright (c) 2026 TKJ製作所
Released under the MIT License.

2026/06/16
picoCar


電源を入れ BootSWを押されたら
その場で向きを変えて、距離を測り一番遠い方向に向いて前進


1. 距離が15cm以内になったら停止

2.その場で向きを変えて、距離を測り一番遠い方向に向いて前進

+ 
走行中赤外線を感知したら、停止しその場で距離の遠い方に回転する。

+
走行中Cdsセンサーを確認し、通常より暗くなったら停止、bootSWで再起動


main_02.py
"""
import time
import lib_LED
import lib_LED_pico
import lib_bootSW
import lib_SR04
import lib_iR
import lib_servo
import lib_Cds

    
def main():
    lib_servo.stop()
    time.sleep(0.5)
    lib_servo.stop()
    while True:
        if lib_bootSW.SW(): # bootSWが押されたら実行
            break

    while True:
        lib_LED.LEDonoff(2)
        # 回転して遠い方向を向く
        print("lib_servo.faraway")
        lib_servo.faraway(45,0.2)
        time.sleep(2)
        # Cds設定
        Cds_lv = lib_Cds.read(0)
        # 前方に直進
        print("lib_servo.run")
        lib_servo.run()
        # 前方の距離が10cm未満になるまで前進を続ける
        print("lib_SR04.read")
        bootSW = 0
        while 15 < lib_SR04.read() and bootSW == 0:
            # 赤外線を感知したら前進を止める
            print("lib_iR.read")
            if lib_iR.read() == 0:
                print("赤外線感知")
                time.sleep(0.001)
                if lib_iR.read() == 0:# 赤外線を感知したら前進を止める
                    print("赤外線感知")
                    break

            # Cdsの明るさが暗くなったら停止
            Cds_lv_now= lib_Cds.read(0)
            print("lib_servo.stop_Cds-1",Cds_lv/1.2,Cds_lv_now)
            if Cds_lv/1.2 > Cds_lv_now:
                print("lib_servo.stop_Cds-2",Cds_lv/1.2,Cds_lv_now)
                lib_servo.stop()
                while True:
                    time.sleep(0.5)
                    if lib_bootSW.SW(): # bootSWが押されたら実行
                        bootSW = 1
                        break
    
        print("lib_servo.stop",)
        lib_servo.stop()
        

if __name__=='__main__':
    main()

