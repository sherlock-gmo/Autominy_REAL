
(cl:in-package :asdf)

(defsystem "bno055_usb_stick_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "CalibrationStatus" :depends-on ("_package_CalibrationStatus"))
    (:file "_package_CalibrationStatus" :depends-on ("_package"))
    (:file "EulerAngles" :depends-on ("_package_EulerAngles"))
    (:file "_package_EulerAngles" :depends-on ("_package"))
    (:file "Output" :depends-on ("_package_Output"))
    (:file "_package_Output" :depends-on ("_package"))
  ))