# Projeto de Testes com Cucumber/Behave - Calculadora

## 1. Descrição do Cucumber

O Cucumber é um framework de automação de testes que suporta o desenvolvimento guiado por comportamento (BDD). Sua principal característica é permitir que equipes de desenvolvimento, testadores e stakeholders colaborem na definição de requisitos e comportamentos esperados do software em uma linguagem natural e de fácil compreensão, conhecida como Gherkin.

O Gherkin utiliza uma sintaxe estruturada com palavras-chave como Feature, Scenario, Given, When, Then, And e But para descrever cenários de teste em um formato de "história". Essa abordagem facilita a comunicação e garante que todos os envolvidos no projeto tenham uma compreensão clara do que o software deve fazer, antes mesmo de uma linha de código ser escrita.

A magia do Cucumber reside na sua capacidade de "traduzir" esses cenários escritos em Gherkin para código executável. Cada passo (Given, When, Then) em um cenário Gherkin é mapeado para um método em um arquivo de código, geralmente escrito em linguagens como Java, Ruby, JavaScript, Python, entre outras. Esses métodos, chamados de "step definitions" (definições de passos), contêm a lógica de automação que interage com o sistema sob teste, verifica os resultados e valida o comportamento esperado.

### Principais Benefícios do Cucumber:

- **Colaboração Aprimorada**: Promove a comunicação entre equipes técnicas e não técnicas, garantindo que todos estejam alinhados com os requisitos.
- **Documentação Viva**: Os cenários Gherkin servem como documentação executável, sempre atualizada com o comportamento real do sistema.
- **Reutilização de Código**: As step definitions podem ser reutilizadas em múltiplos cenários, reduzindo a duplicação de código de automação.
- **Foco no Comportamento**: Encoraja a equipe a pensar no comportamento do usuário e nos resultados esperados, em vez de apenas na implementação técnica.
- **Legibilidade**: Os testes são escritos em uma linguagem clara e compreensível, facilitando a manutenção e o entendimento por qualquer membro da equipe.

Em resumo, o Cucumber não é apenas uma ferramenta de automação, mas uma metodologia que integra a definição de requisitos, o desenvolvimento e os testes, resultando em software de maior qualidade e com maior alinhamento às expectativas do negócio.

## 2. Categorização do Framework Cucumber

### i) Técnicas de Teste

**Classificação**: Testes Baseados em Especificação e Testes de Caixa Preta.

- **Testes Baseados em Especificação**: O Cucumber é o epítome dos testes baseados em especificação. Os cenários Gherkin são, por natureza, especificações de comportamento. Eles descrevem o que o sistema deve fazer sob certas condições, sem se preocupar com a implementação interna. A equipe de desenvolvimento e os stakeholders colaboram para criar essas especificações, que então são transformadas em testes automatizados. O foco está em validar se o software atende aos requisitos definidos.

- **Testes de Caixa Preta**: Ao descrever o comportamento do sistema através dos cenários Gherkin, o Cucumber interage com o software como um usuário final faria, sem ter conhecimento da estrutura interna do código. As step definitions podem manipular a interface do usuário, chamar APIs ou interagir com o banco de dados, mas a perspectiva do teste é sempre externa, focando nas entradas e saídas do sistema. O testador não precisa saber como o código foi implementado para escrever e executar os testes.

### ii) Níveis de Teste

**Classificação**: Testes de Aceitação e Testes de Sistema.

- **Testes de Aceitação**: Este é o nível de teste onde o Cucumber brilha mais intensamente. Os cenários Gherkin são frequentemente chamados de "critérios de aceitação executáveis". Eles são escritos do ponto de vista do negócio e do usuário final para verificar se o sistema atende aos requisitos de negócio e se é aceitável para entrega. A linguagem natural do Gherkin facilita a revisão e aprovação desses testes pelos stakeholders, garantindo que o software entregue o valor esperado.

- **Testes de Sistema**: Embora o foco principal seja a aceitação, o Cucumber também é amplamente utilizado para testes de sistema. Nesses testes, o sistema completo é testado para verificar se ele funciona como um todo, atendendo aos requisitos funcionais e não funcionais. Os cenários Gherkin podem abranger fluxos de trabalho complexos que envolvem múltiplas funcionalidades e componentes do sistema, simulando interações de usuário de ponta a ponta.

### iii) Tipos de Teste

**Classificação**: Testes Funcionais e Testes de Regressão.

- **Testes Funcionais**: A principal aplicação do Cucumber é a validação da funcionalidade do software. Cada cenário Gherkin descreve uma funcionalidade específica ou um comportamento esperado. As step definitions implementam a lógica para interagir com o sistema e verificar se essa funcionalidade opera corretamente de acordo com a especificação. O Cucumber permite testar se o sistema faz o que foi projetado para fazer.

- **Testes de Regressão**: Uma vez que os cenários Gherkin e suas step definitions são criados, eles se tornam um conjunto robusto de testes automatizados. Esses testes podem ser executados repetidamente após cada alteração no código (seja uma nova funcionalidade, correção de bug ou refatoração) para garantir que as mudanças não introduziram novos defeitos ou quebraram funcionalidades existentes. A automação proporcionada pelo Cucumber torna os testes de regressão eficientes e confiáveis, garantindo a estabilidade do software ao longo do tempo.

