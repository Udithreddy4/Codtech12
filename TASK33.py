import cv2
import numpy as np
from PIL import Image, ImageFilter

def apply_cartoon_effect(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.medianBlur(gray, 7)
    edges = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(img, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon

def apply_pencil_sketch(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inv = cv2.bitwise_not(gray)
    blur = cv2.GaussianBlur(inv, (21, 21), 0)
    sketch = cv2.divide(gray, 255 - blur, scale=256)
    return sketch

def apply_oil_painting(image_path):
    img = cv2.imread(image_path)
    oil_painting = cv2.xphoto.oilPainting(img, 7, 1)
    return oil_painting

def apply_sepia(image_path):
    img = cv2.imread(image_path)
    sepia_filter = np.array([[0.272, 0.534, 0.131],
                             [0.349, 0.686, 0.168],
                             [0.393, 0.769, 0.189]])
    sepia = cv2.transform(img, sepia_filter)
    sepia = np.clip(sepia, 0, 255)
    return sepia.astype(np.uint8)

def save_and_show(image, title):
    output_path = f"output_{title}.png"
    cv2.imwrite(output_path, image)
    print(f"{title} saved as {output_path}")
    Image.open(output_path).show()

if __name__ == "__main__":
    image_path = "input.jpg"  # Change to your image file
    cartoon = apply_cartoon_effect(image_path)
    sketch = apply_pencil_sketch(image_path)
    oil_paint = apply_oil_painting(image_path)
    sepia = apply_sepia(image_path)
    
    save_and_show(cartoon, "Cartoon")
    save_and_show(sketch, "Sketch")
    save_and_show(oil_paint, "Oil_Painting")
    save_and_show(sepia, "Sepia")
