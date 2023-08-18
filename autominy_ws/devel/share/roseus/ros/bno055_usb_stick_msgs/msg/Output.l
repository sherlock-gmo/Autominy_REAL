;; Auto-generated. Do not edit!


(when (boundp 'bno055_usb_stick_msgs::Output)
  (if (not (find-package "BNO055_USB_STICK_MSGS"))
    (make-package "BNO055_USB_STICK_MSGS"))
  (shadow 'Output (find-package "BNO055_USB_STICK_MSGS")))
(unless (find-package "BNO055_USB_STICK_MSGS::OUTPUT")
  (make-package "BNO055_USB_STICK_MSGS::OUTPUT"))

(in-package "ROS")
;;//! \htmlinclude Output.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass bno055_usb_stick_msgs::Output
  :super ros::object
  :slots (_header _acceleration _magnetometer _gyroscope _euler_angles _quaternion _linear_acceleration _gravity_vector _temperature _calibration_status ))

(defmethod bno055_usb_stick_msgs::Output
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:acceleration __acceleration) (instance geometry_msgs::Vector3 :init))
    ((:magnetometer __magnetometer) (instance geometry_msgs::Vector3 :init))
    ((:gyroscope __gyroscope) (instance geometry_msgs::Vector3 :init))
    ((:euler_angles __euler_angles) (instance bno055_usb_stick_msgs::EulerAngles :init))
    ((:quaternion __quaternion) (instance geometry_msgs::Quaternion :init))
    ((:linear_acceleration __linear_acceleration) (instance geometry_msgs::Vector3 :init))
    ((:gravity_vector __gravity_vector) (instance geometry_msgs::Vector3 :init))
    ((:temperature __temperature) 0.0)
    ((:calibration_status __calibration_status) (instance bno055_usb_stick_msgs::CalibrationStatus :init))
    )
   (send-super :init)
   (setq _header __header)
   (setq _acceleration __acceleration)
   (setq _magnetometer __magnetometer)
   (setq _gyroscope __gyroscope)
   (setq _euler_angles __euler_angles)
   (setq _quaternion __quaternion)
   (setq _linear_acceleration __linear_acceleration)
   (setq _gravity_vector __gravity_vector)
   (setq _temperature (float __temperature))
   (setq _calibration_status __calibration_status)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:acceleration
   (&rest __acceleration)
   (if (keywordp (car __acceleration))
       (send* _acceleration __acceleration)
     (progn
       (if __acceleration (setq _acceleration (car __acceleration)))
       _acceleration)))
  (:magnetometer
   (&rest __magnetometer)
   (if (keywordp (car __magnetometer))
       (send* _magnetometer __magnetometer)
     (progn
       (if __magnetometer (setq _magnetometer (car __magnetometer)))
       _magnetometer)))
  (:gyroscope
   (&rest __gyroscope)
   (if (keywordp (car __gyroscope))
       (send* _gyroscope __gyroscope)
     (progn
       (if __gyroscope (setq _gyroscope (car __gyroscope)))
       _gyroscope)))
  (:euler_angles
   (&rest __euler_angles)
   (if (keywordp (car __euler_angles))
       (send* _euler_angles __euler_angles)
     (progn
       (if __euler_angles (setq _euler_angles (car __euler_angles)))
       _euler_angles)))
  (:quaternion
   (&rest __quaternion)
   (if (keywordp (car __quaternion))
       (send* _quaternion __quaternion)
     (progn
       (if __quaternion (setq _quaternion (car __quaternion)))
       _quaternion)))
  (:linear_acceleration
   (&rest __linear_acceleration)
   (if (keywordp (car __linear_acceleration))
       (send* _linear_acceleration __linear_acceleration)
     (progn
       (if __linear_acceleration (setq _linear_acceleration (car __linear_acceleration)))
       _linear_acceleration)))
  (:gravity_vector
   (&rest __gravity_vector)
   (if (keywordp (car __gravity_vector))
       (send* _gravity_vector __gravity_vector)
     (progn
       (if __gravity_vector (setq _gravity_vector (car __gravity_vector)))
       _gravity_vector)))
  (:temperature
   (&optional __temperature)
   (if __temperature (setq _temperature __temperature)) _temperature)
  (:calibration_status
   (&rest __calibration_status)
   (if (keywordp (car __calibration_status))
       (send* _calibration_status __calibration_status)
     (progn
       (if __calibration_status (setq _calibration_status (car __calibration_status)))
       _calibration_status)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; geometry_msgs/Vector3 _acceleration
    (send _acceleration :serialization-length)
    ;; geometry_msgs/Vector3 _magnetometer
    (send _magnetometer :serialization-length)
    ;; geometry_msgs/Vector3 _gyroscope
    (send _gyroscope :serialization-length)
    ;; bno055_usb_stick_msgs/EulerAngles _euler_angles
    (send _euler_angles :serialization-length)
    ;; geometry_msgs/Quaternion _quaternion
    (send _quaternion :serialization-length)
    ;; geometry_msgs/Vector3 _linear_acceleration
    (send _linear_acceleration :serialization-length)
    ;; geometry_msgs/Vector3 _gravity_vector
    (send _gravity_vector :serialization-length)
    ;; float64 _temperature
    8
    ;; bno055_usb_stick_msgs/CalibrationStatus _calibration_status
    (send _calibration_status :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; geometry_msgs/Vector3 _acceleration
       (send _acceleration :serialize s)
     ;; geometry_msgs/Vector3 _magnetometer
       (send _magnetometer :serialize s)
     ;; geometry_msgs/Vector3 _gyroscope
       (send _gyroscope :serialize s)
     ;; bno055_usb_stick_msgs/EulerAngles _euler_angles
       (send _euler_angles :serialize s)
     ;; geometry_msgs/Quaternion _quaternion
       (send _quaternion :serialize s)
     ;; geometry_msgs/Vector3 _linear_acceleration
       (send _linear_acceleration :serialize s)
     ;; geometry_msgs/Vector3 _gravity_vector
       (send _gravity_vector :serialize s)
     ;; float64 _temperature
       (sys::poke _temperature (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; bno055_usb_stick_msgs/CalibrationStatus _calibration_status
       (send _calibration_status :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; geometry_msgs/Vector3 _acceleration
     (send _acceleration :deserialize buf ptr-) (incf ptr- (send _acceleration :serialization-length))
   ;; geometry_msgs/Vector3 _magnetometer
     (send _magnetometer :deserialize buf ptr-) (incf ptr- (send _magnetometer :serialization-length))
   ;; geometry_msgs/Vector3 _gyroscope
     (send _gyroscope :deserialize buf ptr-) (incf ptr- (send _gyroscope :serialization-length))
   ;; bno055_usb_stick_msgs/EulerAngles _euler_angles
     (send _euler_angles :deserialize buf ptr-) (incf ptr- (send _euler_angles :serialization-length))
   ;; geometry_msgs/Quaternion _quaternion
     (send _quaternion :deserialize buf ptr-) (incf ptr- (send _quaternion :serialization-length))
   ;; geometry_msgs/Vector3 _linear_acceleration
     (send _linear_acceleration :deserialize buf ptr-) (incf ptr- (send _linear_acceleration :serialization-length))
   ;; geometry_msgs/Vector3 _gravity_vector
     (send _gravity_vector :deserialize buf ptr-) (incf ptr- (send _gravity_vector :serialization-length))
   ;; float64 _temperature
     (setq _temperature (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; bno055_usb_stick_msgs/CalibrationStatus _calibration_status
     (send _calibration_status :deserialize buf ptr-) (incf ptr- (send _calibration_status :serialization-length))
   ;;
   self)
  )

(setf (get bno055_usb_stick_msgs::Output :md5sum-) "1189549f30b7c0d425e89b36006afea6")
(setf (get bno055_usb_stick_msgs::Output :datatype-) "bno055_usb_stick_msgs/Output")
(setf (get bno055_usb_stick_msgs::Output :definition-)
      "std_msgs/Header header
geometry_msgs/Vector3 acceleration
geometry_msgs/Vector3 magnetometer
geometry_msgs/Vector3 gyroscope
bno055_usb_stick_msgs/EulerAngles euler_angles
geometry_msgs/Quaternion quaternion
geometry_msgs/Vector3 linear_acceleration
geometry_msgs/Vector3 gravity_vector
float64 temperature
bno055_usb_stick_msgs/CalibrationStatus calibration_status
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
================================================================================
MSG: bno055_usb_stick_msgs/EulerAngles
float64 heading
float64 roll
float64 pitch
================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: bno055_usb_stick_msgs/CalibrationStatus
# 3 indicates fully calibrated; 0 indicates not calibrated

uint16 system
uint16 gyroscope
uint16 accelerometer
uint16 magnetometer
")



(provide :bno055_usb_stick_msgs/Output "1189549f30b7c0d425e89b36006afea6")


