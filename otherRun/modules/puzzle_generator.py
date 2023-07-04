#!/bin/python3
import random
from equation import Equation
from shape import Shape
from PIL import Image, ImageDraw, ImageFont

class PuzzleGenerator:
    def __init__(self, shape, complexity, difficulty):
        self.shape = shape
        self.complexity = complexity
        self.difficulty = difficulty

    def generate_puzzle(self):
        equations = [Equation.generate_random_equation(self.difficulty) for _ in range(self.complexity)]
        image = self.shape.load_image()
        self.shape.draw_border(image)
        self.layout_equations(image, equations)
        return image

    def layout_equations(self, image, equations):
        font_size = self.calculate_font_size(image)
        font = ImageFont.truetype('arial.ttf', font_size)
        draw = ImageDraw.Draw(image)
        for eq in equations:
            eq_str = str(eq)
            width, height = draw.textsize(eq_str, font=font)
            x = random.randint(0, self.shape.get_image_size()[0] - width)
            y = random.randint(0, self.shape.get_image_size()[1] - height)
            draw.text((x, y), eq_str, font=font, fill="black")

    def calculate_font_size(self, image):
        # For simplicity, just hard-code the font size for now
        return 24

