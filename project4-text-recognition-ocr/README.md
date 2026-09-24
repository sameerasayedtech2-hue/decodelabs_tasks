Text Recognition (OCR) Program

A Python program that extracts text from an image using a pre-trained OCR engine (Tesseract, via pytesseract), instead of training a custom model.

Overview

This project takes an input image containing printed text, pre-processes it to improve readability, runs it through Tesseract OCR, and displays the extracted text along with a confidence score.

Requirements
Python 3.x
Tesseract OCR engine (installed separately, not just the Python wrapper)
Python libraries: pytesseract, opencv-python, pillow
Setup
Install the required Python libraries:
   pip install pytesseract opencv-python pillow
Install the Tesseract OCR engine itself (the Python library only talks to it — it doesn't include it):
Download from: https://github.com/UB-Mannheim/tesseract/wiki
Run the Windows installer
Note the install path (default: C:\Program Files\Tesseract-OCR\)
Point the script to your Tesseract install path by editing this line in ocr_recognizer.py:
python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
Place an image containing clear, printed text in the project folder, named sample.png.
Run the script:
   python ocr_recognizer.py
How It Works

Step 1 — Input: The image is loaded using OpenCV (cv2.imread).

Step 2 — Pre-processing:

The image is converted to grayscale (cv2.cvtColor).
Adaptive thresholding is applied (cv2.adaptiveThreshold) to improve contrast between text and background, which makes the OCR engine's job easier — especially on uneven lighting or backgrounds.

Step 3 — OCR: The pre-processed image is passed to pytesseract.image_to_data(), which returns each recognized word along with its individual confidence score.

Step 4 — Output: The script combines the recognized words into a single string, calculates the average confidence score across all words, and prints the result. It also saves the pre-processed image as processed_output.png for visual confirmation of the pre-processing step.

Meeting the Project Requirements
Requirement	How it's satisfied
Library Integration	pytesseract is used to interface with the Tesseract OCR engine and runs without errors.
Pre-Processing Integrity	The image is converted to grayscale, then adaptive thresholding is applied before OCR runs.
Accuracy Benchmarking	The script calculates an average confidence score across all detected words and checks it against an 80% threshold.
Visual Confirmation	The extracted text and confidence score are printed clearly to the console, and the pre-processed image is saved as a file for visual review.
Sample Output
========================================
OCR TEXT RECOGNITION RESULT
========================================

Extracted Text:
Hello World, this is a sample OCR test image with clear printed text.

Average Confidence Score: 95.0%
Status: PASSED (Confidence >= 80%)

Pre-processed image saved as processed_output.png
Notes
Confidence scores depend heavily on image quality. Clean screenshots of typed text score highest; blurry photos or stylized fonts score lower.
If confidence falls below 80%, try a higher-resolution or higher-contrast image.
On some Windows installations, the Tesseract installer nests the executable inside an extra folder (e.g. Tesseract-OCR\tesseract.exe\tesseract.exe). If you get a "TesseractNotFoundError" even though the file exists, check your actual install path and update tesseract_cmd accordingly.