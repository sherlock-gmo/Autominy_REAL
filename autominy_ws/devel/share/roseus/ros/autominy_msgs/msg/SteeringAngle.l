;; Auto-generated. Do not edit!


(when (boundp 'autominy_msgs::SteeringAngle)
  (if (not (find-package "AUTOMINY_MSGS"))
    (make-package "AUTOMINY_MSGS"))
  (shadow 'SteeringAngle (find-package "AUTOMINY_MSGS")))
(unless (find-package "AUTOMINY_MSGS::STEERINGANGLE")
  (make-package "AUTOMINY_MSGS::STEERINGANGLE"))

(in-package "ROS")
;;//! \htmlinclude SteeringAngle.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass autominy_msgs::SteeringAngle
  :super ros::object
  :slots (_header _value ))

(defmethod autominy_msgs::SteeringAngle
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:value __value) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _value (float __value))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:value
   (&optional __value)
   (if __value (setq _value __value)) _value)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float64 _value
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float64 _value
       (sys::poke _value (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float64 _value
     (setq _value (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get autominy_msgs::SteeringAngle :md5sum-) "d053817de0764f9ee90dbc89c4cdd751")
(setf (get autominy_msgs::SteeringAngle :datatype-) "autominy_msgs/SteeringAngle")
(setf (get autominy_msgs::SteeringAngle :definition-)
      "Header header

# speed [radians, positive = left, negative = right]
float64 value

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

")



(provide :autominy_msgs/SteeringAngle "d053817de0764f9ee90dbc89c4cdd751")


