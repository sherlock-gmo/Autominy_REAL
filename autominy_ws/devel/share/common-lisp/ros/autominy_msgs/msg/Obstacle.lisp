; Auto-generated. Do not edit!


(cl:in-package autominy_msgs-msg)


;//! \htmlinclude Obstacle.msg.html

(cl:defclass <Obstacle> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (object_frame_id
    :reader object_frame_id
    :initarg :object_frame_id
    :type cl:string
    :initform "")
   (object_id
    :reader object_id
    :initarg :object_id
    :type cl:fixnum
    :initform 0)
   (age
    :reader age
    :initarg :age
    :type cl:real
    :initform 0)
   (prediction_age
    :reader prediction_age
    :initarg :prediction_age
    :type cl:real
    :initform 0)
   (odom
    :reader odom
    :initarg :odom
    :type nav_msgs-msg:Odometry
    :initform (cl:make-instance 'nav_msgs-msg:Odometry))
   (size
    :reader size
    :initarg :size
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3))
   (contour_points
    :reader contour_points
    :initarg :contour_points
    :type (cl:vector geometry_msgs-msg:Point)
   :initform (cl:make-array 0 :element-type 'geometry_msgs-msg:Point :initial-element (cl:make-instance 'geometry_msgs-msg:Point)))
   (classification
    :reader classification
    :initarg :classification
    :type cl:fixnum
    :initform 0)
   (classification_age
    :reader classification_age
    :initarg :classification_age
    :type cl:real
    :initform 0)
   (classification_certainty
    :reader classification_certainty
    :initarg :classification_certainty
    :type cl:float
    :initform 0.0))
)

