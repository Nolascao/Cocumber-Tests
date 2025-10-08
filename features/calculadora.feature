# language: pt
Funcionalidade: Calculadora
  Como um usuário da calculadora
  Eu quero realizar operações matemáticas
  Para obter resultados precisos

  Contexto:
    Dado que a calculadora está pronta para uso

  Cenário: Soma de dois números positivos
    Quando eu somo 10 e 5
    Então o resultado deve ser 15

  Cenário: Soma com números negativos
    Quando eu somo -10 e -5
    Então o resultado deve ser -15

  Cenário: Soma de número positivo e negativo
    Quando eu somo 10 e -5
    Então o resultado deve ser 5

  Cenário: Subtração de dois números positivos
    Quando eu subtraio 10 de 5
    Então o resultado deve ser -5

  Cenário: Subtração com números negativos
    Quando eu subtraio -10 de -5
    Então o resultado deve ser 5

  Cenário: Multiplicação de dois números positivos
    Quando eu multiplico 6 por 7
    Então o resultado deve ser 42

  Cenário: Multiplicação com número negativo
    Quando eu multiplico -6 por 7
    Então o resultado deve ser -42

  Cenário: Multiplicação por zero
    Quando eu multiplico 100 por 0
    Então o resultado deve ser 0

  Cenário: Divisão de dois números positivos
    Quando eu divido 10 por 2
    Então o resultado deve ser 5.0

  Cenário: Divisão com resultado decimal
    Quando eu divido 10 por 3
    Então o resultado deve ser aproximadamente 3.33

  Cenário: Divisão de número negativo
    Quando eu divido -10 por 2
    Então o resultado deve ser -5.0

  Cenário: Tentativa de divisão por zero
    Quando eu tento dividir 10 por 0
    Então deve ocorrer um erro com a mensagem "Erro: divisão por zero não é permitida."

  Cenário: Potência de número positivo
    Quando eu calculo 2 elevado a 3
    Então o resultado deve ser 8

  Cenário: Potência com expoente zero
    Quando eu calculo 5 elevado a 0
    Então o resultado deve ser 1

  Cenário: Potência com expoente negativo
    Quando eu calculo 2 elevado a -2
    Então o resultado deve ser 0.25

  Cenário: Potência de base negativa
    Quando eu calculo -2 elevado a 3
    Então o resultado deve ser -8

  Cenário: Raiz quadrada de número positivo
    Quando eu calculo a raiz quadrada de 16
    Então o resultado deve ser 4.0

  Cenário: Raiz quadrada de zero
    Quando eu calculo a raiz quadrada de 0
    Então o resultado deve ser 0.0

  Cenário: Tentativa de raiz quadrada de número negativo
    Quando eu tento calcular a raiz quadrada de -9
    Então deve ocorrer um erro com a mensagem "Erro: não é possível calcular raiz de número negativo."

  Esquema do Cenário: Testes de soma com múltiplos valores
    Quando eu somo <valor1> e <valor2>
    Então o resultado deve ser <resultado>

    Exemplos:
      | valor1 | valor2 | resultado |
      | 0      | 0      | 0         |
      | 1      | 1      | 2         |
      | 100    | 200    | 300       |
      | -50    | 50     | 0         |
      | 999    | 1      | 1000      |

  Esquema do Cenário: Testes de multiplicação com múltiplos valores
    Quando eu multiplico <valor1> por <valor2>
    Então o resultado deve ser <resultado>

    Exemplos:
      | valor1 | valor2 | resultado |
      | 0      | 100    | 0         |
      | 1      | 1      | 1         |
      | 5      | 5      | 25        |
      | -3     | 4      | -12       |
      | 10     | 10     | 100       |

  Esquema do Cenário: Testes de divisão com múltiplos valores
    Quando eu divido <valor1> por <valor2>
    Então o resultado deve ser <resultado>

    Exemplos:
      | valor1 | valor2 | resultado |
      | 10     | 2      | 5.0       |
      | 100    | 4      | 25.0      |
      | 1      | 2      | 0.5       |
      | -20    | 4      | -5.0      |
      | 0      | 5      | 0.0       |

