# Estratégias de Teste para Derivação dos Casos de Teste

## 1. Introdução

Este documento detalha as estratégias de teste utilizadas para derivar os casos de teste da calculadora usando o framework Cucumber/Behave. Os casos de teste foram desenvolvidos com base em técnicas reconhecidas de engenharia de software para garantir cobertura abrangente e detecção eficaz de defeitos.

## 2. Técnicas de Teste Aplicadas

### 2.1 Particionamento de Equivalência

O particionamento de equivalência divide o domínio de entrada em classes de equivalência, onde cada classe representa um conjunto de valores que devem ser tratados de forma similar pelo sistema.

#### Aplicação na Calculadora:

**Operação de Soma:**
- Classe 1: Números positivos (10 + 5 = 15)
- Classe 2: Números negativos (-10 + -5 = -15)
- Classe 3: Positivo + Negativo (10 + -5 = 5)
- Classe 4: Zero (0 + 0 = 0)

**Operação de Multiplicação:**
- Classe 1: Dois positivos (6 × 7 = 42)
- Classe 2: Positivo × Negativo (-6 × 7 = -42)
- Classe 3: Multiplicação por zero (100 × 0 = 0)

**Operação de Divisão:**
- Classe 1: Divisão exata (10 ÷ 2 = 5)
- Classe 2: Divisão com resultado decimal (10 ÷ 3 ≈ 3.33)
- Classe 3: Divisão com negativo (-10 ÷ 2 = -5)
- Classe 4: Divisão inválida - por zero (exceção esperada)

**Operação de Raiz Quadrada:**
- Classe 1: Números positivos (√16 = 4)
- Classe 2: Zero (√0 = 0)
- Classe 3: Números negativos (√-9 = exceção)

### 2.2 Análise de Valores Limites (Boundary Value Analysis)

Esta técnica foca em testar valores nos limites das classes de equivalência, pois defeitos frequentemente ocorrem nas fronteiras.

#### Aplicação na Calculadora:

**Potenciação - Casos Limite:**
- Expoente zero: 5⁰ = 1 (qualquer número elevado a 0)
- Expoente negativo: 2⁻² = 0.25 (potência com resultado fracionário)
- Base negativa: (-2)³ = -8 (número negativo elevado a ímpar)
- Valor muito pequeno vs muito grande: testado via esquema de cenários

**Divisão - Valores Críticos:**
- Divisão por 1: resultado = dividendo
- Divisão de 0: 0 ÷ 5 = 0
- Divisão por número maior: 1 ÷ 2 = 0.5
- Limite crítico: divisão por zero (exceção)

**Soma - Valores Limites:**
- Soma resultando em zero: -50 + 50 = 0
- Valores próximos a milhar: 999 + 1 = 1000
- Valores mínimos: 1 + 1 = 2

### 2.3 Testes de Exceção (Exception Testing)

Validação de comportamentos excepcionais e tratamento de erros.

#### Casos Implementados:

1. **Divisão por Zero:**
   ```gherkin
   Cenário: Tentativa de divisão por zero
     Quando eu tento dividir 10 por 0
     Então deve ocorrer um erro com a mensagem "Erro: divisão por zero não é permitida."
   ```
   - Valida que o sistema não permite operação matematicamente indefinida
   - Garante mensagem de erro apropriada

2. **Raiz Quadrada de Número Negativo:**
   ```gherkin
   Cenário: Tentativa de raiz quadrada de número negativo
     Quando eu tento calcular a raiz quadrada de -9
     Então deve ocorrer um erro com a mensagem "Erro: não é possível calcular raiz de número negativo."
   ```
   - Valida rejeição de entrada inválida para raiz quadrada real
   - Confirma tratamento adequado de domínio matemático

## 3. Estrutura dos Casos de Teste

### 3.1 Organização em Gherkin

Cada caso de teste segue o padrão BDD (Behavior-Driven Development):

```gherkin
Cenário: [Nome descritivo]
  Dado [Pré-condição]
  Quando [Ação]
  Então [Resultado esperado]
```

### 3.2 Contexto Compartilhado

Uso de `Contexto` (Background) para evitar repetição:

