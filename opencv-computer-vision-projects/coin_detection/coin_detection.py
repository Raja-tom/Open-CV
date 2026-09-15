"""
Coin Detection and Counting using OpenCV.

Usage:
    python coin_detection.py --input ../images/coins.jpg
    python coin_detection.py --input ../images/coins.jpg --output result.jpg
"""

import cv2
import argparse
import os


def detect_and_count_coins(input_path, output_path="coin_result.jpg"):

    # Read image
    image = cv2.imread(input_path)

    if image is None:
        raise FileNotFoundError(
            "Could not read image: {}".format(input_path)
        )

    # Make a copy for drawing results
    result = image.copy()

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Reduce noise
    gray = cv2.GaussianBlur(gray, (9, 9), 2)

    # Detect circles
    circles = cv2.HoughCircles(
        gray,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=80,
        param1=100,
        param2=50,
        minRadius=50,
        maxRadius=160
    )

    valid_circles = []

    if circles is not None:

        # Convert detected circles to integers
        circles = circles[0]

        for circle in circles:
            x, y, r = circle
            valid_circles.append(
                (int(round(x)), int(round(y)), int(round(r)))
            )

        # Sort biggest circles first
        valid_circles.sort(key=lambda c: c[2], reverse=True)

        filtered = []

        # Remove smaller circles located inside larger coins
        for x, y, r in valid_circles:

            inside_coin = False

            for fx, fy, fr in filtered:

                distance = ((x - fx) ** 2 + (y - fy) ** 2) ** 0.5

                if distance < fr * 0.75 and r < fr * 0.75:
                    inside_coin = True
                    break

            if not inside_coin:
                filtered.append((x, y, r))

        valid_circles = filtered

    # Number of coins
    count = len(valid_circles)

    # Draw detected coins
    for x, y, r in valid_circles:

        cv2.circle(
            result,
            (x, y),
            r,
            (0, 255, 0),
            2
        )

        cv2.circle(
            result,
            (x, y),
            3,
            (0, 0, 255),
            -1
        )

    # Display count
    cv2.putText(
        result,
        "Coins: {}".format(count),
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2,
        cv2.LINE_AA
    )

    # Save result
    output_dir = os.path.dirname(output_path)

    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    cv2.imwrite(output_path, result)

    print("Detected coins: {}".format(count))
    print("Result saved to: {}".format(output_path))

    # Show result
    cv2.imshow("Coin Detection", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():

    parser = argparse.ArgumentParser(
        description="Coin Detection and Counting using OpenCV"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to the coin image"
    )

    parser.add_argument(
        "--output",
        default="coin_result.jpg",
        help="Path to save the result"
    )

    args = parser.parse_args()

    detect_and_count_coins(
        args.input,
        args.output
    )


if __name__ == "__main__":
    main()