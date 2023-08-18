; Auto-generated. Do not edit!


(cl:in-package bno055_usb_stick_msgs-msg)


;//! \htmlinclude CalibrationStatus.msg.html

(cl:defclass <CalibrationStatus> (roslisp-msg-protocol:ros-message)
  ((system
    :reader system
    :initarg :system
    :type cl:fixnum
    :initform 0)
   (gyroscope
    :reader gyroscope
    :initarg :gyroscope
    :type cl:fixnum
    :initform 0)
   (accelerometer
    :reader accelerometer
    :initarg :accelerometer
    :type cl:fixnum
    :initform 0)
   (magnetometer
    :reader magnetometer
    :initarg :magnetometer
    :type cl:fixnum
    :initform 0))
)

(cl:defclass CalibrationStatus (<CalibrationStatus>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CalibrationStatus>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CalibrationStatus)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name bno055_usb_stick_msgs-msg:<CalibrationStatus> is deprecated: use bno055_usb_stick_msgs-msg:CalibrationStatus instead.")))

(cl:ensure-generic-function 'system-val :lambda-list '(m))
(cl:defmethod system-val ((m <CalibrationStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader bno055_usb_stick_msgs-msg:system-val is deprecated.  Use bno055_usb_stick_msgs-msg:system instead.")
  (system m))

(cl:ensure-generic-function 'gyroscope-val :lambda-list '(m))
(cl:defmethod gyroscope-val ((m <CalibrationStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader bno055_usb_stick_msgs-msg:gyroscope-val is deprecated.  Use bno055_usb_stick_msgs-msg:gyroscope instead.")
  (gyroscope m))

(cl:ensure-generic-function 'accelerometer-val :lambda-list '(m))
(cl:defmethod accelerometer-val ((m <CalibrationStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader bno055_usb_stick_msgs-msg:accelerometer-val is deprecated.  Use bno055_usb_stick_msgs-msg:accelerometer instead.")
  (accelerometer m))

(cl:ensure-generic-function 'magnetometer-val :lambda-list '(m))
(cl:defmethod magnetometer-val ((m <CalibrationStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader bno055_usb_stick_msgs-msg:magnetometer-val is deprecated.  Use bno055_usb_stick_msgs-msg:magnetometer instead.")
  (magnetometer m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CalibrationStatus>) ostream)
  "Serializes a message object of type '<CalibrationStatus>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'system)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'system)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gyroscope)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'gyroscope)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'accelerometer)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'accelerometer)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'magnetometer)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'magnetometer)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CalibrationStatus>) istream)
  "Deserializes a message object of type '<CalibrationStatus>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'system)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'system)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'gyroscope)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'gyroscope)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'accelerometer)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'accelerometer)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'magnetometer)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'magnetometer)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CalibrationStatus>)))
  "Returns string type for a message object of type '<CalibrationStatus>"
  "bno055_usb_stick_msgs/CalibrationStatus")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CalibrationStatus)))
  "Returns string type for a message object of type 'CalibrationStatus"
  "bno055_usb_stick_msgs/CalibrationStatus")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CalibrationStatus>)))
  "Returns md5sum for a message object of type '<CalibrationStatus>"
  "dcc2b46dfebad9476df3c38a333f4515")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CalibrationStatus)))
  "Returns md5sum for a message object of type 'CalibrationStatus"
  "dcc2b46dfebad9476df3c38a333f4515")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CalibrationStatus>)))
  "Returns full string definition for message of type '<CalibrationStatus>"
  (cl:format cl:nil "# 3 indicates fully calibrated; 0 indicates not calibrated~%~%uint16 system~%uint16 gyroscope~%uint16 accelerometer~%uint16 magnetometer~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CalibrationStatus)))
  "Returns full string definition for message of type 'CalibrationStatus"
  (cl:format cl:nil "# 3 indicates fully calibrated; 0 indicates not calibrated~%~%uint16 system~%uint16 gyroscope~%uint16 accelerometer~%uint16 magnetometer~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CalibrationStatus>))
  (cl:+ 0
     2
     2
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CalibrationStatus>))
  "Converts a ROS message object to a list"
  (cl:list 'CalibrationStatus
    (cl:cons ':system (system msg))
    (cl:cons ':gyroscope (gyroscope msg))
    (cl:cons ':accelerometer (accelerometer msg))
    (cl:cons ':magnetometer (magnetometer msg))
))