(cl:defclass Obstacle (<Obstacle>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Obstacle>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Obstacle)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name autominy_msgs-msg:<Obstacle> is deprecated: use autominy_msgs-msg:Obstacle instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <Obstacle>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader autominy_msgs-msg:header-val is deprecated.  Use autominy_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'object_frame_id-val :lambda-list '(m))
(cl:defmethod object_frame_id-val ((m <Obstacle>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader autominy_msgs-msg:object_frame_id-val is deprecated.  Use autominy_msgs-msg:object_frame_id instead.")
  (object_frame_id m))

(cl:ensure-generic-function 'object_id-val :lambda-list '(m))
(cl:defmethod object_id-val ((m <Obstacle>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader autominy_msgs-msg:object_id-val is deprecated.  Use autominy_msgs-msg:object_id instead.")
  (object_id m))

(cl:ensure-generic-function 'age-val :lambda-list '(m))
(cl:defmethod age-val ((m <Obstacle>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader autominy_msgs-msg:age-val is deprecated.  Use autominy_msgs-msg:age instead.")
  (age m))

(cl:ensure-generic-function 'prediction_age-val :lambda-list '(m))
(cl:defmethod prediction_age-val ((m <Obstacle>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader autominy_msgs-msg:prediction_age-val is deprecated.  Use autominy_msgs-msg:prediction_age instead.")
  (prediction_age m))

(cl:ensure-generic-function 'odom-val :lambda-list '(m))
(cl:defmethod odom-val ((m <Obstacle>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader autominy_msgs-msg:odom-val is deprecated.  Use autominy_msgs-msg:odom instead.")
  (odom m))

(cl:ensure-generic-function 'size-val :lambda-list '(m))
(cl:defmethod size-val ((m <Obstacle>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader autominy_msgs-msg:size-val is deprecated.  Use autominy_msgs-msg:size instead.")
  (size m))

(cl:ensure-generic-function 'contour_points-val :lambda-list '(m))
(cl:defmethod contour_points-val ((m <Obstacle>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader autominy_msgs-msg:contour_points-val is deprecated.  Use autominy_msgs-msg:contour_points instead.")
  (contour_points m))

(cl:ensure-generic-function 'classification-val :lambda-list '(m))
(cl:defmethod classification-val ((m <Obstacle>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader autominy_msgs-msg:classification-val is deprecated.  Use autominy_msgs-msg:classification instead.")
  (classification m))

(cl:ensure-generic-function 'classification_age-val :lambda-list '(m))
(cl:defmethod classification_age-val ((m <Obstacle>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader autominy_msgs-msg:classification_age-val is deprecated.  Use autominy_msgs-msg:classification_age instead.")
  (classification_age m))

(cl:ensure-generic-function 'classification_certainty-val :lambda-list '(m))
(cl:defmethod classification_certainty-val ((m <Obstacle>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader autominy_msgs-msg:classification_certainty-val is deprecated.  Use autominy_msgs-msg:classification_certainty instead.")
  (classification_certainty m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<Obstacle>)))
    "Constants for message type '<Obstacle>"
  '((:UNCLASSIFIED . 0)
    (:UNKNOWN_SMALL . 1)
    (:UNKNOWN_BIG . 2)
    (:PEDESTRIAN . 3)
    (:BIKE . 4)
    (:CAR . 5)
    (:TRUCK . 6))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'Obstacle)))
    "Constants for message type 'Obstacle"
  '((:UNCLASSIFIED . 0)
    (:UNKNOWN_SMALL . 1)
    (:UNKNOWN_BIG . 2)
    (:PEDESTRIAN . 3)
    (:BIKE . 4)
    (:CAR . 5)
    (:TRUCK . 6))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Obstacle>) ostream)
  "Serializes a message object of type '<Obstacle>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'object_frame_id))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'object_frame_id))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'object_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'object_id)) ostream)
  (cl:let ((__sec (cl:floor (cl:slot-value msg 'age)))
        (__nsec (cl:round (cl:* 1e9 (cl:- (cl:slot-value msg 'age) (cl:floor (cl:slot-value msg 'age)))))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 0) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __nsec) ostream))
  (cl:let ((__sec (cl:floor (cl:slot-value msg 'prediction_age)))
        (__nsec (cl:round (cl:* 1e9 (cl:- (cl:slot-value msg 'prediction_age) (cl:floor (cl:slot-value msg 'prediction_age)))))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 0) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __nsec) ostream))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'odom) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'size) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'contour_points))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'contour_points))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'classification)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'classification)) ostream)
  (cl:let ((__sec (cl:floor (cl:slot-value msg 'classification_age)))
        (__nsec (cl:round (cl:* 1e9 (cl:- (cl:slot-value msg 'classification_age) (cl:floor (cl:slot-value msg 'classification_age)))))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 0) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __nsec) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'classification_certainty))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Obstacle>) istream)
  "Deserializes a message object of type '<Obstacle>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'object_frame_id) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'object_frame_id) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'object_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'object_id)) (cl:read-byte istream))
    (cl:let ((__sec 0) (__nsec 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 0) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __nsec) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'age) (cl:+ (cl:coerce __sec 'cl:double-float) (cl:/ __nsec 1e9))))
    (cl:let ((__sec 0) (__nsec 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 0) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __nsec) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'prediction_age) (cl:+ (cl:coerce __sec 'cl:double-float) (cl:/ __nsec 1e9))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'odom) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'size) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'contour_points) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'contour_points)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'geometry_msgs-msg:Point))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'classification)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'classification)) (cl:read-byte istream))
    (cl:let ((__sec 0) (__nsec 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 0) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __nsec) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'classification_age) (cl:+ (cl:coerce __sec 'cl:double-float) (cl:/ __nsec 1e9))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'classification_certainty) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Obstacle>)))
  "Returns string type for a message object of type '<Obstacle>"
  "autominy_msgs/Obstacle")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Obstacle)))
  "Returns string type for a message object of type 'Obstacle"
  "autominy_msgs/Obstacle")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Obstacle>)))
  "Returns md5sum for a message object of type '<Obstacle>"
  "56ed5dd3c8412ae50b6a996467672cf4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Obstacle)))
  "Returns md5sum for a message object of type 'Obstacle"
  "56ed5dd3c8412ae50b6a996467672cf4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Obstacle>)))
  "Returns full string definition for message of type '<Obstacle>"
  (cl:format cl:nil "# Detected or simulated object~%################################################################################~%~%# Header~%# header.frame_id defines reference frame~%Header header~%~%# Object frame (analogous to child_frame_id in nav_msgs/Odometry)~%string object_frame_id~%~%~%# ID for tracking~%uint16 object_id~%~%# duration this object has been tracked for~%duration age~%~%# duration since last update/confirmation by measurement~%# (set to 0 as soon as a measurement update is available)~%duration prediction_age~%~%~%# odometry of the object (position, orientation, linear and angular velocities)~%# odom.header.frame_id is header.frame_id~%# child_frame_id is object_frame_id~%nav_msgs/Odometry odom~%~%# maximal size of the object (x,y,z) or (depth, width, height) [m]~%# relative to the object frame, i.e. the orientation of the object is taken into account~%geometry_msgs/Vector3 size~%~%~%# The contour points of the object [m]~%geometry_msgs/Point[] contour_points~%~%~%# definition of most likely class of this object:~%#   0: unclassified~%#   1: unknown small~%#   2: unknown big~%#   3: pedestrian~%#   4: bike~%#   5: car~%#   6: truck~%uint16 UNCLASSIFIED    = 0~%uint16 UNKNOWN_SMALL   = 1~%uint16 UNKNOWN_BIG     = 2~%uint16 PEDESTRIAN      = 3~%uint16 BIKE            = 4~%uint16 CAR             = 5~%uint16 TRUCK           = 6~%~%# most likely class of this object~%uint16 classification~%~%# duration this object has been classified as current class~%duration classification_age~%~%# The higher this value the more reliable the assigned object class [0,1]~%float64 classification_certainty~%~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: nav_msgs/Odometry~%# This represents an estimate of a position and velocity in free space.  ~%# The pose in this message should be specified in the coordinate frame given by header.frame_id.~%# The twist in this message should be specified in the coordinate frame given by the child_frame_id~%Header header~%string child_frame_id~%geometry_msgs/PoseWithCovariance pose~%geometry_msgs/TwistWithCovariance twist~%~%================================================================================~%MSG: geometry_msgs/PoseWithCovariance~%# This represents a pose in free space with uncertainty.~%~%Pose pose~%~%# Row-major representation of the 6x6 covariance matrix~%# The orientation parameters use a fixed-axis representation.~%# In order, the parameters are:~%# (x, y, z, rotation about X axis, rotation about Y axis, rotation about Z axis)~%float64[36] covariance~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: geometry_msgs/TwistWithCovariance~%# This expresses velocity in free space with uncertainty.~%~%Twist twist~%~%# Row-major representation of the 6x6 covariance matrix~%# The orientation parameters use a fixed-axis representation.~%# In order, the parameters are:~%# (x, y, z, rotation about X axis, rotation about Y axis, rotation about Z axis)~%float64[36] covariance~%~%================================================================================~%MSG: geometry_msgs/Twist~%# This expresses velocity in free space broken into its linear and angular parts.~%Vector3  linear~%Vector3  angular~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Obstacle)))
  "Returns full string definition for message of type 'Obstacle"
  (cl:format cl:nil "# Detected or simulated object~%################################################################################~%~%# Header~%# header.frame_id defines reference frame~%Header header~%~%# Object frame (analogous to child_frame_id in nav_msgs/Odometry)~%string object_frame_id~%~%~%# ID for tracking~%uint16 object_id~%~%# duration this object has been tracked for~%duration age~%~%# duration since last update/confirmation by measurement~%# (set to 0 as soon as a measurement update is available)~%duration prediction_age~%~%~%# odometry of the object (position, orientation, linear and angular velocities)~%# odom.header.frame_id is header.frame_id~%# child_frame_id is object_frame_id~%nav_msgs/Odometry odom~%~%# maximal size of the object (x,y,z) or (depth, width, height) [m]~%# relative to the object frame, i.e. the orientation of the object is taken into account~%geometry_msgs/Vector3 size~%~%~%# The contour points of the object [m]~%geometry_msgs/Point[] contour_points~%~%~%# definition of most likely class of this object:~%#   0: unclassified~%#   1: unknown small~%#   2: unknown big~%#   3: pedestrian~%#   4: bike~%#   5: car~%#   6: truck~%uint16 UNCLASSIFIED    = 0~%uint16 UNKNOWN_SMALL   = 1~%uint16 UNKNOWN_BIG     = 2~%uint16 PEDESTRIAN      = 3~%uint16 BIKE            = 4~%uint16 CAR             = 5~%uint16 TRUCK           = 6~%~%# most likely class of this object~%uint16 classification~%~%# duration this object has been classified as current class~%duration classification_age~%~%# The higher this value the more reliable the assigned object class [0,1]~%float64 classification_certainty~%~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: nav_msgs/Odometry~%# This represents an estimate of a position and velocity in free space.  ~%# The pose in this message should be specified in the coordinate frame given by header.frame_id.~%# The twist in this message should be specified in the coordinate frame given by the child_frame_id~%Header header~%string child_frame_id~%geometry_msgs/PoseWithCovariance pose~%geometry_msgs/TwistWithCovariance twist~%~%================================================================================~%MSG: geometry_msgs/PoseWithCovariance~%# This represents a pose in free space with uncertainty.~%~%Pose pose~%~%# Row-major representation of the 6x6 covariance matrix~%# The orientation parameters use a fixed-axis representation.~%# In order, the parameters are:~%# (x, y, z, rotation about X axis, rotation about Y axis, rotation about Z axis)~%float64[36] covariance~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: geometry_msgs/TwistWithCovariance~%# This expresses velocity in free space with uncertainty.~%~%Twist twist~%~%# Row-major representation of the 6x6 covariance matrix~%# The orientation parameters use a fixed-axis representation.~%# In order, the parameters are:~%# (x, y, z, rotation about X axis, rotation about Y axis, rotation about Z axis)~%float64[36] covariance~%~%================================================================================~%MSG: geometry_msgs/Twist~%# This expresses velocity in free space broken into its linear and angular parts.~%Vector3  linear~%Vector3  angular~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Obstacle>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:length (cl:slot-value msg 'object_frame_id))
     2
     8
     8
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'odom))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'size))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'contour_points) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     2
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Obstacle>))
  "Converts a ROS message object to a list"
  (cl:list 'Obstacle
    (cl:cons ':header (header msg))
    (cl:cons ':object_frame_id (object_frame_id msg))
    (cl:cons ':object_id (object_id msg))
    (cl:cons ':age (age msg))
    (cl:cons ':prediction_age (prediction_age msg))
    (cl:cons ':odom (odom msg))
    (cl:cons ':size (size msg))
    (cl:cons ':contour_points (contour_points msg))
    (cl:cons ':classification (classification msg))
    (cl:cons ':classification_age (classification_age msg))
    (cl:cons ':classification_certainty (classification_certainty msg))
))
