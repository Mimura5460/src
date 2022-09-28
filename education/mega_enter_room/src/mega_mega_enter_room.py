#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import rospy
import time
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class EnterRoom():
    def __init__(self):
        self.twist_pub=rospy.Publisher('/vmegarover/diff_drive_controller/cmd_vel',Twist, queue_size = 1)

        rospy.Subscriber('/scan', LaserScan, self.laserCB)
        self.front_laser_dist=999.9

    def laserCB(self,receive_msg):
        self.front_laser_dist=receive_msg.ranges[359]

    def execute(self):

        vel=Twist()
        vel.linear.x=0.2
        target_dist=2.0
        safe_dist=1.0
        target_time=target_dist/vel.linear.x
        start_time=time.time()
        stop_time=0
        stop_start=0
        stop_end=0

        while not rospy.is_shutdown():

            if self.front_laser_dist>=safe_dist:
                self.twist_pub.publish(vel)
                print("Go Straight")

            elif self.front_laser_dist<=safe_dist:
                stop_start=time.time()
                print("Disability in front of you")
                rospy.sleep(1.0)
                stop_end=time.time()-stop_start
                stop_time+=stop_end

            finish_time=time.time()-start_time-stop_time

            if finish_time>=target_time:
                print("Completed Entry")
                break

if __name__=='__main__':
    rospy.init_node('door_open')

    er=EnterRoom()

    er.execute()
    rospy.spin()
