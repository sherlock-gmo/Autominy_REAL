; Auto-generated. Do not edit!


(cl:in-package bno055_usb_stick_msgs-msg)


;//! \htmlinclude Output.msg.html

(cl:defclass <Output> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (acceleration
    :reader acceleration
    :initarg :acceleration
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3))
   (magnetometer
    :reader magnetometer
    :initarg :magnetometer
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3))
   (gyroscope
    :reader gyroscope
    :initarg :gyroscope
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3))
   (euler_angles
    :reader euler_angles
    :initarg :euler_angles
    :type bno055_usb_stick_msgs-msg:EulerAngles
    :initform (cl:make-instance 'bno055_usb_stick_msgs-msg:EulerAngles))
   (quaternion
    :reader quaternion
    :initarg :quaternion
    :type geometry_msgs-msg:Quaternion
    :initform (cl:make-instance 'geometry_msgs-msg:Quaternion))
   (linear_acceleration
    :reader linear_acceleration
    :initarg :linear_acceleration
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3))
   (gravity_vector
    :reader gravity_vector
    :initarg :gravity_vector
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3))
   (temperature
    :reader temperature
    :initarg :temperature
    :type cl:float
    :initform 0.0)
   (calibration_status
    :reader calibration_status
    :initarg :calibration_status
    :type bno055_usb_stick_msgs-msg:CalibrationStatus
    :initform (cl:make-instance 'bno055_usb_stick_msgs-msg:CalibrationStatus)))
)

(cl:defclass Output (<Output>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Output>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Output)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name bno055_usb_stick_msgs-msg:<Output> is deprecated: use bno055_usb_stick_msgs-msg:Output instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <Output>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader bno055_usb_stick_msgs-msg:header-val is deprecated.  Use bno055_usb_stick_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'acceleration-val :lambda-list '(m))
(cl:defmethod acceleration-val ((m <Output>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader bno055_usb_stick_msgs-msg:acceleration-val is deprecated.  Use bno055_usb_stick_msgs-msg:acceleration instead.")
  (acceleration m))

(cl:ensure-generic-function 'magnetometer-val :lambda-list '(m))
(cl:defmethod magnetometer-val ((m <Output>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader bno055_usb_stick_msgs-msg:magnetometer-val is deprecated.  Use bno055_usb_stick_msgs-msg:magnetometer instead.")
  (magnetometer m))

(cl:ensure-generic-function 'gyroscope-val :lambda-list '(m))
(cl:defmethod gyroscope-val ((m <Output>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader bno055_usb_stick_msgs-msg:gyroscope-val is deprecated.  Use bno055_usb_stick_msgs-msg:gyroscope instead.")
  (gyroscope m))

(cl:ensure-generic-function 'euler_angles-val :lambda-list '(m))
(cl:defmethod euler_angles-val ((m <Output>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader bno055_usb_stick_msgs-msg:euler_angles-val is deprecated.  Use bno055_usb_stick_msgs-msg:euler_angles instead.")
  (euler_angles m))

(cl:ensure-generic-function 'quaternion-val :lambda-list '(m))
(cl:defmethod quaternion-val ((m <Output>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader bno055_usb_stick_msgs-msg:quaternion-val is deprecated.  Use bno055_usb_stick_msgs-msg:quaternion instead.")
  (quaternion m))

(cl:ensure-generic-function 'linear_acceleration-val :lambda-list '(m))
(cl:defmethod linear_acceleration-val ((m <Output>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader bno055_usb_stick_msgs-msg:linear_acceleration-val is deprecated.  Use bno055_usb_stick_msgs-msg:linear_acceleration instead.")
  (linear_acceleration m))

(cl:ensure-generic-function 'gravity_vector-val :lambda-list '(m))
(cl:defmethod gravity_vector-val ((m <Output>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader bno055_usb_stick_msgs-msg:gravity_vector-val is deprecated.  Use bno055_usb_stick_msgs-msg:gravity_vector instead.")
  (gravity_vector m))

(cl:ensure-generic-function 'temperature-val :lambda-list '(m))
(cl:defmethod temperature-val ((m <Output>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader bno055_usb_stick_msgs-msg:temperature-val is deprecated.  Use bno055_usb_stick_msgs-msg:temperature instead.")
  (temperature m))

(cl:ensure-generic-function 'calibration_status-val :lambda-list '(m))
(cl:defmethod calibration_status-val ((m <Output>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader bno055_usb_stick_msgs-msg:calibration_status-val is deprecated.  Use bno055_usb_stick_msgs-msg:calibration_status instead.")
  (calibration_status m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Output>) ostream)
  "Serializes a message object of type '<Output>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'acceleration) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'magnetometer) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'gyroscope) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'euler_angles) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'quaternion) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'linear_acceleration) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'gravity_vector) ostream)
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'temperature))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'calibration_status) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Output>) istream)
  "Deserializes a message object of type '<Output>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'acceleration) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'magnetometer) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'gyroscope) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'euler_angles) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'quaternion) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'linear_acceleration) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'gravity_vector) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'temperature) (roslisp-utils:decode-double-float-bits bits)))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'calibration_status) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Output>)))
  "Returns string type for a message object of type '<Output>"
  "bno055_usb_stick_msgs/Output")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Output)))
  "Returns string type for a message object of type 'Output"
  "bno055_usb_stick_msgs/Output")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Output>)))
  "Returns md5sum for a message object of type '<Output>"
  "1189549f30b7c0d425e89b36006afea6")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Output)))
  "Returns md5sum for a message object of type 'Output"
  "1189549f30b7c0d425e89b36006afea6")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Output>)))
  "Returns full string definition for message of type '<Output>"
  (cl:format cl:nil "std_msgs/Header header~%geometry_msgs/Vector3 acceleration~%geometry_msgs/Vector3 magnetometer~%geometry_msgs/Vector3 gyroscope~%bno055_usb_stick_msgs/EulerAngles euler_angles~%geometry_msgs/Quaternion quaternion~%geometry_msgs/Vector3 linear_acceleration~%geometry_msgs/Vector3 gravity_vector~%float64 temperature~%bno055_usb_stick_msgs/CalibrationStatus calibration_status~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%================================================================================~%MSG: bno055_usb_stick_msgs/EulerAngles~%float64 heading~%float64 roll~%float64 pitch~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: bno055_usb_stick_msgs/CalibrationStatus~%# 3 indicates fully calibrated; 0 indicates not calibrated~%~%uint16 system~%uint16 gyroscope~%uint16 accelerometer~%uint16 magnetometer~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Output)))
  "Returns full string definition for message of type 'Output"
  (cl:format cl:nil "std_msgs/Header header~%geometry_msgs/Vector3 acceleration~%geometry_msgs/Vector3 magnetometer~%geometry_msgs/Vector3 gyroscope~%bno055_usb_stick_msgs/EulerAngles euler_angles~%geometry_msgs/Quaternion quaternion~%geometry_msgs/Vector3 linear_acceleration~%geometry_msgs/Vector3 gravity_vector~%float64 temperature~%bno055_usb_stick_msgs/CalibrationStatus calibration_status~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%================================================================================~%MSG: bno055_usb_stick_msgs/EulerAngles~%float64 heading~%float64 roll~%float64 pitch~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: bno055_usb_stick_msgs/CalibrationStatus~%# 3 indicates fully calibrated; 0 indicates not calibrated~%~%uint16 system~%uint16 gyroscope~%uint16 accelerometer~%uint16 magnetometer~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Output>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'acceleration))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'magnetometer))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'gyroscope))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'euler_angles))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'quaternion))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'linear_acceleration))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'gravity_vector))
     8
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'calibration_status))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Output>))
  "Converts a ROS message object to a list"
  (cl:list 'Output
    (cl:cons ':header (header msg))
    (cl:cons ':acceleration (acceleration msg))
    (cl:cons ':magnetometer (magnetometer msg))
    (cl:cons ':gyroscope (gyroscope msg))
    (cl:cons ':euler_angles (euler_angles msg))
    (cl:cons ':quaternion (quaternion msg))
    (cl:cons ':linear_acceleration (linear_acceleration msg))
    (cl:cons ':gravity_vector (gravity_vector msg))
    (cl:cons ':temperature (temperature msg))
    (cl:cons ':calibration_status (calibration_status msg))
))
