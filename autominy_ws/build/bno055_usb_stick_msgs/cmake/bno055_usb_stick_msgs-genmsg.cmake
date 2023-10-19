# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "bno055_usb_stick_msgs: 3 messages, 0 services")

set(MSG_I_FLAGS "-Ibno055_usb_stick_msgs:/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg;-Igeometry_msgs:/opt/ros/noetic/share/geometry_msgs/cmake/../msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(bno055_usb_stick_msgs_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/CalibrationStatus.msg" NAME_WE)
add_custom_target(_bno055_usb_stick_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "bno055_usb_stick_msgs" "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/CalibrationStatus.msg" ""
)

get_filename_component(_filename "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/EulerAngles.msg" NAME_WE)
add_custom_target(_bno055_usb_stick_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "bno055_usb_stick_msgs" "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/EulerAngles.msg" ""
)

get_filename_component(_filename "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/Output.msg" NAME_WE)
add_custom_target(_bno055_usb_stick_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "bno055_usb_stick_msgs" "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/Output.msg" "bno055_usb_stick_msgs/CalibrationStatus:geometry_msgs/Quaternion:geometry_msgs/Vector3:std_msgs/Header:bno055_usb_stick_msgs/EulerAngles"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(bno055_usb_stick_msgs
  "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/CalibrationStatus.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/bno055_usb_stick_msgs
)
_generate_msg_cpp(bno055_usb_stick_msgs
  "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/EulerAngles.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/bno055_usb_stick_msgs
)
_generate_msg_cpp(bno055_usb_stick_msgs
  "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/Output.msg"
  "${MSG_I_FLAGS}"
  "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/CalibrationStatus.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/EulerAngles.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/bno055_usb_stick_msgs
)

### Generating Services

### Generating Module File
_generate_module_cpp(bno055_usb_stick_msgs
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/bno055_usb_stick_msgs
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(bno055_usb_stick_msgs_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(bno055_usb_stick_msgs_generate_messages bno055_usb_stick_msgs_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/CalibrationStatus.msg" NAME_WE)
add_dependencies(bno055_usb_stick_msgs_generate_messages_cpp _bno055_usb_stick_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/EulerAngles.msg" NAME_WE)
add_dependencies(bno055_usb_stick_msgs_generate_messages_cpp _bno055_usb_stick_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/Output.msg" NAME_WE)
add_dependencies(bno055_usb_stick_msgs_generate_messages_cpp _bno055_usb_stick_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(bno055_usb_stick_msgs_gencpp)
add_dependencies(bno055_usb_stick_msgs_gencpp bno055_usb_stick_msgs_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS bno055_usb_stick_msgs_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(bno055_usb_stick_msgs
  "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/CalibrationStatus.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/bno055_usb_stick_msgs
)
_generate_msg_eus(bno055_usb_stick_msgs
  "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/EulerAngles.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/bno055_usb_stick_msgs
)
_generate_msg_eus(bno055_usb_stick_msgs
  "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/Output.msg"
  "${MSG_I_FLAGS}"
  "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/CalibrationStatus.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/EulerAngles.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/bno055_usb_stick_msgs
)

### Generating Services

### Generating Module File
_generate_module_eus(bno055_usb_stick_msgs
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/bno055_usb_stick_msgs
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(bno055_usb_stick_msgs_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(bno055_usb_stick_msgs_generate_messages bno055_usb_stick_msgs_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/CalibrationStatus.msg" NAME_WE)
add_dependencies(bno055_usb_stick_msgs_generate_messages_eus _bno055_usb_stick_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/EulerAngles.msg" NAME_WE)
add_dependencies(bno055_usb_stick_msgs_generate_messages_eus _bno055_usb_stick_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/Output.msg" NAME_WE)
add_dependencies(bno055_usb_stick_msgs_generate_messages_eus _bno055_usb_stick_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(bno055_usb_stick_msgs_geneus)
add_dependencies(bno055_usb_stick_msgs_geneus bno055_usb_stick_msgs_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS bno055_usb_stick_msgs_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(bno055_usb_stick_msgs
  "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/CalibrationStatus.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/bno055_usb_stick_msgs
)
_generate_msg_lisp(bno055_usb_stick_msgs
  "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/EulerAngles.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/bno055_usb_stick_msgs
)
_generate_msg_lisp(bno055_usb_stick_msgs
  "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/Output.msg"
  "${MSG_I_FLAGS}"
  "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/CalibrationStatus.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/EulerAngles.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/bno055_usb_stick_msgs
)

### Generating Services

### Generating Module File
_generate_module_lisp(bno055_usb_stick_msgs
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/bno055_usb_stick_msgs
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(bno055_usb_stick_msgs_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(bno055_usb_stick_msgs_generate_messages bno055_usb_stick_msgs_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/CalibrationStatus.msg" NAME_WE)
add_dependencies(bno055_usb_stick_msgs_generate_messages_lisp _bno055_usb_stick_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/EulerAngles.msg" NAME_WE)
add_dependencies(bno055_usb_stick_msgs_generate_messages_lisp _bno055_usb_stick_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/Output.msg" NAME_WE)
add_dependencies(bno055_usb_stick_msgs_generate_messages_lisp _bno055_usb_stick_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(bno055_usb_stick_msgs_genlisp)
add_dependencies(bno055_usb_stick_msgs_genlisp bno055_usb_stick_msgs_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS bno055_usb_stick_msgs_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(bno055_usb_stick_msgs
  "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/CalibrationStatus.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/bno055_usb_stick_msgs
)
_generate_msg_nodejs(bno055_usb_stick_msgs
  "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/EulerAngles.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/bno055_usb_stick_msgs
)
_generate_msg_nodejs(bno055_usb_stick_msgs
  "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/Output.msg"
  "${MSG_I_FLAGS}"
  "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/CalibrationStatus.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/EulerAngles.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/bno055_usb_stick_msgs
)

### Generating Services

### Generating Module File
_generate_module_nodejs(bno055_usb_stick_msgs
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/bno055_usb_stick_msgs
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(bno055_usb_stick_msgs_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(bno055_usb_stick_msgs_generate_messages bno055_usb_stick_msgs_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/CalibrationStatus.msg" NAME_WE)
add_dependencies(bno055_usb_stick_msgs_generate_messages_nodejs _bno055_usb_stick_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/EulerAngles.msg" NAME_WE)
add_dependencies(bno055_usb_stick_msgs_generate_messages_nodejs _bno055_usb_stick_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/Output.msg" NAME_WE)
add_dependencies(bno055_usb_stick_msgs_generate_messages_nodejs _bno055_usb_stick_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(bno055_usb_stick_msgs_gennodejs)
add_dependencies(bno055_usb_stick_msgs_gennodejs bno055_usb_stick_msgs_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS bno055_usb_stick_msgs_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(bno055_usb_stick_msgs
  "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/CalibrationStatus.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/bno055_usb_stick_msgs
)
_generate_msg_py(bno055_usb_stick_msgs
  "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/EulerAngles.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/bno055_usb_stick_msgs
)
_generate_msg_py(bno055_usb_stick_msgs
  "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/Output.msg"
  "${MSG_I_FLAGS}"
  "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/CalibrationStatus.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/noetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg;/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/EulerAngles.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/bno055_usb_stick_msgs
)

### Generating Services

### Generating Module File
_generate_module_py(bno055_usb_stick_msgs
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/bno055_usb_stick_msgs
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(bno055_usb_stick_msgs_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(bno055_usb_stick_msgs_generate_messages bno055_usb_stick_msgs_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/CalibrationStatus.msg" NAME_WE)
add_dependencies(bno055_usb_stick_msgs_generate_messages_py _bno055_usb_stick_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/EulerAngles.msg" NAME_WE)
add_dependencies(bno055_usb_stick_msgs_generate_messages_py _bno055_usb_stick_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sherlock2004/Autominy_REAL/autominy_ws/src/bno055_usb_stick_msgs/msg/Output.msg" NAME_WE)
add_dependencies(bno055_usb_stick_msgs_generate_messages_py _bno055_usb_stick_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(bno055_usb_stick_msgs_genpy)
add_dependencies(bno055_usb_stick_msgs_genpy bno055_usb_stick_msgs_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS bno055_usb_stick_msgs_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/bno055_usb_stick_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/bno055_usb_stick_msgs
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(bno055_usb_stick_msgs_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(bno055_usb_stick_msgs_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/bno055_usb_stick_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/bno055_usb_stick_msgs
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(bno055_usb_stick_msgs_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(bno055_usb_stick_msgs_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/bno055_usb_stick_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/bno055_usb_stick_msgs
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(bno055_usb_stick_msgs_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(bno055_usb_stick_msgs_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/bno055_usb_stick_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/bno055_usb_stick_msgs
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(bno055_usb_stick_msgs_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(bno055_usb_stick_msgs_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/bno055_usb_stick_msgs)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/bno055_usb_stick_msgs\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/bno055_usb_stick_msgs
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(bno055_usb_stick_msgs_generate_messages_py geometry_msgs_generate_messages_py)
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(bno055_usb_stick_msgs_generate_messages_py std_msgs_generate_messages_py)
endif()
