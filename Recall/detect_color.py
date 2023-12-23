#This fuction takes the image-ROS message from Camera and filter it to find the number of pixel of request color.

from __future__ import division
from cv_bridge import CvBridge
import cv2
import numpy as np
import math
import logging

@nrp.MapVariable("red_left",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("red_right",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("blue_left",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("blue_right",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("green_left",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("green_right",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("brown_left", scope = nrp.GLOBAL)
@nrp.MapVariable("brown_right",scope = nrp.GLOBAL)
@nrp.MapVariable("black_left", scope = nrp.GLOBAL)
@nrp.MapVariable("black_right", scope = nrp.GLOBAL)
@nrp.MapVariable("red",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("blue",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("black",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("green",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("brown",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapRobotSubscriber("Camera", Topic("/husky/husky/camera", sensor_msgs.msg.Image))
@nrp.Robot2Neuron()
def detect_color (t,Camera,red_left,red_right,blue_left,blue_right,green_left,green_right,brown_left,brown_right,black_left,black_right,red,blue,black,green,brown):
        
        bridge = CvBridge()
        image = Camera.value
        cv_image = bridge.imgmsg_to_cv2(image,"bgr8")
        hsv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
        
        def detectcolorred(cv_image,hsv_image):
            lower_red = np.array([0, 30, 30])
            upper_red = np.array([0, 255, 255])
            mask_red = cv2.inRange(hsv_image, lower_red, upper_red)
            image_size= (cv_image.shape[0] * cv_image.shape[1])
            if (image_size > 0):
                half = cv_image.shape[1] // 2
                red_left.value = cv2.countNonZero(mask_red[:, :half])
                red_right.value = cv2.countNonZero(mask_red[:, half:])
                red_left.value = 2 * (red_left.value / image_size)
                red_right.value = 2 * (red_right.value / image_size)
                red.value = red_left.value + red_right.value
                return red
                
        
        def detectcolorgreen(cv_image,hsv_image):
            lower_green = np.array([50, 30, 30])
            upper_green = np.array([70, 255, 255])
            mask_green = cv2.inRange(hsv_image, lower_green, upper_green)
            image_size = (cv_image.shape[0] * cv_image.shape[1])
            if (image_size > 0):
                half = cv_image.shape[1] // 2
                green_left.value = cv2.countNonZero(mask_green[:, :half])
                green_right.value = cv2.countNonZero(mask_green[:, half:])
                green_left.value = 2 * (green_left.value / image_size)
                green_right.value = 2 * (green_right.value / image_size)
                green.value = green_left.value + green_right.value
                return green
        
        def detectcolorblue(cv_image,hsv_image):
            lower_blue = np.array([115, 100, 20])
            upper_blue = np.array([125, 255, 255])
            mask_blue = cv2.inRange(hsv_image, lower_blue, upper_blue)
            image_size = (cv_image.shape[0] * cv_image.shape[1])
            if (image_size > 0):
                half = cv_image.shape[1] // 2
                blue_left.value = cv2.countNonZero(mask_blue[:, :half])
                blue_right.value = cv2.countNonZero(mask_blue[:, half:])
                blue_left.value = 2 * (blue_left.value / image_size)
                blue_right.value = 2 * (blue_right.value / image_size)
                blue.value = blue_left.value + blue_right.value
                return blue
            
        def detectcolorbrown(cv_image,hsv_image):
            lower_brown = np.array([10,100, 20])
            upper_brown = np.array([20, 255, 200])
            mask_brown = cv2.inRange(hsv_image, lower_brown, upper_brown)
            image_size = (cv_image.shape[0] * cv_image.shape[1])
            if (image_size > 0):
                half = cv_image.shape[1] // 2
                brown_left.value = cv2.countNonZero(mask_brown[:, :half])
                brown_right.value = cv2.countNonZero(mask_brown[:, half:])
                brown_left.value = 2 * (brown_left.value / image_size)
                brown_right.value = 2 * (brown_right.value / image_size)
                brown.value = brown_left.value + brown_right.value
                return brown
        
        def detectcolorblack(cv_image,hsv_image):
            lower_black = np.array([0,0,0])
            upper_black = np.array([0,0,5])
            mask_black = cv2.inRange(hsv_image, lower_black, upper_black)
            image_size = (cv_image.shape[0] * cv_image.shape[1])
            if (image_size > 0):
                half = cv_image.shape[1] // 2
                black_left.value = cv2.countNonZero(mask_black[:, :half])
                black_right.value = cv2.countNonZero(mask_black[:, half:])
                black_left.value = 2 * (black_left.value / image_size)
                black_right.value = 2 * (black_right.value / image_size)
                black.value = black_left.value + black_right.value
                return black

        blue = detectcolorblue(cv_image,hsv_image)
        red = detectcolorred(cv_image,hsv_image)
        black = detectcolorblack(cv_image,hsv_image)
        green = detectcolorgreen(cv_image,hsv_image)
        brown = detectcolorbrown(cv_image,hsv_image)