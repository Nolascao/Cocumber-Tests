# operacoes.py
# Módulo responsável pelas operações matemáticas

def soma(a, b):
 return a + b

def subtracao(a, b):
 return a - b

def multiplicacao(a, b):
 return a * b

def divisao(a, b):
 if b == 0:
     raise ValueError("Erro: divisão por zero não é permitida.")
 return a / b

def potencia(a, b):
 return a ** b

def raiz_quadrada(a):
 if a < 0:
     raise ValueError("Erro: não é possível calcular raiz de número negativo.")
 return a ** 0.5