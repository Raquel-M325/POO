import streamlit as st
import math

class Equacao:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def set_a(self, a):
        if not isinstance(a, int):
            raise ValueError("Não é inteiro")
        return a 
    
    def set_b(self, b):
        if not isinstance(b, int):
            raise ValueError("Não é inteiro")
        return b
    
    def set_c(self, c):
        if not isinstance(c, int):
            raise ValueError("Não é inteiro")
        return c

    def get_a(self):
        return self.a
    
    def get_b(self):
        return self.b
    
    def get_c(self):
        return self.c
    
    def calc_delta(self):
        self.delta = self.b**2 -4 * self.a * self.c
        return self.delta
    
    def calc_y(self, x):
        return self.a * x**2 + self.b * x + self.c

    def calc_bhaskara(self):
        if self.delta < 0:
            raise ValueError("Delta negativo!")

        raiz_delta = math.sqrt(self.delta)
        self.x1 = (-self.b + raiz_delta)/ (2 * self.a)
        self.x2 = (-self.b - raiz_delta) / (2 * self.a)

        return self.x1, self.x2

    def __str__(self):
        return f"Valor a = {self.a} \n Valor b = {self.b} \n Valor c = {self.c}" 