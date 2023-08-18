// Auto-generated. Do not edit!

// (in-package bno055_usb_stick_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let EulerAngles = require('./EulerAngles.js');
let CalibrationStatus = require('./CalibrationStatus.js');
let std_msgs = _finder('std_msgs');
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

class Output {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.acceleration = null;
      this.magnetometer = null;
      this.gyroscope = null;
      this.euler_angles = null;
      this.quaternion = null;
      this.linear_acceleration = null;
      this.gravity_vector = null;
      this.temperature = null;
      this.calibration_status = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('acceleration')) {
        this.acceleration = initObj.acceleration
      }
      else {
        this.acceleration = new geometry_msgs.msg.Vector3();
      }
      if (initObj.hasOwnProperty('magnetometer')) {
        this.magnetometer = initObj.magnetometer
      }
      else {
        this.magnetometer = new geometry_msgs.msg.Vector3();
      }
      if (initObj.hasOwnProperty('gyroscope')) {
        this.gyroscope = initObj.gyroscope
      }
      else {
        this.gyroscope = new geometry_msgs.msg.Vector3();
      }
      if (initObj.hasOwnProperty('euler_angles')) {
        this.euler_angles = initObj.euler_angles
      }
      else {
        this.euler_angles = new EulerAngles();
      }
      if (initObj.hasOwnProperty('quaternion')) {
        this.quaternion = initObj.quaternion
      }
      else {
        this.quaternion = new geometry_msgs.msg.Quaternion();
      }
      if (initObj.hasOwnProperty('linear_acceleration')) {
        this.linear_acceleration = initObj.linear_acceleration
      }
      else {
        this.linear_acceleration = new geometry_msgs.msg.Vector3();
      }
      if (initObj.hasOwnProperty('gravity_vector')) {
        this.gravity_vector = initObj.gravity_vector
      }
      else {
        this.gravity_vector = new geometry_msgs.msg.Vector3();
      }
      if (initObj.hasOwnProperty('temperature')) {
        this.temperature = initObj.temperature
      }
      else {
        this.temperature = 0.0;
      }
      if (initObj.hasOwnProperty('calibration_status')) {
        this.calibration_status = initObj.calibration_status
      }
      else {
        this.calibration_status = new CalibrationStatus();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Output
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [acceleration]
    bufferOffset = geometry_msgs.msg.Vector3.serialize(obj.acceleration, buffer, bufferOffset);
    // Serialize message field [magnetometer]
    bufferOffset = geometry_msgs.msg.Vector3.serialize(obj.magnetometer, buffer, bufferOffset);
    // Serialize message field [gyroscope]
    bufferOffset = geometry_msgs.msg.Vector3.serialize(obj.gyroscope, buffer, bufferOffset);
    // Serialize message field [euler_angles]
    bufferOffset = EulerAngles.serialize(obj.euler_angles, buffer, bufferOffset);
    // Serialize message field [quaternion]
    bufferOffset = geometry_msgs.msg.Quaternion.serialize(obj.quaternion, buffer, bufferOffset);
    // Serialize message field [linear_acceleration]
    bufferOffset = geometry_msgs.msg.Vector3.serialize(obj.linear_acceleration, buffer, bufferOffset);
    // Serialize message field [gravity_vector]
    bufferOffset = geometry_msgs.msg.Vector3.serialize(obj.gravity_vector, buffer, bufferOffset);
    // Serialize message field [temperature]
    bufferOffset = _serializer.float64(obj.temperature, buffer, bufferOffset);
    // Serialize message field [calibration_status]
    bufferOffset = CalibrationStatus.serialize(obj.calibration_status, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Output
    let len;
    let data = new Output(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [acceleration]
    data.acceleration = geometry_msgs.msg.Vector3.deserialize(buffer, bufferOffset);
    // Deserialize message field [magnetometer]
    data.magnetometer = geometry_msgs.msg.Vector3.deserialize(buffer, bufferOffset);
    // Deserialize message field [gyroscope]
    data.gyroscope = geometry_msgs.msg.Vector3.deserialize(buffer, bufferOffset);
    // Deserialize message field [euler_angles]
    data.euler_angles = EulerAngles.deserialize(buffer, bufferOffset);
    // Deserialize message field [quaternion]
    data.quaternion = geometry_msgs.msg.Quaternion.deserialize(buffer, bufferOffset);
    // Deserialize message field [linear_acceleration]
    data.linear_acceleration = geometry_msgs.msg.Vector3.deserialize(buffer, bufferOffset);
    // Deserialize message field [gravity_vector]
    data.gravity_vector = geometry_msgs.msg.Vector3.deserialize(buffer, bufferOffset);
    // Deserialize message field [temperature]
    data.temperature = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [calibration_status]
    data.calibration_status = CalibrationStatus.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 192;
  }

  static datatype() {
    // Returns string type for a message object
    return 'bno055_usb_stick_msgs/Output';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '1189549f30b7c0d425e89b36006afea6';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    std_msgs/Header header
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
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Output(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.acceleration !== undefined) {
      resolved.acceleration = geometry_msgs.msg.Vector3.Resolve(msg.acceleration)
    }
    else {
      resolved.acceleration = new geometry_msgs.msg.Vector3()
    }

    if (msg.magnetometer !== undefined) {
      resolved.magnetometer = geometry_msgs.msg.Vector3.Resolve(msg.magnetometer)
    }
    else {
      resolved.magnetometer = new geometry_msgs.msg.Vector3()
    }

    if (msg.gyroscope !== undefined) {
      resolved.gyroscope = geometry_msgs.msg.Vector3.Resolve(msg.gyroscope)
    }
    else {
      resolved.gyroscope = new geometry_msgs.msg.Vector3()
    }

    if (msg.euler_angles !== undefined) {
      resolved.euler_angles = EulerAngles.Resolve(msg.euler_angles)
    }
    else {
      resolved.euler_angles = new EulerAngles()
    }

    if (msg.quaternion !== undefined) {
      resolved.quaternion = geometry_msgs.msg.Quaternion.Resolve(msg.quaternion)
    }
    else {
      resolved.quaternion = new geometry_msgs.msg.Quaternion()
    }

    if (msg.linear_acceleration !== undefined) {
      resolved.linear_acceleration = geometry_msgs.msg.Vector3.Resolve(msg.linear_acceleration)
    }
    else {
      resolved.linear_acceleration = new geometry_msgs.msg.Vector3()
    }

    if (msg.gravity_vector !== undefined) {
      resolved.gravity_vector = geometry_msgs.msg.Vector3.Resolve(msg.gravity_vector)
    }
    else {
      resolved.gravity_vector = new geometry_msgs.msg.Vector3()
    }

    if (msg.temperature !== undefined) {
      resolved.temperature = msg.temperature;
    }
    else {
      resolved.temperature = 0.0
    }

    if (msg.calibration_status !== undefined) {
      resolved.calibration_status = CalibrationStatus.Resolve(msg.calibration_status)
    }
    else {
      resolved.calibration_status = new CalibrationStatus()
    }

    return resolved;
    }
};

module.exports = Output;
