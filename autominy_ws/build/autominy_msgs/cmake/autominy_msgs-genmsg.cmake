# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "autominy_msgs: 17 messages, 0 services")

set(MSG_I_FLAGS "-Iautominy_msgs:/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/noetic/share/geometry_msgs/cmake/../msg;-Inav_msgs:/opt/ros/noetic/share/nav_msgs/cmake/../msg;-Iactionlib_msgs:/opt/ros/noetic/share/actionlib_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(autominy_msgs_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/NormalizedSpeedCommand.msg" NAME_WE)
add_custom_target(_autominy_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "autominy_msgs" "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/NormalizedSpeedCommand.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/NormalizedSteeringCommand.msg" NAME_WE)
add_custom_target(_autominy_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "autominy_msgs" "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/NormalizedSteeringCommand.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Plot.msg" NAME_WE)
add_custom_target(_autominy_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "autominy_msgs" "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Plot.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringAngle.msg" NAME_WE)
add_custom_target(_autominy_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "autominy_msgs" "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringAngle.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Speed.msg" NAME_WE)
add_custom_target(_autominy_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "autominy_msgs" "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Speed.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SpeedCommand.msg" NAME_WE)
add_custom_target(_autominy_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "autominy_msgs" "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SpeedCommand.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SpeedPWMCommand.msg" NAME_WE)
add_custom_target(_autominy_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "autominy_msgs" "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SpeedPWMCommand.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringCommand.msg" NAME_WE)
add_custom_target(_autominy_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "autominy_msgs" "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringCommand.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringPWMCommand.msg" NAME_WE)
add_custom_target(_autominy_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "autominy_msgs" "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringPWMCommand.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringFeedback.msg" NAME_WE)
add_custom_target(_autominy_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "autominy_msgs" "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringFeedback.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Tick.msg" NAME_WE)
add_custom_target(_autominy_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "autominy_msgs" "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Tick.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Trajectory.msg" NAME_WE)
add_custom_target(_autominy_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "autominy_msgs" "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Trajectory.msg" "geometry_msgs/Twist:autominy_msgs/TrajectoryPoint:geometry_msgs/Pose:geometry_msgs/Point:geometry_msgs/Vector3:geometry_msgs/Quaternion:std_msgs/Header"
)

get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/TrajectoryPoint.msg" NAME_WE)
add_custom_target(_autominy_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "autominy_msgs" "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/TrajectoryPoint.msg" "geometry_msgs/Twist:geometry_msgs/Pose:geometry_msgs/Point:geometry_msgs/Vector3:geometry_msgs/Quaternion"
)

get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Obstacle.msg" NAME_WE)
add_custom_target(_autominy_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "autominy_msgs" "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Obstacle.msg" "geometry_msgs/Twist:geometry_msgs/Pose:nav_msgs/Odometry:geometry_msgs/Point:geometry_msgs/Vector3:std_msgs/Header:geometry_msgs/Quaternion:geometry_msgs/PoseWithCovariance:geometry_msgs/TwistWithCovariance"
)

get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Obstacles.msg" NAME_WE)
add_custom_target(_autominy_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "autominy_msgs" "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Obstacles.msg" "geometry_msgs/Twist:geometry_msgs/Pose:nav_msgs/Odometry:geometry_msgs/Point:geometry_msgs/Vector3:autominy_msgs/Obstacle:std_msgs/Header:geometry_msgs/Quaternion:geometry_msgs/PoseWithCovariance:geometry_msgs/TwistWithCovariance"
)

