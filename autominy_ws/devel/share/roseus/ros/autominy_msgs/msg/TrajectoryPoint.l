;; Auto-generated. Do not edit!


(when (boundp 'autominy_msgs::TrajectoryPoint)
  (if (not (find-package "AUTOMINY_MSGS"))
    (make-package "AUTOMINY_MSGS"))
  (shadow 'TrajectoryPoint (find-package "AUTOMINY_MSGS")))
(unless (find-package "AUTOMINY_MSGS::TRAJECTORYPOINT")
  (make-package "AUTOMINY_MSGS::TRAJECTORYPOINT"))

(in-package "ROS")
;;//! \htmlinclude TrajectoryPoint.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass autominy_msgs::TrajectoryPoint
  :super ros::object
  :slots (_pose _velocity _acceleration _time_from_start ))

(defmethod autominy_msgs::TrajectoryPoint
  (:init
   (&key
    ((:pose __pose) (instance geometry_msgs::Pose :init))
    ((:velocity __velocity) (instance geometry_msgs::Twist :init))
    ((:acceleration __acceleration) (instance geometry_msgs::Twist :init))
    ((:time_from_start __time_from_start) (instance ros::time :init))
    )
   (send-super :init)
   (setq _pose __pose)
   (setq _velocity __velocity)
   (setq _acceleration __acceleration)
   (setq _time_from_start __time_from_start)
   self)
  (:pose
   (&rest __pose)
   (if (keywordp (car __pose))
       (send* _pose __pose)
     (progn
       (if __pose (setq _pose (car __pose)))
       _pose)))
  (:velocity
   (&rest __velocity)
   (if (keywordp (car __velocity))
       (send* _velocity __velocity)
     (progn
       (if __velocity (setq _velocity (car __velocity)))
       _velocity)))
  (:acceleration
   (&rest __acceleration)
   (if (keywordp (car __acceleration))
       (send* _acceleration __acceleration)
     (progn
       (if __acceleration (setq _acceleration (car __acceleration)))
       _acceleration)))
  (:time_from_start
   (&optional __time_from_start)
   (if __time_from_start (setq _time_from_start __time_from_start)) _time_from_start)
  (:serialization-length
   ()
   (+
    ;; geometry_msgs/Pose _pose
    (send _pose :serialization-length)
    ;; geometry_msgs/Twist _velocity
    (send _velocity :serialization-length)
    ;; geometry_msgs/Twist _acceleration
    (send _acceleration :serialization-length)
    ;; duration _time_from_start
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; geometry_msgs/Pose _pose
       (send _pose :serialize s)
     ;; geometry_msgs/Twist _velocity
       (send _velocity :serialize s)
     ;; geometry_msgs/Twist _acceleration
       (send _acceleration :serialize s)
     ;; duration _time_from_start
       (write-long (send _time_from_start :sec) s) (write-long (send _time_from_start :nsec) s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; geometry_msgs/Pose _pose
     (send _pose :deserialize buf ptr-) (incf ptr- (send _pose :serialization-length))
   ;; geometry_msgs/Twist _velocity
     (send _velocity :deserialize buf ptr-) (incf ptr- (send _velocity :serialization-length))
   ;; geometry_msgs/Twist _acceleration
     (send _acceleration :deserialize buf ptr-) (incf ptr- (send _acceleration :serialization-length))
   ;; duration _time_from_start
     (send _time_from_start :sec (sys::peek buf ptr- :integer)) (incf ptr- 4)  (send _time_from_start :nsec (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get autominy_msgs::TrajectoryPoint :md5sum-) "4c309845772249e786605716950755c3")
(setf (get autominy_msgs::TrajectoryPoint :datatype-) "autominy_msgs/TrajectoryPoint")
(setf (get autominy_msgs::TrajectoryPoint :definition-)
      "# This represents a point on a trajectory given a pose velocity and acceleration at a given time
geometry_msgs/Pose pose
geometry_msgs/Twist velocity
geometry_msgs/Twist acceleration

duration time_from_start

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
")



(provide :autominy_msgs/TrajectoryPoint "4c309845772249e786605716950755c3")


