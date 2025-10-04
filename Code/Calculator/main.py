# main.py
# Arquivo principal que integra tudo

import operacoes as op
import interface as ui

def main():
 while True:
     ui.exibir_menu()
     opcao = ui.obter_opcao()

     if opcao is None:
         continue

     if opcao == 0:
         print("Encerrando a calculadora... Até logo!")
         break

     try:
         if opcao in [1, 2, 3, 4, 5]:
             valor1 = ui.obter_valor("Digite o primeiro número: ")
             if valor1 is None:
                 continue
             valor2 = ui.obter_valor("Digite o segundo número: ")
             if valor2 is None:
                 continue

             if opcao == 1:
                 resultado = op.soma(valor1, valor2)
             elif opcao == 2:
                 resultado = op.subtracao(valor1, valor2)
             elif opcao == 3:
                 resultado = op.multiplicacao(valor1, valor2)
             elif opcao == 4:
                 resultado = op.divisao(valor1, valor2)
             elif opcao == 5:
                 resultado = op.potencia(valor1, valor2)

         elif opcao == 6:
             valor = ui.obter_valor("Digite o número: ")
             if valor is None:
                 continue
             resultado = op.raiz_quadrada(valor)

         else:
             print("Opção inválida! Tente novamente.")
             continue

         print(f"Resultado: {resultado}")

     except ValueError as e:
         print(e)

     input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
 main()