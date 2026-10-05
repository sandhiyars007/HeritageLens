import pytesseract
import cv2
import numpy as np
from PIL import Image


def extract_text(image):

    try:
        # PIL image -> OpenCV
        img = np.array(image)

        # RGB -> Grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        # Improve contrast
        gray = cv2.equalizeHist(gray)

        # Remove small noise
        gray = cv2.GaussianBlur(gray, (3, 3), 0)

        # Convert to black and white
        _, thresh = cv2.threshold(
            gray,
            0,
            255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )

        # OCR
        text = pytesseract.image_to_string(
            thresh,
            lang="tam+eng",
            config="--psm 6"
        )

        return text.strip()

    except Exception as e:
        return f"OCR Error: {e}"
