# OpenCV Computer Vision Projects

Two beginner-friendly Computer Vision projects implemented with Python and OpenCV:

1. **Coin Detection and Counting**
2. **Fruit Image Segmentation**

The projects use stable OpenCV APIs and avoid OpenCV-contrib dependencies.

## Requirements

- Python 3.9 or newer
- OpenCV
- NumPy

Install dependencies:

```bash
pip install -r requirements.txt
```

For a clean setup, a virtual environment is recommended:

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Project 1: Coin Detection and Counting

### Concept

The program detects circular objects using the **Hough Circle Transform** and counts the detected circles.

Pipeline:

`Input Image -> Grayscale -> Gaussian Blur -> Hough Circle Transform -> Count`

Run:

```bash
python coin_detection/coin_detection.py --input images/coins.jpg
```

Save the result to a specific path:

```bash
python coin_detection/coin_detection.py --input images/coins.jpg --output coin_result.jpg
```

### Important note

Hough Circle detection depends on image quality, coin size, lighting, and overlap. The parameters near the `cv2.HoughCircles()` call can be adjusted for a different image.

## Project 2: Fruit Image Segmentation

### Concept

The program separates red fruit from the background using **HSV color thresholding**.

Pipeline:

`Input Image -> HSV -> Red Color Mask -> Morphological Cleaning -> Segmented Image`

Run:

```bash
python fruit_segmentation/fruit_segmentation.py --input images/fruits.jpg
```

Save the segmented image:

```bash
python fruit_segmentation/fruit_segmentation.py --input images/fruits.jpg --output fruit_segmented.jpg
```

### Important note

The included example targets **red fruits**. For bananas, oranges, green apples, etc., change the HSV ranges in `fruit_segmentation.py`.

## Repository Structure

```text
opencv-computer-vision-projects/
├── coin_detection/
│   ├── coin_detection.py
│   └── README.md
├── fruit_segmentation/
│   ├── fruit_segmentation.py
│   └── README.md
├── images/
│   ├── coins.jpg
│   └── fruits.jpg
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Compatibility

The code intentionally uses long-established OpenCV functions rather than version-specific or contrib-only features.

`requirements.txt` allows OpenCV 4.x while preventing an automatic jump to a future OpenCV 5 API that could require changes.

Because Python and OpenCV support changes over time, compatibility with **every possible version** cannot be guaranteed. Python 3.9+ with a current OpenCV 4.x release is the recommended setup.

## Viva Topics

### Coin Detection
- Image preprocessing
- Grayscale conversion
- Gaussian blur
- Hough Circle Transform
- Object detection
- Object counting

### Fruit Segmentation
- Color spaces
- HSV
- Thresholding
- Binary masks
- Morphological operations
- Contours
- Image segmentation

## License

MIT
