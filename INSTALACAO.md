# Guia de Instalação - Cucumber/Behave para Calculadora

Este documento fornece instruções detalhadas para instalação e configuração do ambiente de testes.

## Pré-requisitos

Antes de iniciar, certifique-se de ter instalado:

### 1. Python 3.7+

Verifique a versão do Python:
```bash
python3 --version
```

Se não tiver Python instalado:
- **macOS**: `brew install python3`
- **Ubuntu/Debian**: `sudo apt-get install python3 python3-pip`
- **Windows**: Baixe de [python.org](https://www.python.org/downloads/)

### 2. pip (Gerenciador de Pacotes Python)

Geralmente vem instalado com Python 3.4+. Verifique:
```bash
python3 -m pip --version
```

## Instalação Passo a Passo

### Passo 1: Clonar/Obter o Projeto

```bash
# Se usando Git
git clone <url-do-repositorio>
cd Cocumber-Tests

# Ou extrair o arquivo ZIP e navegar até o diretório
cd /caminho/para/Cocumber-Tests
```

### Passo 2: Criar Ambiente Virtual

Ambiente virtual isola as dependências do projeto:

```bash
python3 -m venv venv
```

Isso cria um diretório `venv/` com uma instalação Python isolada.

### Passo 3: Ativar Ambiente Virtual

**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows (Command Prompt):**
```cmd
venv\Scripts\activate.bat
```

**Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

Quando ativado, você verá `(venv)` no início da linha de comando.

### Passo 4: Instalar Dependências

Com o ambiente virtual ativado:

```bash
pip install -r requirements.txt
```

Isso instalará:
- `behave` - Framework BDD (Cucumber para Python)
- `parse` - Biblioteca de parsing
- `parse-type` - Extensões de tipos
- `six` - Compatibilidade Python

### Passo 5: Verificar Instalação

```bash
behave --version
```

Saída esperada: `behave 1.2.6`

## Execução dos Testes

### Método 1: Comando Direto

```bash
# Certifique-se de que o ambiente virtual está ativado
source venv/bin/activate  # macOS/Linux
# ou
venv\Scripts\activate     # Windows

# Execute os testes
behave
```

### Método 2: Script de Execução (macOS/Linux)

Primeiro, torne o script executável:
```bash
chmod +x executar_testes.sh
```

Execute:
```bash
./executar_testes.sh
```

O script automaticamente:
1. Cria ambiente virtual (se não existir)
2. Ativa o ambiente
3. Instala dependências
4. Executa os testes

### Opções de Execução

```bash
# Execução padrão (todos os testes)
behave

# Modo verboso (mais detalhes)
behave -v

# Executar cenário específico por nome
behave --name "Soma"

# Executar cenário específico por linha
behave features/calculadora.feature:10

# Gerar relatório JUnit
behave --junit --junit-directory reports/

# Executar sem captura de stdout (útil para debug)
behave --no-capture

# Parar na primeira falha
behave --stop
```

## Estrutura de Arquivos

Após instalação, a estrutura será:

```
Cocumber-Tests/
├── venv/                          # Ambiente virtual (criado)
├── Code/
│   └── Calculator/
│       ├── operacoes.py          # Código da calculadora
│       ├── interface.py
│       └── main.py
├── features/
│   ├── calculadora.feature       # Cenários de teste
│   ├── environment.py            # Hooks do Behave
│   └── steps/
│       └── calculadora_steps.py  # Step definitions
├── behave.ini                    # Configuração do Behave
├── requirements.txt              # Dependências
├── executar_testes.sh           # Script de execução
├── .gitignore                   # Ignorar arquivos Git
├── INSTALACAO.md                # Este arquivo
├── ESTRATEGIAS_TESTE.md         # Documentação de estratégias
└── README.md                    # Documentação principal
```

## Desativando o Ambiente Virtual

Quando terminar:

```bash
deactivate
```

## Solucionando Problemas

### Problema: "python3: command not found"

**Solução**: Instale Python 3 ou use `python` em vez de `python3`

### Problema: "Permission denied" ao executar script

**Solução**: 
```bash
chmod +x executar_testes.sh
```

### Problema: "No module named 'behave'"

**Solução**: 
1. Ative o ambiente virtual
2. Reinstale dependências: `pip install -r requirements.txt`

### Problema: "externally-managed-environment" no pip

**Solução**: Use ambiente virtual (já coberto neste guia)

### Problema: Testes não encontrados

**Solução**: 
1. Verifique se está no diretório raiz do projeto
2. Confirme que `features/` e `features/steps/` existem
3. Execute: `behave --dry-run` para listar cenários sem executar

### Problema: ImportError ao executar testes

**Solução**: 
Verifique se o diretório `Code/Calculator` existe com os arquivos Python

## Atualizando Dependências

Para atualizar pacotes:

```bash
source venv/bin/activate
pip install --upgrade behave parse parse-type
```

## Removendo o Ambiente

Para remover completamente o ambiente virtual:

```bash
deactivate  # Se estiver ativado
rm -rf venv/
```

Para reinstalar, siga os passos 2-4 novamente.

## Próximos Passos

Após instalação bem-sucedida:

1. Leia `README.md` para visão geral do projeto
2. Consulte `ESTRATEGIAS_TESTE.md` para entender os casos de teste
3. Execute `behave -v` para ver testes em ação
4. Explore `features/calculadora.feature` para ver cenários Gherkin
5. Examine `features/steps/calculadora_steps.py` para entender step definitions

## Suporte

Para problemas adicionais:

1. Verifique logs de erro detalhadamente
2. Consulte documentação oficial do Behave: https://behave.readthedocs.io/
3. Verifique versões de Python e pip

## Checklist de Verificação

- [ ] Python 3.7+ instalado
- [ ] pip instalado e funcional
- [ ] Ambiente virtual criado (`venv/` existe)
- [ ] Ambiente virtual ativado (vê `(venv)` no prompt)
- [ ] Dependências instaladas (`pip list` mostra behave)
- [ ] `behave --version` retorna 1.2.6
- [ ] `behave --dry-run` lista 34 cenários
- [ ] `behave` executa todos os testes com sucesso

Se todos os itens estão marcados, instalação está completa!