```gherkin
Contexto:
  Dado que a calculadora está pronta para uso
```

Executado antes de cada cenário, garante estado inicial consistente.

## 4. Cobertura de Testes

### 4.1 Cobertura Funcional

| Operação | Casos de Teste | Cobertura |
|----------|---------------|-----------|
| Soma | 8 (3 individuais + 5 outline) | 100% |
| Subtração | 2 | 100% |
| Multiplicação | 8 (3 individuais + 5 outline) | 100% |
| Divisão | 8 (3 individuais + 5 outline) | 100% |
| Potência | 4 | 100% |
| Raiz Quadrada | 3 | 100% |

**Total: 33 cenários de teste**

### 4.2 Cobertura de Condições

- ✓ Entradas válidas (valores positivos, negativos, zero)
- ✓ Entradas inválidas (divisão por zero, raiz de negativo)
- ✓ Valores limites (zero, unitário, decimais)
- ✓ Resultados exatos e aproximados
- ✓ Tratamento de exceções

### 4.3 Tipos de Validação

1. **Validação Exata:** `o resultado deve ser X`
2. **Validação Aproximada:** `o resultado deve ser aproximadamente X` (tolerância de 0.01)
3. **Validação de Exceção:** `deve ocorrer um erro com a mensagem "X"`

## 5. Rastreabilidade

### 5.1 Mapeamento Requisito → Teste

| Requisito | Cenários de Teste |
|-----------|-------------------|
| RF01: Sistema deve realizar soma | Soma de positivos, negativos, misto, zero |
| RF02: Sistema deve realizar subtração | Subtração de positivos, negativos |
| RF03: Sistema deve realizar multiplicação | Multiplicação padrão, com negativo, por zero |
| RF04: Sistema deve realizar divisão | Divisão exata, decimal, com negativo |
| RF05: Sistema deve rejeitar divisão por zero | Tentativa de divisão por zero |
| RF06: Sistema deve realizar potenciação | Potência com expoentes positivo, zero, negativo, base negativa |
| RF07: Sistema deve calcular raiz quadrada | Raiz de positivo, zero |
| RF08: Sistema deve rejeitar raiz de negativo | Tentativa de raiz de negativo |

## 6. Estratégia de Execução

### 6.1 Ordem de Execução

Os testes são executados na ordem definida no arquivo `.feature`:
1. Operações básicas (soma, subtração, multiplicação)
2. Operações com validação de erro (divisão por zero)
3. Operações avançadas (potência, raiz)
4. Casos parametrizados (Scenario Outline)

### 6.2 Critérios de Aceitação

Um teste é considerado bem-sucedido quando:
- ✓ Valores esperados são retornados para entradas válidas
- ✓ Exceções apropriadas são lançadas para entradas inválidas
- ✓ Mensagens de erro são corretas e descritivas
- ✓ Precisão numérica está dentro da tolerância definida

## 7. Manutenção e Extensão

### 7.1 Adicionar Novos Casos

Para adicionar novos casos de teste:
1. Identificar a operação/funcionalidade
2. Definir classes de equivalência
3. Identificar valores limites
4. Escrever cenário Gherkin no arquivo `.feature`
5. Implementar step definition se necessário

### 7.2 Reutilização de Steps

As step definitions foram projetadas para reutilização:
- `@when('eu somo {valor1:f} e {valor2:f}')` - reutilizado em múltiplos cenários
- `@then('o resultado deve ser {esperado:f}')` - validação padrão
- `@then('deve ocorrer um erro com a mensagem "{mensagem}"')` - validação de exceções

## 8. Conclusão

As estratégias aplicadas garantem:
- **Cobertura abrangente** de funcionalidades e casos extremos
- **Detecção eficaz** de defeitos através de testes sistemáticos
- **Manutenibilidade** através de código bem estruturado e reutilizável
- **Rastreabilidade** entre requisitos e casos de teste
- **Comunicação clara** entre equipe técnica e stakeholders via Gherkin

A combinação de particionamento de equivalência, análise de valores limites, testes de exceção e testes parametrizados fornece uma suite de testes robusta e confiável para validação da calculadora.

