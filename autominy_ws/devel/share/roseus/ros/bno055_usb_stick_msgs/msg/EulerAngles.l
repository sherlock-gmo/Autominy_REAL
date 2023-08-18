;; Auto-generated. Do not edit!


(when (boundp 'bno055_usb_stick_msgs::EulerAngles)
  (if (not (find-package "BNO055_USB_STICK_MSGS"))
    (make-package "BNO055_USB_STICK_MSGS"))
  (shadow 'EulerAngles (find-package "BNO055_USB_STICK_MSGS")))
(unless (find-package "BNO055_USB_STICK_MSGS::EULERANGLES")
  (make-package "BNO055_USB_STICK_MSGS::EULERANGLES"))

(in-package "ROS")
;;//! \htmlinclude EulerAngles.msg.html


(defclass bno055_usb_stick_msgs::EulerAngles
  :super ros::object
  :slots (_heading _roll _pitch ))

(defmethod bno055_usb_stick_msgs::EulerAngles
  (:init
   (&key
    ((:heading __heading) 0.0)
    ((:roll __roll) 0.0)
    ((:pitch __pitch) 0.0)
    )
   (send-super :init)
   (setq _heading (float __heading))
   (setq _roll (float __roll))
   (setq _pitch (float __pitch))
   self)
  (:heading
   (&optional __heading)
   (if __heading (setq _heading __heading)) _heading)
  (:roll
   (&optional __roll)
   (if __roll (setq _roll __roll)) _roll)
  (:pitch
   (&optional __pitch)
   (if __pitch (setq _pitch __pitch)) _pitch)
  (:serialization-length
   ()
   (+
    ;; float64 _heading
    8
    ;; float64 _roll
    8
    ;; float64 _pitch
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _heading
       (sys::poke _heading (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _roll
       (sys::poke _roll (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _pitch
       (sys::poke _pitch (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _heading
     (setq _heading (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _roll
     (setq _roll (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _pitch
     (setq _pitch (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get bno055_usb_stick_msgs::EulerAngles :md5sum-) "2cfcb5286131de123be05c39311011e6")
(setf (get bno055_usb_stick_msgs::EulerAngles :datatype-) "bno055_usb_stick_msgs/EulerAngles")
(setf (get bno055_usb_stick_msgs::EulerAngles :definition-)
      "float64 heading
float64 roll
float64 pitch
")



(provide :bno055_usb_stick_msgs/EulerAngles "2cfcb5286131de123be05c39311011e6")


