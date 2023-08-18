# Install script for directory: /home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/autominy_msgs/msg" TYPE FILE FILES
    "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/NormalizedSpeedCommand.msg"
    "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/NormalizedSteeringCommand.msg"
    "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Plot.msg"
    "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringAngle.msg"
    "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Speed.msg"
    "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SpeedCommand.msg"
    "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SpeedPWMCommand.msg"
    "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringAngle.msg"
    "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringCommand.msg"
    "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringPWMCommand.msg"
    "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/SteeringFeedback.msg"
    "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Tick.msg"
    "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Trajectory.msg"
    "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/TrajectoryPoint.msg"
    "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Obstacle.msg"
    "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Obstacles.msg"
    "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/msg/Voltage.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/autominy_msgs/cmake" TYPE FILE FILES "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/build/autominy_msgs/catkin_generated/installspace/autominy_msgs-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/devel/include/autominy_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/devel/share/roseus/ros/autominy_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/devel/share/common-lisp/ros/autominy_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/devel/share/gennodejs/ros/autominy_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python3" -m compileall "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/devel/lib/python3/dist-packages/autominy_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/devel/lib/python3/dist-packages/autominy_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/build/autominy_msgs/catkin_generated/installspace/autominy_msgs.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/autominy_msgs/cmake" TYPE FILE FILES "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/build/autominy_msgs/catkin_generated/installspace/autominy_msgs-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/autominy_msgs/cmake" TYPE FILE FILES
    "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/build/autominy_msgs/catkin_generated/installspace/autominy_msgsConfig.cmake"
    "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/build/autominy_msgs/catkin_generated/installspace/autominy_msgsConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/autominy_msgs" TYPE FILE FILES "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/autominy_msgs" TYPE DIRECTORY FILES "/home/sherlock2004/dotMEX_Autominy_REAL/autominy_ws/src/autominy_msgs/include/autominy_msgs" FILES_MATCHING REGEX "/[^/]*\\.h$" REGEX "/\\.git$" EXCLUDE)
endif()

