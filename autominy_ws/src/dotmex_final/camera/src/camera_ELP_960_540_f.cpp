#include <ros/ros.h>
#include <sensor_msgs/Image.h>
#include <sensor_msgs/CompressedImage.h>
#include <cv_bridge/cv_bridge.h>
#include <opencv2/opencv.hpp>

int main(int argc, char** argv){
  printf("Nodo camera_ELP_960_540_f inicializado\n");
  ros::init(argc, argv, "camera_ELP_960_540_f");
  ros::NodeHandle nh;
  ros::Publisher image_pub = nh.advertise<sensor_msgs::Image>("/sensors/camera/color/image_raw", 1);
  ros::Publisher comp_image_pub = nh.advertise<sensor_msgs::CompressedImage>("/sensors/camera/color/image_raw/compressed", 1);

  cv::VideoCapture cap(0);
	cap.set(cv::CAP_PROP_FRAME_WIDTH,1920);
	cap.set(cv::CAP_PROP_FRAME_HEIGHT,1080);
  ros::Rate loop_rate(50);
  while (nh.ok()) {
		cv::Mat imagen0;
    cap >> imagen0;
    // Revisa si se adquirio una imagen
    if(imagen0.empty()) {
			ROS_ERROR("Error en la camara");
			break;
		}
		cv::resize(imagen0,imagen0,cv::Size(960,540));
		cv_bridge::CvImage img_bridge;
		sensor_msgs::Image img_msg;
		sensor_msgs::CompressedImage comp_img_msg;
		//imagen normal
		//img_bridge = cv_bridge::CvImage(std_msgs::Header(), "bgr8", imagen0);
		img_bridge = cv_bridge::CvImage(std_msgs::Header(), "rgb8", imagen0);
		img_bridge.toImageMsg(img_msg);      
		// imagen comprimida
		std::vector<int> params = {cv::IMWRITE_JPEG_QUALITY,90};
		cv::imencode(".jpg",imagen0,comp_img_msg.data,params);
		comp_img_msg.format = "jpeg";   
		// publica los mensajes
    image_pub.publish(img_msg);
    comp_image_pub.publish(comp_img_msg);
		loop_rate.sleep();
	}
	cap.release();
	return 0;
}