get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Voltage.msg" NAME_WE)
add_custom_target(_autominy_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "autominy_msgs" "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Voltage.msg" "std_msgs/Header"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/NormalizedSpeedCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/autominy_msgs
)
_generate_msg_cpp(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/NormalizedSteeringCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/autominy_msgs
)
_generate_msg_cpp(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Plot.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/autominy_msgs
)
_generate_msg_cpp(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringAngle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/autominy_msgs
)
_generate_msg_cpp(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Speed.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/autominy_msgs
)
_generate_msg_cpp(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SpeedCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/autominy_msgs
)
_generate_msg_cpp(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SpeedPWMCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/autominy_msgs
)
_generate_msg_cpp(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/autominy_msgs
)
_generate_msg_cpp(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringPWMCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/autominy_msgs
)
_generate_msg_cpp(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/autominy_msgs
)
_generate_msg_cpp(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Tick.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/autominy_msgs
)
_generate_msg_cpp(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Trajectory.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg;/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/TrajectoryPoint.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/autominy_msgs
)
_generate_msg_cpp(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/TrajectoryPoint.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/autominy_msgs
)
_generate_msg_cpp(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Obstacle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/nav_msgs/cmake/../msg/Odometry.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/PoseWithCovariance.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/TwistWithCovariance.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/autominy_msgs
)
_generate_msg_cpp(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Obstacles.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/nav_msgs/cmake/../msg/Odometry.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Obstacle.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/PoseWithCovariance.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/TwistWithCovariance.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/autominy_msgs
)
_generate_msg_cpp(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Voltage.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/autominy_msgs
)

### Generating Services

