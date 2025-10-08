import sys
import os

# Adiciona o diretório Code/Calculator ao path para importar os módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../Code/Calculator'))

from behave import given, when, then, use_step_matcher
import operacoes as op

# Configura o matcher para usar parse com suporte a números
use_step_matcher("parse")

@given('que a calculadora está pronta para uso')
def step_calculadora_pronta(context):
    """
    Inicializa o contexto para os testes da calculadora.
    Prepara o ambiente para armazenar resultados e exceções.
    """
    context.resultado = None
    context.excecao = None

@when('eu somo {valor1:g} e {valor2:g}')
def step_soma(context, valor1, valor2):
    """
    Executa a operação de soma entre dois valores.
    
    Args:
        valor1: Primeiro operando
        valor2: Segundo operando
    """
    context.resultado = op.soma(float(valor1), float(valor2))

@when('eu subtraio {valor2:g} de {valor1:g}')
def step_subtracao(context, valor1, valor2):
    """
    Executa a operação de subtração.
    
    Args:
        valor1: Minuendo
        valor2: Subtraendo
    """
    context.resultado = op.subtracao(float(valor1), float(valor2))

@when('eu multiplico {valor1:g} por {valor2:g}')
def step_multiplicacao(context, valor1, valor2):
    """
    Executa a operação de multiplicação.
    
    Args:
        valor1: Primeiro fator
        valor2: Segundo fator
    """
    context.resultado = op.multiplicacao(float(valor1), float(valor2))

@when('eu divido {valor1:g} por {valor2:g}')
def step_divisao(context, valor1, valor2):
    """
    Executa a operação de divisão.
    
    Args:
        valor1: Dividendo
        valor2: Divisor
    """
    context.resultado = op.divisao(float(valor1), float(valor2))

@when('eu tento dividir {valor1:g} por {valor2:g}')
def step_tenta_divisao(context, valor1, valor2):
    """
    Tenta executar uma divisão que pode gerar exceção.
    Captura a exceção para validação posterior.
    
    Args:
        valor1: Dividendo
        valor2: Divisor
    """
    try:
        context.resultado = op.divisao(float(valor1), float(valor2))
    except ValueError as e:
        context.excecao = str(e)

@when('eu calculo {base:g} elevado a {expoente:g}')
def step_potencia(context, base, expoente):
    """
    Executa a operação de potenciação.
    
    Args:
        base: Base da potência
        expoente: Expoente da potência
    """
    context.resultado = op.potencia(float(base), float(expoente))

@when('eu calculo a raiz quadrada de {valor:g}')
def step_raiz_quadrada(context, valor):
    """
    Executa a operação de raiz quadrada.
    
    Args:
        valor: Valor do qual se deseja calcular a raiz
    """
    context.resultado = op.raiz_quadrada(float(valor))

@when('eu tento calcular a raiz quadrada de {valor:g}')
def step_tenta_raiz_quadrada(context, valor):
    """
    Tenta executar uma raiz quadrada que pode gerar exceção.
    Captura a exceção para validação posterior.
    
    Args:
        valor: Valor do qual se deseja calcular a raiz
    """
    try:
        context.resultado = op.raiz_quadrada(float(valor))
    except ValueError as e:
        context.excecao = str(e)

@then('o resultado deve ser {esperado:g}')
def step_resultado_esperado(context, esperado):
    """
    Valida se o resultado obtido é exatamente igual ao esperado.
    
    Args:
        esperado: Valor esperado do resultado
    """
    assert context.resultado == float(esperado), \
        f"Esperado {esperado}, mas obteve {context.resultado}"

@then('o resultado deve ser aproximadamente {esperado:g}')
def step_resultado_aproximado(context, esperado):
    """
    Valida se o resultado obtido é aproximadamente igual ao esperado.
    Usa tolerância de 0.01 para comparação de valores decimais.
    
    Args:
        esperado: Valor esperado do resultado
    """
    assert abs(context.resultado - float(esperado)) < 0.01, \
        f"Esperado aproximadamente {esperado}, mas obteve {context.resultado}"

@then('deve ocorrer um erro com a mensagem "{mensagem}"')
def step_erro_esperado(context, mensagem):
    """
    Valida se uma exceção foi lançada com a mensagem esperada.
    
    Args:
        mensagem: Mensagem de erro esperada
    """
    assert context.excecao is not None, \
        "Esperava uma exceção, mas nenhuma foi lançada"
    assert context.excecao == mensagem, \
        f"Esperava mensagem '{mensagem}', mas obteve '{context.excecao}'"

