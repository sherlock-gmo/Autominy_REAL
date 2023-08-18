;; Auto-generated. Do not edit!


(when (boundp 'autominy_msgs::Obstacles)
  (if (not (find-package "AUTOMINY_MSGS"))
    (make-package "AUTOMINY_MSGS"))
  (shadow 'Obstacles (find-package "AUTOMINY_MSGS")))
(unless (find-package "AUTOMINY_MSGS::OBSTACLES")
  (make-package "AUTOMINY_MSGS::OBSTACLES"))

(in-package "ROS")
;;//! \htmlinclude Obstacles.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass autominy_msgs::Obstacles
  :super ros::object
  :slots (_header _obstacles ))

(defmethod autominy_msgs::Obstacles
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:obstacles __obstacles) ())
    )
   (send-super :init)
   (setq _header __header)
   (setq _obstacles __obstacles)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:obstacles
   (&rest __obstacles)
   (if (keywordp (car __obstacles))
       (send* _obstacles __obstacles)
     (progn
       (if __obstacles (setq _obstacles (car __obstacles)))
       _obstacles)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; autominy_msgs/Obstacle[] _obstacles
    (apply #'+ (send-all _obstacles :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; autominy_msgs/Obstacle[] _obstacles
     (write-long (length _obstacles) s)
     (dolist (elem _obstacles)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; autominy_msgs/Obstacle[] _obstacles
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _obstacles (let (r) (dotimes (i n) (push (instance autominy_msgs::Obstacle :init) r)) r))
     (dolist (elem- _obstacles)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get autominy_msgs::Obstacles :md5sum-) "bd5a4bc101d0799505ddfd03792ae7c5")
(setf (get autominy_msgs::Obstacles :datatype-) "autominy_msgs/Obstacles")
(setf (get autominy_msgs::Obstacles :definition-)
      "Header header

Obstacle[] obstacles

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: autominy_msgs/Obstacle
# Detected or simulated object
################################################################################

# Header
# header.frame_id defines reference frame
Header header

# Object frame (analogous to child_frame_id in nav_msgs/Odometry)
string object_frame_id


# ID for tracking
uint16 object_id

# duration this object has been tracked for
duration age

# duration since last update/confirmation by measurement
# (set to 0 as soon as a measurement update is available)
duration prediction_age


# odometry of the object (position, orientation, linear and angular velocities)
# odom.header.frame_id is header.frame_id
# child_frame_id is object_frame_id
nav_msgs/Odometry odom

# maximal size of the object (x,y,z) or (depth, width, height) [m]
# relative to the object frame, i.e. the orientation of the object is taken into account
geometry_msgs/Vector3 size


# The contour points of the object [m]
geometry_msgs/Point[] contour_points


# definition of most likely class of this object:
#   0: unclassified
#   1: unknown small
#   2: unknown big
#   3: pedestrian
#   4: bike
#   5: car
#   6: truck
uint16 UNCLASSIFIED    = 0
uint16 UNKNOWN_SMALL   = 1
uint16 UNKNOWN_BIG     = 2
uint16 PEDESTRIAN      = 3
uint16 BIKE            = 4
uint16 CAR             = 5
uint16 TRUCK           = 6

# most likely class of this object
uint16 classification

# duration this object has been classified as current class
duration classification_age

# The higher this value the more reliable the assigned object class [0,1]
float64 classification_certainty


================================================================================
MSG: nav_msgs/Odometry
# This represents an estimate of a position and velocity in free space.  
# The pose in this message should be specified in the coordinate frame given by header.frame_id.
# The twist in this message should be specified in the coordinate frame given by the child_frame_id
Header header
string child_frame_id
geometry_msgs/PoseWithCovariance pose
geometry_msgs/TwistWithCovariance twist

================================================================================
MSG: geometry_msgs/PoseWithCovariance
# This represents a pose in free space with uncertainty.

Pose pose

# Row-major representation of the 6x6 covariance matrix
# The orientation parameters use a fixed-axis representation.
# In order, the parameters are:
# (x, y, z, rotation about X axis, rotation about Y axis, rotation about Z axis)
float64[36] covariance

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: geometry_msgs/TwistWithCovariance
# This expresses velocity in free space with uncertainty.

Twist twist

# Row-major representation of the 6x6 covariance matrix
# The orientation parameters use a fixed-axis representation.
# In order, the parameters are:
# (x, y, z, rotation about X axis, rotation about Y axis, rotation about Z axis)
float64[36] covariance

================================================================================
MSG: geometry_msgs/Twist
# This expresses velocity in free space broken into its linear and angular parts.
Vector3  linear
Vector3  angular

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
")



(provide :autominy_msgs/Obstacles "bd5a4bc101d0799505ddfd03792ae7c5")


