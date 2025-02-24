# Automated Drive System for the AutoMiny V4.0
This repository contains the software of an Automated Drive System (ADS) for the [AutoMINY v4.0](https://autominy.github.io/AutoMiny/). With this, the car lane-keeping at different speeds, identify and obey different traffic signals, evade obstacles, stop if pedestrian appears and parking. You can check the [video](https://youtu.be/j18L-LGWZRA?si=wzGuThgaPfrntlDV).

It works with the additional packages:
+[darknet_ros](https://github.com/leggedrobotics/darknet_ros)
+[bno055_usb_stick](https://github.com/yoshito-n-students/bno055_usb_stick)

The ADS' packages are run on board computer while `darknet_ros` and `gps_vis` packages can run on a remote computer. 
![ROS](/media/ros_eng.png)


# How to compile
This repository can be copied in the remote and on board computers. Then, 
```
$ catkin_make --only-pkg-with-deps dotmex_final gps_vis autominy_msgs
```


To identify the objects on the road, the perception system uses a Convolutional Neural Network (CNN) with the YOLOv3 architecture. For this reason, a


# "List of ';' separated packages to build"
catkin_make -DCATKIN_BLACKLIST_PACKAGES="darknet_ros"
