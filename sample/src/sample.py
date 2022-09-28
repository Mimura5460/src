#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy

def main():
    count=1
    while not rospy.is_shutdown():
        rospy.loginfo("Hello Word")
        print("Hello"+str(count))
        count+=1
        rospy.sleep(1.0)
    rospy.loginfo("Good bye...")

if __name__=="__main__":
    rospy.init_node("tuto_node",anonymous=True)
    main()
