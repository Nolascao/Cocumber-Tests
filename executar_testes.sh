#!/bin/bash

# Script para executar testes Behave/Cucumber
# Uso: ./executar_testes.sh [opções]

# Cores para output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  Executando Testes Cucumber/Behave${NC}"
echo -e "${BLUE}========================================${NC}"

# Verificar se o ambiente virtual existe
if [ ! -d "venv" ]; then
    echo -e "${RED}Ambiente virtual não encontrado!${NC}"
    echo -e "${BLUE}Criando ambiente virtual...${NC}"
    python3 -m venv venv
    
    echo -e "${BLUE}Ativando ambiente virtual...${NC}"
    source venv/bin/activate
    
    echo -e "${BLUE}Instalando dependências...${NC}"
    pip install -r requirements.txt
else
    echo -e "${GREEN}Ambiente virtual encontrado!${NC}"
    source venv/bin/activate
fi

echo ""
echo -e "${BLUE}Executando testes...${NC}"
echo ""

# Executar behave com os argumentos passados
if [ $# -eq 0 ]; then
    # Sem argumentos - execução padrão
    behave
else
    # Com argumentos - passar para o behave
    behave "$@"
fi

# Capturar código de saída
EXIT_CODE=$?

echo ""
if [ $EXIT_CODE -eq 0 ]; then
    echo -e "${GREEN}========================================${NC}"
    echo -e "${GREEN}  ✓ Todos os testes passaram!${NC}"
    echo -e "${GREEN}========================================${NC}"
else
    echo -e "${RED}========================================${NC}"
    echo -e "${RED}  ✗ Alguns testes falharam${NC}"
    echo -e "${RED}========================================${NC}"
fi

exit $EXIT_CODE

