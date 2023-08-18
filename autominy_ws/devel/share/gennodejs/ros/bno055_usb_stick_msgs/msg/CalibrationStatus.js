// Auto-generated. Do not edit!

// (in-package bno055_usb_stick_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class CalibrationStatus {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.system = null;
      this.gyroscope = null;
      this.accelerometer = null;
      this.magnetometer = null;
    }
    else {
      if (initObj.hasOwnProperty('system')) {
        this.system = initObj.system
      }
      else {
        this.system = 0;
      }
      if (initObj.hasOwnProperty('gyroscope')) {
        this.gyroscope = initObj.gyroscope
      }
      else {
        this.gyroscope = 0;
      }
      if (initObj.hasOwnProperty('accelerometer')) {
        this.accelerometer = initObj.accelerometer
      }
      else {
        this.accelerometer = 0;
      }
      if (initObj.hasOwnProperty('magnetometer')) {
        this.magnetometer = initObj.magnetometer
      }
      else {
        this.magnetometer = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type CalibrationStatus
    // Serialize message field [system]
    bufferOffset = _serializer.uint16(obj.system, buffer, bufferOffset);
    // Serialize message field [gyroscope]
    bufferOffset = _serializer.uint16(obj.gyroscope, buffer, bufferOffset);
    // Serialize message field [accelerometer]
    bufferOffset = _serializer.uint16(obj.accelerometer, buffer, bufferOffset);
    // Serialize message field [magnetometer]
    bufferOffset = _serializer.uint16(obj.magnetometer, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type CalibrationStatus
    let len;
    let data = new CalibrationStatus(null);
    // Deserialize message field [system]
    data.system = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [gyroscope]
    data.gyroscope = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [accelerometer]
    data.accelerometer = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [magnetometer]
    data.magnetometer = _deserializer.uint16(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'bno055_usb_stick_msgs/CalibrationStatus';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'dcc2b46dfebad9476df3c38a333f4515';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
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
    const resolved = new CalibrationStatus(null);
    if (msg.system !== undefined) {
      resolved.system = msg.system;
    }
    else {
      resolved.system = 0
    }

    if (msg.gyroscope !== undefined) {
      resolved.gyroscope = msg.gyroscope;
    }
    else {
      resolved.gyroscope = 0
    }

    if (msg.accelerometer !== undefined) {
      resolved.accelerometer = msg.accelerometer;
    }
    else {
      resolved.accelerometer = 0
    }

    if (msg.magnetometer !== undefined) {
      resolved.magnetometer = msg.magnetometer;
    }
    else {
      resolved.magnetometer = 0
    }

    return resolved;
    }
};

module.exports = CalibrationStatus;
