#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <opencv2/highgui/highgui.hpp>
#include <cv_bridge/cv_bridge.h>

int main(int argc, char** argv){
  printf("Nodo camera_ELP_960_540 inicializado\n");
  ros::init(argc, argv, "camera_ELP_960_540");
  ros::NodeHandle nh;
  image_transport::ImageTransport it(nh);
	//it.setTransport("raw");
  image_transport::Publisher pub = it.advertise("/sensors/camera/color/image_raw", 1);

  cv::VideoCapture cap(0);
  cv::Mat frame;
	sensor_msgs::ImagePtr msg;
	cap.set(cv::CAP_PROP_FRAME_WIDTH,960);
	cap.set(cv::CAP_PROP_FRAME_HEIGHT,540);

  ros::Rate loop_rate(30);
  while (nh.ok()) {


    cap >> frame;
    // Check if grabbed frame is actually full with some content
    if(!frame.empty()) {
      msg = cv_bridge::CvImage(std_msgs::Header(), "bgr8", frame).toImageMsg();
      pub.publish(msg);
      cv::waitKey(1);
    }
		
    ros::spinOnce();
    loop_rate.sleep();
  }
}



