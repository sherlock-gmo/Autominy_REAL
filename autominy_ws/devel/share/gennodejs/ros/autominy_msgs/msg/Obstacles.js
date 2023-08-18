// Auto-generated. Do not edit!

// (in-package autominy_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let Obstacle = require('./Obstacle.js');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class Obstacles {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.obstacles = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('obstacles')) {
        this.obstacles = initObj.obstacles
      }
      else {
        this.obstacles = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Obstacles
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [obstacles]
    // Serialize the length for message field [obstacles]
    bufferOffset = _serializer.uint32(obj.obstacles.length, buffer, bufferOffset);
    obj.obstacles.forEach((val) => {
      bufferOffset = Obstacle.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Obstacles
    let len;
    let data = new Obstacles(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [obstacles]
    // Deserialize array length for message field [obstacles]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.obstacles = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.obstacles[i] = Obstacle.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    object.obstacles.forEach((val) => {
      length += Obstacle.getMessageSize(val);
    });
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'autominy_msgs/Obstacles';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'bd5a4bc101d0799505ddfd03792ae7c5';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    
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
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Obstacles(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.obstacles !== undefined) {
      resolved.obstacles = new Array(msg.obstacles.length);
      for (let i = 0; i < resolved.obstacles.length; ++i) {
        resolved.obstacles[i] = Obstacle.Resolve(msg.obstacles[i]);
      }
    }
    else {
      resolved.obstacles = []
    }

    return resolved;
    }
};

module.exports = Obstacles;
