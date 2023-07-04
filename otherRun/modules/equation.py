#!/bin/python3
import random

class Equation:
    def __init__(self, a, b, op):
        self.a = a
        self.b = b
        self.op = op

    def __str__(self):
        return f"{self.a} {self.op} {self.b} = "

    @staticmethod
    def from_string(equation_str):
        a, op, b, _ = equation_str.split()
        return Equation(int(a), int(b), op)

    @staticmethod
    def generate_random_equation(difficulty):
        ops = ['+', '-', '*', '/']
        op = random.choice(ops[:difficulty // 2 + 1])
        if op in ['+', '-']:
            a = random.randint(0, 20 - difficulty)
            b = random.randint(0, 20 - difficulty)
        else:
            a = random.randint(1, 10 - (difficulty // 2))
            b = random.randint(1, 10 - (difficulty // 2))
        return Equation(a, b, op)

