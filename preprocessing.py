from PIL import Image, ImageEnhance, ImageFilter

def preprocess_image(image):

    image = image.convert("L")

    image = ImageEnhance.Contrast(image).enhance(2)

    image = image.filter(ImageFilter.SHARPEN)

    return image
