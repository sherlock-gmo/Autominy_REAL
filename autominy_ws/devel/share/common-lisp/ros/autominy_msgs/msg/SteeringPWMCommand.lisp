; Auto-generated. Do not edit!


(cl:in-package autominy_msgs-msg)


;//! \htmlinclude SteeringPWMCommand.msg.html

(cl:defclass <SteeringPWMCommand> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (value
    :reader value
    :initarg :value
    :type cl:fixnum
    :initform 0))
)

(cl:defclass SteeringPWMCommand (<SteeringPWMCommand>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SteeringPWMCommand>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SteeringPWMCommand)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name autominy_msgs-msg:<SteeringPWMCommand> is deprecated: use autominy_msgs-msg:SteeringPWMCommand instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <SteeringPWMCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader autominy_msgs-msg:header-val is deprecated.  Use autominy_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'value-val :lambda-list '(m))
(cl:defmethod value-val ((m <SteeringPWMCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader autominy_msgs-msg:value-val is deprecated.  Use autominy_msgs-msg:value instead.")
  (value m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SteeringPWMCommand>) ostream)
  "Serializes a message object of type '<SteeringPWMCommand>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let* ((signed (cl:slot-value msg 'value)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SteeringPWMCommand>) istream)
  "Deserializes a message object of type '<SteeringPWMCommand>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'value) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SteeringPWMCommand>)))
  "Returns string type for a message object of type '<SteeringPWMCommand>"
  "autominy_msgs/SteeringPWMCommand")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SteeringPWMCommand)))
  "Returns string type for a message object of type 'SteeringPWMCommand"
  "autominy_msgs/SteeringPWMCommand")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SteeringPWMCommand>)))
  "Returns md5sum for a message object of type '<SteeringPWMCommand>"
  "1df4bae6d493b0cc189b572aeab3b8a1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SteeringPWMCommand)))
  "Returns md5sum for a message object of type 'SteeringPWMCommand"
  "1df4bae6d493b0cc189b572aeab3b8a1")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SteeringPWMCommand>)))
  "Returns full string definition for message of type '<SteeringPWMCommand>"
  (cl:format cl:nil "Header header~%~%# steering angle pwm~%int16 value~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SteeringPWMCommand)))
  "Returns full string definition for message of type 'SteeringPWMCommand"
  (cl:format cl:nil "Header header~%~%# steering angle pwm~%int16 value~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SteeringPWMCommand>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SteeringPWMCommand>))
  "Converts a ROS message object to a list"
  (cl:list 'SteeringPWMCommand
    (cl:cons ':header (header msg))
    (cl:cons ':value (value msg))
))