### Generating Module File
_generate_module_cpp(autominy_msgs
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/autominy_msgs
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(autominy_msgs_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(autominy_msgs_generate_messages autominy_msgs_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/NormalizedSpeedCommand.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_cpp _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/NormalizedSteeringCommand.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_cpp _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Plot.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_cpp _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringAngle.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_cpp _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Speed.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_cpp _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SpeedCommand.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_cpp _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SpeedPWMCommand.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_cpp _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringCommand.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_cpp _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringPWMCommand.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_cpp _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringFeedback.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_cpp _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Tick.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_cpp _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Trajectory.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_cpp _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/TrajectoryPoint.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_cpp _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Obstacle.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_cpp _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Obstacles.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_cpp _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Voltage.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_cpp _autominy_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(autominy_msgs_gencpp)
add_dependencies(autominy_msgs_gencpp autominy_msgs_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS autominy_msgs_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/NormalizedSpeedCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/autominy_msgs
)
_generate_msg_eus(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/NormalizedSteeringCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/autominy_msgs
)
_generate_msg_eus(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Plot.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/autominy_msgs
)
_generate_msg_eus(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringAngle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/autominy_msgs
)
_generate_msg_eus(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Speed.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/autominy_msgs
)
_generate_msg_eus(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SpeedCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/autominy_msgs
)
_generate_msg_eus(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SpeedPWMCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/autominy_msgs
)
_generate_msg_eus(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/autominy_msgs
)
_generate_msg_eus(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringPWMCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/autominy_msgs
)
_generate_msg_eus(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/autominy_msgs
)
_generate_msg_eus(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Tick.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/autominy_msgs
)
_generate_msg_eus(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Trajectory.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg;/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/TrajectoryPoint.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/autominy_msgs
)
_generate_msg_eus(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/TrajectoryPoint.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/autominy_msgs
)
_generate_msg_eus(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Obstacle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/nav_msgs/cmake/../msg/Odometry.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/PoseWithCovariance.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/TwistWithCovariance.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/autominy_msgs
)
_generate_msg_eus(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Obstacles.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/nav_msgs/cmake/../msg/Odometry.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Obstacle.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/PoseWithCovariance.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/TwistWithCovariance.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/autominy_msgs
)
_generate_msg_eus(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Voltage.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/autominy_msgs
)

### Generating Services

### Generating Module File
_generate_module_eus(autominy_msgs
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/autominy_msgs
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(autominy_msgs_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(autominy_msgs_generate_messages autominy_msgs_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/NormalizedSpeedCommand.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_eus _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/NormalizedSteeringCommand.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_eus _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Plot.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_eus _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringAngle.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_eus _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Speed.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_eus _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SpeedCommand.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_eus _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SpeedPWMCommand.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_eus _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringCommand.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_eus _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringPWMCommand.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_eus _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringFeedback.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_eus _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Tick.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_eus _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Trajectory.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_eus _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/TrajectoryPoint.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_eus _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Obstacle.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_eus _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Obstacles.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_eus _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Voltage.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_eus _autominy_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(autominy_msgs_geneus)
add_dependencies(autominy_msgs_geneus autominy_msgs_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS autominy_msgs_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/NormalizedSpeedCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/autominy_msgs
)
_generate_msg_lisp(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/NormalizedSteeringCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/autominy_msgs
)
_generate_msg_lisp(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Plot.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/autominy_msgs
)
_generate_msg_lisp(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringAngle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/autominy_msgs
)
_generate_msg_lisp(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Speed.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/autominy_msgs
)
_generate_msg_lisp(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SpeedCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/autominy_msgs
)
_generate_msg_lisp(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SpeedPWMCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/autominy_msgs
)
_generate_msg_lisp(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/autominy_msgs
)
_generate_msg_lisp(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringPWMCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/autominy_msgs
)
_generate_msg_lisp(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/autominy_msgs
)
_generate_msg_lisp(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Tick.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/autominy_msgs
)
_generate_msg_lisp(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Trajectory.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg;/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/TrajectoryPoint.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/autominy_msgs
)
_generate_msg_lisp(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/TrajectoryPoint.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/autominy_msgs
)
_generate_msg_lisp(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Obstacle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/nav_msgs/cmake/../msg/Odometry.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/PoseWithCovariance.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/TwistWithCovariance.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/autominy_msgs
)
_generate_msg_lisp(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Obstacles.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/nav_msgs/cmake/../msg/Odometry.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Obstacle.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/PoseWithCovariance.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/TwistWithCovariance.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/autominy_msgs
)
_generate_msg_lisp(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Voltage.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/autominy_msgs
)

### Generating Services

### Generating Module File
_generate_module_lisp(autominy_msgs
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/autominy_msgs
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(autominy_msgs_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(autominy_msgs_generate_messages autominy_msgs_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/NormalizedSpeedCommand.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_lisp _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/NormalizedSteeringCommand.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_lisp _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Plot.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_lisp _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringAngle.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_lisp _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Speed.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_lisp _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SpeedCommand.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_lisp _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SpeedPWMCommand.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_lisp _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringCommand.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_lisp _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringPWMCommand.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_lisp _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringFeedback.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_lisp _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Tick.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_lisp _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Trajectory.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_lisp _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/TrajectoryPoint.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_lisp _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Obstacle.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_lisp _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Obstacles.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_lisp _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Voltage.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_lisp _autominy_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(autominy_msgs_genlisp)
add_dependencies(autominy_msgs_genlisp autominy_msgs_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS autominy_msgs_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/NormalizedSpeedCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/autominy_msgs
)
_generate_msg_nodejs(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/NormalizedSteeringCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/autominy_msgs
)
_generate_msg_nodejs(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Plot.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/autominy_msgs
)
_generate_msg_nodejs(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringAngle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/autominy_msgs
)
_generate_msg_nodejs(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Speed.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/autominy_msgs
)
_generate_msg_nodejs(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SpeedCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/autominy_msgs
)
_generate_msg_nodejs(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SpeedPWMCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/autominy_msgs
)
_generate_msg_nodejs(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/autominy_msgs
)
_generate_msg_nodejs(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringPWMCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/autominy_msgs
)
_generate_msg_nodejs(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/autominy_msgs
)
_generate_msg_nodejs(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Tick.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/autominy_msgs
)
_generate_msg_nodejs(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Trajectory.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg;/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/TrajectoryPoint.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/autominy_msgs
)
_generate_msg_nodejs(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/TrajectoryPoint.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/autominy_msgs
)
_generate_msg_nodejs(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Obstacle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/nav_msgs/cmake/../msg/Odometry.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/PoseWithCovariance.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/TwistWithCovariance.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/autominy_msgs
)
_generate_msg_nodejs(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Obstacles.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/nav_msgs/cmake/../msg/Odometry.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Obstacle.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/PoseWithCovariance.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/TwistWithCovariance.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/autominy_msgs
)
_generate_msg_nodejs(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Voltage.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/autominy_msgs
)

### Generating Services

### Generating Module File
_generate_module_nodejs(autominy_msgs
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/autominy_msgs
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(autominy_msgs_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(autominy_msgs_generate_messages autominy_msgs_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/NormalizedSpeedCommand.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_nodejs _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/NormalizedSteeringCommand.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_nodejs _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Plot.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_nodejs _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringAngle.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_nodejs _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Speed.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_nodejs _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SpeedCommand.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_nodejs _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SpeedPWMCommand.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_nodejs _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringCommand.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_nodejs _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringPWMCommand.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_nodejs _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringFeedback.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_nodejs _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Tick.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_nodejs _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Trajectory.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_nodejs _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/TrajectoryPoint.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_nodejs _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Obstacle.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_nodejs _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Obstacles.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_nodejs _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Voltage.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_nodejs _autominy_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(autominy_msgs_gennodejs)
add_dependencies(autominy_msgs_gennodejs autominy_msgs_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS autominy_msgs_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/NormalizedSpeedCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/autominy_msgs
)
_generate_msg_py(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/NormalizedSteeringCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/autominy_msgs
)
_generate_msg_py(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Plot.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/autominy_msgs
)
_generate_msg_py(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringAngle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/autominy_msgs
)
_generate_msg_py(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Speed.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/autominy_msgs
)
_generate_msg_py(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SpeedCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/autominy_msgs
)
_generate_msg_py(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SpeedPWMCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/autominy_msgs
)
_generate_msg_py(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/autominy_msgs
)
_generate_msg_py(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringPWMCommand.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/autominy_msgs
)
_generate_msg_py(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringFeedback.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/autominy_msgs
)
_generate_msg_py(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Tick.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/autominy_msgs
)
_generate_msg_py(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Trajectory.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg;/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/TrajectoryPoint.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/autominy_msgs
)
_generate_msg_py(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/TrajectoryPoint.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/autominy_msgs
)
_generate_msg_py(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Obstacle.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/nav_msgs/cmake/../msg/Odometry.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/PoseWithCovariance.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/TwistWithCovariance.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/autominy_msgs
)
_generate_msg_py(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Obstacles.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/noetic/share/nav_msgs/cmake/../msg/Odometry.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Obstacle.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/PoseWithCovariance.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/TwistWithCovariance.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/autominy_msgs
)
_generate_msg_py(autominy_msgs
  "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Voltage.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/autominy_msgs
)

### Generating Services

### Generating Module File
_generate_module_py(autominy_msgs
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/autominy_msgs
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(autominy_msgs_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(autominy_msgs_generate_messages autominy_msgs_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/NormalizedSpeedCommand.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_py _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/NormalizedSteeringCommand.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_py _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Plot.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_py _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringAngle.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_py _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Speed.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_py _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SpeedCommand.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_py _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SpeedPWMCommand.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_py _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringCommand.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_py _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringPWMCommand.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_py _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringFeedback.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_py _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Tick.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_py _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Trajectory.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_py _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/TrajectoryPoint.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_py _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Obstacle.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_py _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Obstacles.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_py _autominy_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Voltage.msg" NAME_WE)
add_dependencies(autominy_msgs_generate_messages_py _autominy_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(autominy_msgs_genpy)
add_dependencies(autominy_msgs_genpy autominy_msgs_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS autominy_msgs_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/autominy_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/autominy_msgs
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(autominy_msgs_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(autominy_msgs_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()
if(TARGET nav_msgs_generate_messages_cpp)
  add_dependencies(autominy_msgs_generate_messages_cpp nav_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/autominy_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/autominy_msgs
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(autominy_msgs_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(autominy_msgs_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()
if(TARGET nav_msgs_generate_messages_eus)
  add_dependencies(autominy_msgs_generate_messages_eus nav_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/autominy_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/autominy_msgs
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(autominy_msgs_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(autominy_msgs_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()
if(TARGET nav_msgs_generate_messages_lisp)
  add_dependencies(autominy_msgs_generate_messages_lisp nav_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/autominy_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/autominy_msgs
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(autominy_msgs_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(autominy_msgs_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()
if(TARGET nav_msgs_generate_messages_nodejs)
  add_dependencies(autominy_msgs_generate_messages_nodejs nav_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/autominy_msgs)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/autominy_msgs\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/autominy_msgs
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(autominy_msgs_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(autominy_msgs_generate_messages_py geometry_msgs_generate_messages_py)
endif()
if(TARGET nav_msgs_generate_messages_py)
  add_dependencies(autominy_msgs_generate_messages_py nav_msgs_generate_messages_py)
endif()
