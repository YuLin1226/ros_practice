#!/usr/bin/env python
# PKG = 'numpy_tutorial'
# import roslib; roslib.load_manifest(PKG)

import rospy
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats
from beginner_pkg.msg import Num_complex

import numpy
def talker():
    pub = rospy.Publisher('floats', Num_complex, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    r = rospy.Rate(10) # 10hz


    # int8 id
    # float64 x
    # float64 y
    # int32[] scan
    # string[] landmark
    # beginner_pkg/Num data

    
    while not rospy.is_shutdown():
        a = Num_complex()
        a.id = 5
        a.x = 1.1
        a.y = 2.2
        a.scan = [1,2,3,4,5,6,7,8,9]
        
        pub.publish(a)
        r.sleep()

if __name__ == '__main__':
    talker()