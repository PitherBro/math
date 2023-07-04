#!/bin/python3
from PIL import Image, ImageDraw

class Shape:
    def __init__(self, image_path, border_size):
        self.image_path = image_path
        self.border_size = border_size

    def load_image(self):
        return Image.open(self.image_path)

    def draw_border(self, image):
        width, height = image.size
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 0, width, height), outline="black", width=self.border_size)

    def get_image_size(self):
        with self.load_image() as img:
            return img.size


