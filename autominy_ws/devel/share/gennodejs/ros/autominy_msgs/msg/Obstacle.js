// Auto-generated. Do not edit!

// (in-package autominy_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let nav_msgs = _finder('nav_msgs');
let std_msgs = _finder('std_msgs');
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

class Obstacle {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.object_frame_id = null;
      this.object_id = null;
      this.age = null;
      this.prediction_age = null;
      this.odom = null;
      this.size = null;
      this.contour_points = null;
      this.classification = null;
      this.classification_age = null;
      this.classification_certainty = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('object_frame_id')) {
        this.object_frame_id = initObj.object_frame_id
      }
      else {
        this.object_frame_id = '';
      }
      if (initObj.hasOwnProperty('object_id')) {
        this.object_id = initObj.object_id
      }
      else {
        this.object_id = 0;
      }
      if (initObj.hasOwnProperty('age')) {
        this.age = initObj.age
      }
      else {
        this.age = {secs: 0, nsecs: 0};
      }
      if (initObj.hasOwnProperty('prediction_age')) {
        this.prediction_age = initObj.prediction_age
      }
      else {
        this.prediction_age = {secs: 0, nsecs: 0};
      }
      if (initObj.hasOwnProperty('odom')) {
        this.odom = initObj.odom
      }
      else {
        this.odom = new nav_msgs.msg.Odometry();
      }
      if (initObj.hasOwnProperty('size')) {
        this.size = initObj.size
      }
      else {
        this.size = new geometry_msgs.msg.Vector3();
      }
      if (initObj.hasOwnProperty('contour_points')) {
        this.contour_points = initObj.contour_points
      }
      else {
        this.contour_points = [];
      }
      if (initObj.hasOwnProperty('classification')) {
        this.classification = initObj.classification
      }
      else {
        this.classification = 0;
      }
      if (initObj.hasOwnProperty('classification_age')) {
        this.classification_age = initObj.classification_age
      }
      else {
        this.classification_age = {secs: 0, nsecs: 0};
      }
      if (initObj.hasOwnProperty('classification_certainty')) {
        this.classification_certainty = initObj.classification_certainty
      }
      else {
        this.classification_certainty = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Obstacle
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [object_frame_id]
    bufferOffset = _serializer.string(obj.object_frame_id, buffer, bufferOffset);
    // Serialize message field [object_id]
    bufferOffset = _serializer.uint16(obj.object_id, buffer, bufferOffset);
    // Serialize message field [age]
    bufferOffset = _serializer.duration(obj.age, buffer, bufferOffset);
    // Serialize message field [prediction_age]
    bufferOffset = _serializer.duration(obj.prediction_age, buffer, bufferOffset);
    // Serialize message field [odom]
    bufferOffset = nav_msgs.msg.Odometry.serialize(obj.odom, buffer, bufferOffset);
    // Serialize message field [size]
    bufferOffset = geometry_msgs.msg.Vector3.serialize(obj.size, buffer, bufferOffset);
    // Serialize message field [contour_points]
    // Serialize the length for message field [contour_points]
    bufferOffset = _serializer.uint32(obj.contour_points.length, buffer, bufferOffset);
    obj.contour_points.forEach((val) => {
      bufferOffset = geometry_msgs.msg.Point.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [classification]
    bufferOffset = _serializer.uint16(obj.classification, buffer, bufferOffset);
    // Serialize message field [classification_age]
    bufferOffset = _serializer.duration(obj.classification_age, buffer, bufferOffset);
    // Serialize message field [classification_certainty]
    bufferOffset = _serializer.float64(obj.classification_certainty, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Obstacle
    let len;
    let data = new Obstacle(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [object_frame_id]
    data.object_frame_id = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [object_id]
    data.object_id = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [age]
    data.age = _deserializer.duration(buffer, bufferOffset);
    // Deserialize message field [prediction_age]
    data.prediction_age = _deserializer.duration(buffer, bufferOffset);
    // Deserialize message field [odom]
    data.odom = nav_msgs.msg.Odometry.deserialize(buffer, bufferOffset);
    // Deserialize message field [size]
    data.size = geometry_msgs.msg.Vector3.deserialize(buffer, bufferOffset);
    // Deserialize message field [contour_points]
    // Deserialize array length for message field [contour_points]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.contour_points = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.contour_points[i] = geometry_msgs.msg.Point.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [classification]
    data.classification = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [classification_age]
    data.classification_age = _deserializer.duration(buffer, bufferOffset);
    // Deserialize message field [classification_certainty]
    data.classification_certainty = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    length += _getByteLength(object.object_frame_id);
    length += nav_msgs.msg.Odometry.getMessageSize(object.odom);
    length += 24 * object.contour_points.length;
    return length + 68;
  }

  static datatype() {
    // Returns string type for a message object
    return 'autominy_msgs/Obstacle';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '56ed5dd3c8412ae50b6a996467672cf4';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
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
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Obstacle(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.object_frame_id !== undefined) {
      resolved.object_frame_id = msg.object_frame_id;
    }
    else {
      resolved.object_frame_id = ''
    }

    if (msg.object_id !== undefined) {
      resolved.object_id = msg.object_id;
    }
    else {
      resolved.object_id = 0
    }

    if (msg.age !== undefined) {
      resolved.age = msg.age;
    }
    else {
      resolved.age = {secs: 0, nsecs: 0}
    }

    if (msg.prediction_age !== undefined) {
      resolved.prediction_age = msg.prediction_age;
    }
    else {
      resolved.prediction_age = {secs: 0, nsecs: 0}
    }

    if (msg.odom !== undefined) {
      resolved.odom = nav_msgs.msg.Odometry.Resolve(msg.odom)
    }
    else {
      resolved.odom = new nav_msgs.msg.Odometry()
    }

    if (msg.size !== undefined) {
      resolved.size = geometry_msgs.msg.Vector3.Resolve(msg.size)
    }
    else {
      resolved.size = new geometry_msgs.msg.Vector3()
    }

    if (msg.contour_points !== undefined) {
      resolved.contour_points = new Array(msg.contour_points.length);
      for (let i = 0; i < resolved.contour_points.length; ++i) {
        resolved.contour_points[i] = geometry_msgs.msg.Point.Resolve(msg.contour_points[i]);
      }
    }
    else {
      resolved.contour_points = []
    }

    if (msg.classification !== undefined) {
      resolved.classification = msg.classification;
    }
    else {
      resolved.classification = 0
    }

    if (msg.classification_age !== undefined) {
      resolved.classification_age = msg.classification_age;
    }
    else {
      resolved.classification_age = {secs: 0, nsecs: 0}
    }

    if (msg.classification_certainty !== undefined) {
      resolved.classification_certainty = msg.classification_certainty;
    }
    else {
      resolved.classification_certainty = 0.0
    }

    return resolved;
    }
};

// Constants for message
Obstacle.Constants = {
  UNCLASSIFIED: 0,
  UNKNOWN_SMALL: 1,
  UNKNOWN_BIG: 2,
  PEDESTRIAN: 3,
  BIKE: 4,
  CAR: 5,
  TRUCK: 6,
}

module.exports = Obstacle;
