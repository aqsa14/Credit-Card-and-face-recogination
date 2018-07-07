import argparse
import cv2
from credit_card import start_credit_card_recognition, preprocess_ocra_font_image
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--card_image", type=str, default="resources/images/card-image.jpeg")
    parser.add_argument("-r","--ocra_image", type=str, default="resources/images/ocra-image.png")
    
    args = parser.parse_args()
    return args

def show_image(image,wait,name = "Image"):
    cv2.imshow(name, image)
    if wait:
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def main():
    args = get_args()
    card_image = cv2.imread(args.card_image)
    ocra_image = cv2.imread(args.ocra_image)

    ocra_image = preprocess_ocra_font_image(ocra_image)
    start_credit_card_recognition(card_image,ocra_image)
    show_image(card_image,False, "Card")
    show_image(ocra_image,True, "OCR-A Digits")


if __name__ == '__main__':
    main()