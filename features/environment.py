"""
Arquivo de configuração do ambiente de testes Behave.
Define hooks que são executados antes e depois dos testes.
"""

def before_all(context):
    """
    Executado uma vez antes de todos os testes.
    Configura o ambiente de testes global.
    """
    context.config.setup_logging()
    print("\n" + "="*60)
    print("INICIANDO TESTES DA CALCULADORA COM BEHAVE/CUCUMBER")
    print("="*60)

def after_all(context):
    """
    Executado uma vez após todos os testes.
    Pode ser usado para limpeza de recursos globais.
    """
    print("\n" + "="*60)
    print("TESTES FINALIZADOS")
    print("="*60)

def before_feature(context, feature):
    """
    Executado antes de cada feature.
    
    Args:
        feature: Objeto feature do Behave
    """
    print(f"\n--- Testando Feature: {feature.name} ---")

def before_scenario(context, scenario):
    """
    Executado antes de cada cenário.
    Inicializa variáveis de contexto para cada teste.
    
    Args:
        scenario: Objeto scenario do Behave
    """
    context.resultado = None
    context.excecao = None

def after_scenario(context, scenario):
    """
    Executado após cada cenário.
    Pode ser usado para limpeza ou logging.
    
    Args:
        scenario: Objeto scenario do Behave
    """
    if scenario.status == "failed":
        print(f"FALHA no cenário: {scenario.name}")

