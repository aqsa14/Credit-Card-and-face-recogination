from imutils import contours
import numpy as np
import argparse
import cv2

def preprocess_ocra_font_image(ocra_font_image):
    """Converts ocra font image to gray scale and threshold with known range.
    
    Arguments:
        ocra_font_image {numpy.ndarray} -- numpy are of image
    """

    gray = cv2.cvtColor(ocra_font_image, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY_INV)[1]
    return gray
def get_digits_from_contours(image, contrs):
    
    digit_bbox = {}
    for (i,c) in enumerate(contrs):
        (x, y, w, h) = cv2.boundingRect(c)
        
        bounding_box_image = image[y:(y + h), x:(x + w)]
        print (x, y, w, h)
        print (c)
        print image.shape
        print bounding_box_image.shape
        bounding_box_image = cv2.resize(bounding_box_image, (60, 90))
    
        # update the digits dictionary, mapping the digit name to the ROI
        digit_bbox[i] = bounding_box_image
    return digit_bbox


def get_counters(image):
    cnts = cv2.findContours(image.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[1]
    cnts = contours.sort_contours(cnts, method="left-to-right")
    return cnts[0]
def start_credit_card_recognition(card_image,ocra_font_image):
    counters = get_counters(ocra_font_image)

    digit_bboxes = get_digits_from_contours(ocra_font_image, ocra_font_image)
    print digit_bboxes