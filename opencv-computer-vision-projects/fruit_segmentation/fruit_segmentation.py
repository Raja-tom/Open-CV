"""
Fruit Image Segmentation using OpenCV.

This example segments a red fruit (such as an apple) using HSV thresholding.

Usage:
    python fruit_segmentation.py --input ../images/fruits.jpg
    python fruit_segmentation.py --input ../images/fruits.jpg --output segmented.jpg
"""

import argparse
import os
import cv2


def segment_red_fruit(input_path, output_path=None):
    image = cv2.imread(input_path)
    if image is None:
        raise FileNotFoundError("Could not read input image: {}".format(input_path))

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Red wraps around the HSV hue range, so use two ranges.
    lower_red_1 = (0, 80, 50)
    upper_red_1 = (10, 255, 255)
    lower_red_2 = (170, 80, 50)
    upper_red_2 = (179, 255, 255)

    mask1 = cv2.inRange(hsv, lower_red_1, upper_red_1)
    mask2 = cv2.inRange(hsv, lower_red_2, upper_red_2)
    mask = cv2.bitwise_or(mask1, mask2)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    segmented = cv2.bitwise_and(image, image, mask=mask)

    # Draw contours around detected fruit regions.
    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    result = image.copy()
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 300:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if output_path:
        output_dir = os.path.dirname(output_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        cv2.imwrite(output_path, segmented)

    return mask, segmented, result


def main():
    parser = argparse.ArgumentParser(description="Segment red fruits using OpenCV.")
    parser.add_argument("--input", required=True, help="Path to the input image.")
    parser.add_argument(
        "--output", default="fruit_segmented.jpg", help="Output image path."
    )
    args = parser.parse_args()

    mask, segmented, result = segment_red_fruit(args.input, args.output)

    print("Fruit segmentation completed.")
    print("Segmented image saved to: {}".format(args.output))

    cv2.imshow("Original + Detected Region", result)
    cv2.imshow("Fruit Mask", mask)
    cv2.imshow("Segmented Fruit", segmented)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