## 3. Instalação e Integração do Framework

### 3.1 Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)
- Sistema operacional: Windows, Linux ou macOS

### 3.2 Instalação do Behave

O Behave é a implementação Python do Cucumber. Para instalar:

#### Opção 1: Instalação via requirements.txt (Recomendado)

```bash
# Clonar ou navegar até o diretório do projeto
cd /caminho/para/Cocumber-Tests

# Instalar dependências
pip install -r requirements.txt
```

#### Opção 2: Instalação manual

```bash
pip install behave==1.2.6
pip install parse==1.20.2
pip install parse-type==0.6.2
```

### 3.3 Verificação da Instalação

```bash
# Verificar se o Behave foi instalado corretamente
behave --version

# Saída esperada: behave 1.2.6
```

### 3.4 Estrutura do Projeto

```
Cocumber-Tests/
├── Code/
│   └── Calculator/
│       ├── operacoes.py        # Módulo com operações matemáticas
│       ├── interface.py        # Módulo de interface (não usado nos testes)
│       └── main.py             # Programa principal da calculadora
├── features/
│   ├── calculadora.feature     # Cenários de teste em Gherkin
│   ├── environment.py          # Configuração de hooks do Behave
│   └── steps/
│       └── calculadora_steps.py # Step definitions
├── behave.ini                  # Configuração do Behave
├── requirements.txt            # Dependências do projeto
├── ESTRATEGIAS_TESTE.md        # Documentação das estratégias de teste
└── README.md                   # Este arquivo
```

## 4. Executando os Testes

### 4.1 Execução Completa

Para executar todos os testes:

```bash
# No diretório raiz do projeto
behave
```

### 4.2 Execução com Relatório Detalhado

```bash
# Formato verboso com mais detalhes
behave -v

# Mostrar cenários que passaram
behave --no-skipped --format pretty
```

### 4.3 Execução de Cenários Específicos

```bash
# Executar apenas cenários de soma
behave --name "soma"

# Executar cenários por linha
behave features/calculadora.feature:10
```

### 4.4 Execução com Tags (se adicionadas)

```bash
# Exemplo se tags forem adicionadas no futuro
behave --tags=@soma
behave --tags=@erro
```

### 4.5 Geração de Relatórios

```bash
# Gerar relatório JUnit (útil para CI/CD)
behave --junit --junit-directory reports/
```

## 5. Interpretando os Resultados

### 5.1 Saída de Sucesso

```
Feature: Calculadora
  Cenário: Soma de dois números positivos
    Dado que a calculadora está pronta para uso ... passed
    Quando eu somo 10 e 5                        ... passed
    Então o resultado deve ser 15                ... passed

1 feature passed, 0 failed, 0 skipped
33 scenarios passed, 0 failed, 0 skipped
99 steps passed, 0 failed, 0 skipped
```

### 5.2 Saída de Falha

```
Feature: Calculadora
  Cenário: Soma de dois números positivos
    Dado que a calculadora está pronta para uso ... passed
    Quando eu somo 10 e 5                        ... passed
    Então o resultado deve ser 16                ... FAILED

Assertion Failed: Esperado 16, mas obteve 15
```

## 6. Estratégias de Teste Aplicadas

Os casos de teste foram derivados usando as seguintes estratégias:

1. **Particionamento de Equivalência**: Divisão de entradas em classes (positivos, negativos, zero)
2. **Análise de Valores Limites**: Testes em fronteiras (zero, expoentes especiais)
3. **Testes de Exceção**: Validação de erros (divisão por zero, raiz de negativo)
4. **Testes Parametrizados**: Uso de Scenario Outline para múltiplas combinações

Para detalhes completos, consulte: `ESTRATEGIAS_TESTE.md`

## 7. Cobertura de Testes

- **Total de Cenários**: 33
- **Operações Testadas**: Soma, Subtração, Multiplicação, Divisão, Potência, Raiz Quadrada
- **Cobertura Funcional**: 100%
- **Testes de Exceção**: 2 (divisão por zero, raiz de negativo)
- **Testes Parametrizados**: 15 (via Scenario Outline)

## 8. Manutenção e Extensão

### 8.1 Adicionando Novos Cenários

Edite `features/calculadora.feature`:

```gherkin
Cenário: Nova operação
  Dado que a calculadora está pronta para uso
  Quando eu executo nova operação com X e Y
  Então o resultado deve ser Z
```

### 8.2 Adicionando Novos Steps

Edite `features/steps/calculadora_steps.py`:

```python
@when('eu executo nova operação com {x:f} e {y:f}')
def step_impl(context, x, y):
    context.resultado = nova_operacao(x, y)
```

## 9. Boas Práticas

1. **Cenários Independentes**: Cada cenário deve ser executável independentemente
2. **Nomes Descritivos**: Use nomes claros que descrevam o comportamento testado
3. **Dado-Quando-Então**: Mantenha a estrutura BDD clara
4. **Reutilização**: Maximize a reutilização de step definitions
5. **Foco no Comportamento**: Teste o "o quê", não o "como"

## 10. Referências

- [Documentação Oficial do Behave](https://behave.readthedocs.io/)
- [Tutorial Gherkin](https://cucumber.io/docs/gherkin/)
- [BDD com Python](https://automationpanda.com/bdd/)
