#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math

raio = float(input("Digite o raio do círculo em centimetros: "))

area = (raio**2)*math.pi

print(f"A area do raio do seu circulo é {area: .2f}")