#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#--------------------------------------------------------------------------
#Title: ドアが開いているときに進むノード（トピック通信）
#Author: Shunsuke Wada
#Data 2022/9/5
#Memo: 
#Memo:
#--------------------------------------------------------------------------

import rospy
import time
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class EnterRoom():
    def __init__(self):
        #パブリッシャの宣言
        self.twist_pub = rospy.Publisher('/vmegarover/diff_drive_controller/cmd_vel', Twist, queue_size = 1)
        #サブスクライバーの宣言
        rospy.Subscriber('/scan',LaserScan,self.laserCB)
        #値の初期化
        self.front_laser_dist = 999.9

    def laserCB(self,receive_msg):
        #LIDERの視野角
        self.front_laser_dist = receive_msg.ranges[359]

    def exesute(self):
        vel =Twist()
        #進む距離と速度
        vel.linear.x = 0.2
        target_dist = 2.0
        #安全距離
        safe_dist =1.0
        #目標タイムの計算
        target_time = target_dist / vel.linear.x
        #実行開始時間を格納
        start_time = time.time()
        #値の初期化
        stop_time = 0
        stop_start = 0
        stop_end = 0
        rospy.loginfo('Start door open')
        rospy.sleep(0.5)
        while not rospy.is_shutdown():
            #安全距離のとき実行
            if self.if self.front_laser_dist >= safe_dist:
                self.twist_pub.publish(vel)
                rospy.sleep(0.5)
                    
            #障害物があるとき実行
            elif self.front_laser_dist <= safe_dist:
                #現在の時間を格納
                stop_start = time.time()
                rospy.loginfo('Please open door')
                rospy.sleep(10.0)

                #止まっていた時間の格納
                stop_end = time.time() - stop_start
                stop_time += stop_end
            #終了時刻を格納
            finish_time = time.time() - start_time - stop_time
            #時間計測
            print("now_time = ", time.time() - start_time - stop_time)
            #目標タイムに到達したとき実行
            if finish_time >= target_time:
                rospy.loginfo('End door open')
                break

if __name__ == '__main__':
    rospy.init_node('door_open1')
    er = EnterRoom()
    er.execute()
    rospy.spin()


