# interface.py
# Módulo responsável pela interface visual no console

def exibir_menu():
 print("=" * 40)
 print("      CALCULADORA PYTHON CONSOLE")
 print("=" * 40)
 print("1 - Soma")
 print("2 - Subtração")
 print("3 - Multiplicação")
 print("4 - Divisão")
 print("5 - Potência")
 print("6 - Raiz Quadrada")
 print("0 - Sair")
 print("=" * 40)

def obter_opcao():
 try:
     opcao = int(input("Escolha uma opção: "))
     return opcao
 except ValueError:
     print("Entrada inválida! Digite um número.")
     return None

def obter_valor(mensagem):
 try:
     return float(input(mensagem))
 except ValueError:
     print("Entrada inválida! Digite um número válido.")
     return None