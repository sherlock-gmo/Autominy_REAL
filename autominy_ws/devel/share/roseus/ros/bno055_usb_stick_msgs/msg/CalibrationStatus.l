;; Auto-generated. Do not edit!


(when (boundp 'bno055_usb_stick_msgs::CalibrationStatus)
  (if (not (find-package "BNO055_USB_STICK_MSGS"))
    (make-package "BNO055_USB_STICK_MSGS"))
  (shadow 'CalibrationStatus (find-package "BNO055_USB_STICK_MSGS")))
(unless (find-package "BNO055_USB_STICK_MSGS::CALIBRATIONSTATUS")
  (make-package "BNO055_USB_STICK_MSGS::CALIBRATIONSTATUS"))

(in-package "ROS")
;;//! \htmlinclude CalibrationStatus.msg.html


(defclass bno055_usb_stick_msgs::CalibrationStatus
  :super ros::object
  :slots (_system _gyroscope _accelerometer _magnetometer ))

(defmethod bno055_usb_stick_msgs::CalibrationStatus
  (:init
   (&key
    ((:system __system) 0)
    ((:gyroscope __gyroscope) 0)
    ((:accelerometer __accelerometer) 0)
    ((:magnetometer __magnetometer) 0)
    )
   (send-super :init)
   (setq _system (round __system))
   (setq _gyroscope (round __gyroscope))
   (setq _accelerometer (round __accelerometer))
   (setq _magnetometer (round __magnetometer))
   self)
  (:system
   (&optional __system)
   (if __system (setq _system __system)) _system)
  (:gyroscope
   (&optional __gyroscope)
   (if __gyroscope (setq _gyroscope __gyroscope)) _gyroscope)
  (:accelerometer
   (&optional __accelerometer)
   (if __accelerometer (setq _accelerometer __accelerometer)) _accelerometer)
  (:magnetometer
   (&optional __magnetometer)
   (if __magnetometer (setq _magnetometer __magnetometer)) _magnetometer)
  (:serialization-length
   ()
   (+
    ;; uint16 _system
    2
    ;; uint16 _gyroscope
    2
    ;; uint16 _accelerometer
    2
    ;; uint16 _magnetometer
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint16 _system
       (write-word _system s)
     ;; uint16 _gyroscope
       (write-word _gyroscope s)
     ;; uint16 _accelerometer
       (write-word _accelerometer s)
     ;; uint16 _magnetometer
       (write-word _magnetometer s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint16 _system
     (setq _system (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _gyroscope
     (setq _gyroscope (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _accelerometer
     (setq _accelerometer (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _magnetometer
     (setq _magnetometer (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get bno055_usb_stick_msgs::CalibrationStatus :md5sum-) "dcc2b46dfebad9476df3c38a333f4515")
(setf (get bno055_usb_stick_msgs::CalibrationStatus :datatype-) "bno055_usb_stick_msgs/CalibrationStatus")
(setf (get bno055_usb_stick_msgs::CalibrationStatus :definition-)
      "# 3 indicates fully calibrated; 0 indicates not calibrated

uint16 system
uint16 gyroscope
uint16 accelerometer
uint16 magnetometer
")



(provide :bno055_usb_stick_msgs/CalibrationStatus "dcc2b46dfebad9476df3c38a333f4515")


