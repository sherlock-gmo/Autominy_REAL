;; Auto-generated. Do not edit!


(when (boundp 'autominy_msgs::Obstacle)
  (if (not (find-package "AUTOMINY_MSGS"))
    (make-package "AUTOMINY_MSGS"))
  (shadow 'Obstacle (find-package "AUTOMINY_MSGS")))
(unless (find-package "AUTOMINY_MSGS::OBSTACLE")
  (make-package "AUTOMINY_MSGS::OBSTACLE"))

(in-package "ROS")
;;//! \htmlinclude Obstacle.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))
(if (not (find-package "NAV_MSGS"))
  (ros::roseus-add-msgs "nav_msgs"))
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(intern "*UNCLASSIFIED*" (find-package "AUTOMINY_MSGS::OBSTACLE"))
(shadow '*UNCLASSIFIED* (find-package "AUTOMINY_MSGS::OBSTACLE"))
(defconstant autominy_msgs::Obstacle::*UNCLASSIFIED* 0)
(intern "*UNKNOWN_SMALL*" (find-package "AUTOMINY_MSGS::OBSTACLE"))
(shadow '*UNKNOWN_SMALL* (find-package "AUTOMINY_MSGS::OBSTACLE"))
(defconstant autominy_msgs::Obstacle::*UNKNOWN_SMALL* 1)
(intern "*UNKNOWN_BIG*" (find-package "AUTOMINY_MSGS::OBSTACLE"))
(shadow '*UNKNOWN_BIG* (find-package "AUTOMINY_MSGS::OBSTACLE"))
(defconstant autominy_msgs::Obstacle::*UNKNOWN_BIG* 2)
(intern "*PEDESTRIAN*" (find-package "AUTOMINY_MSGS::OBSTACLE"))
(shadow '*PEDESTRIAN* (find-package "AUTOMINY_MSGS::OBSTACLE"))
(defconstant autominy_msgs::Obstacle::*PEDESTRIAN* 3)
(intern "*BIKE*" (find-package "AUTOMINY_MSGS::OBSTACLE"))
(shadow '*BIKE* (find-package "AUTOMINY_MSGS::OBSTACLE"))
(defconstant autominy_msgs::Obstacle::*BIKE* 4)
(intern "*CAR*" (find-package "AUTOMINY_MSGS::OBSTACLE"))
(shadow '*CAR* (find-package "AUTOMINY_MSGS::OBSTACLE"))
(defconstant autominy_msgs::Obstacle::*CAR* 5)
(intern "*TRUCK*" (find-package "AUTOMINY_MSGS::OBSTACLE"))
(shadow '*TRUCK* (find-package "AUTOMINY_MSGS::OBSTACLE"))
(defconstant autominy_msgs::Obstacle::*TRUCK* 6)

(defun autominy_msgs::Obstacle-to-symbol (const)
  (cond
        ((= const 0) 'autominy_msgs::Obstacle::*UNCLASSIFIED*)
        ((= const 1) 'autominy_msgs::Obstacle::*UNKNOWN_SMALL*)
        ((= const 2) 'autominy_msgs::Obstacle::*UNKNOWN_BIG*)
        ((= const 3) 'autominy_msgs::Obstacle::*PEDESTRIAN*)
        ((= const 4) 'autominy_msgs::Obstacle::*BIKE*)
        ((= const 5) 'autominy_msgs::Obstacle::*CAR*)
        ((= const 6) 'autominy_msgs::Obstacle::*TRUCK*)
        (t nil)))

(defclass autominy_msgs::Obstacle
  :super ros::object
  :slots (_header _object_frame_id _object_id _age _prediction_age _odom _size _contour_points _classification _classification_age _classification_certainty ))

(defmethod autominy_msgs::Obstacle
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:object_frame_id __object_frame_id) "")
    ((:object_id __object_id) 0)
    ((:age __age) (instance ros::time :init))
    ((:prediction_age __prediction_age) (instance ros::time :init))
    ((:odom __odom) (instance nav_msgs::Odometry :init))
    ((:size __size) (instance geometry_msgs::Vector3 :init))
    ((:contour_points __contour_points) ())
    ((:classification __classification) 0)
    ((:classification_age __classification_age) (instance ros::time :init))
    ((:classification_certainty __classification_certainty) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _object_frame_id (string __object_frame_id))
   (setq _object_id (round __object_id))
   (setq _age __age)
   (setq _prediction_age __prediction_age)
   (setq _odom __odom)
   (setq _size __size)
   (setq _contour_points __contour_points)
   (setq _classification (round __classification))
   (setq _classification_age __classification_age)
   (setq _classification_certainty (float __classification_certainty))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:object_frame_id
   (&optional __object_frame_id)
   (if __object_frame_id (setq _object_frame_id __object_frame_id)) _object_frame_id)
  (:object_id
   (&optional __object_id)
   (if __object_id (setq _object_id __object_id)) _object_id)
  (:age
   (&optional __age)
   (if __age (setq _age __age)) _age)
  (:prediction_age
   (&optional __prediction_age)
   (if __prediction_age (setq _prediction_age __prediction_age)) _prediction_age)
  (:odom
   (&rest __odom)
   (if (keywordp (car __odom))
       (send* _odom __odom)
     (progn
       (if __odom (setq _odom (car __odom)))
       _odom)))
  (:size
   (&rest __size)
   (if (keywordp (car __size))
       (send* _size __size)
     (progn
       (if __size (setq _size (car __size)))
       _size)))
  (:contour_points
   (&rest __contour_points)
   (if (keywordp (car __contour_points))
       (send* _contour_points __contour_points)
     (progn
       (if __contour_points (setq _contour_points (car __contour_points)))
       _contour_points)))
  (:classification
   (&optional __classification)
   (if __classification (setq _classification __classification)) _classification)
  (:classification_age
   (&optional __classification_age)
   (if __classification_age (setq _classification_age __classification_age)) _classification_age)
  (:classification_certainty
   (&optional __classification_certainty)
   (if __classification_certainty (setq _classification_certainty __classification_certainty)) _classification_certainty)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; string _object_frame_id
    4 (length _object_frame_id)
    ;; uint16 _object_id
    2
    ;; duration _age
    8
    ;; duration _prediction_age
    8
    ;; nav_msgs/Odometry _odom
    (send _odom :serialization-length)
    ;; geometry_msgs/Vector3 _size
    (send _size :serialization-length)
    ;; geometry_msgs/Point[] _contour_points
    (apply #'+ (send-all _contour_points :serialization-length)) 4
    ;; uint16 _classification
    2
    ;; duration _classification_age
    8
    ;; float64 _classification_certainty
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; string _object_frame_id
       (write-long (length _object_frame_id) s) (princ _object_frame_id s)
     ;; uint16 _object_id
       (write-word _object_id s)
     ;; duration _age
       (write-long (send _age :sec) s) (write-long (send _age :nsec) s)
     ;; duration _prediction_age
       (write-long (send _prediction_age :sec) s) (write-long (send _prediction_age :nsec) s)
     ;; nav_msgs/Odometry _odom
       (send _odom :serialize s)
     ;; geometry_msgs/Vector3 _size
       (send _size :serialize s)
     ;; geometry_msgs/Point[] _contour_points
     (write-long (length _contour_points) s)
     (dolist (elem _contour_points)
       (send elem :serialize s)
       )
     ;; uint16 _classification
       (write-word _classification s)
     ;; duration _classification_age
       (write-long (send _classification_age :sec) s) (write-long (send _classification_age :nsec) s)
     ;; float64 _classification_certainty
       (sys::poke _classification_certainty (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; string _object_frame_id
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _object_frame_id (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; uint16 _object_id
     (setq _object_id (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; duration _age
     (send _age :sec (sys::peek buf ptr- :integer)) (incf ptr- 4)  (send _age :nsec (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; duration _prediction_age
     (send _prediction_age :sec (sys::peek buf ptr- :integer)) (incf ptr- 4)  (send _prediction_age :nsec (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; nav_msgs/Odometry _odom
     (send _odom :deserialize buf ptr-) (incf ptr- (send _odom :serialization-length))
   ;; geometry_msgs/Vector3 _size
     (send _size :deserialize buf ptr-) (incf ptr- (send _size :serialization-length))
   ;; geometry_msgs/Point[] _contour_points
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _contour_points (let (r) (dotimes (i n) (push (instance geometry_msgs::Point :init) r)) r))
     (dolist (elem- _contour_points)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; uint16 _classification
     (setq _classification (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; duration _classification_age
     (send _classification_age :sec (sys::peek buf ptr- :integer)) (incf ptr- 4)  (send _classification_age :nsec (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float64 _classification_certainty
     (setq _classification_certainty (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get autominy_msgs::Obstacle :md5sum-) "56ed5dd3c8412ae50b6a996467672cf4")
(setf (get autominy_msgs::Obstacle :datatype-) "autominy_msgs/Obstacle")
(setf (get autominy_msgs::Obstacle :definition-)
      "# Detected or simulated object
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



(provide :autominy_msgs/Obstacle "56ed5dd3c8412ae50b6a996467672cf4")


