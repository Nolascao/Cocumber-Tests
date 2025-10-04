# Descrição do Cocumber
O Cucumber é um framework de automação de testes que suporta o desenvolvimento guiado por comportamento (BDD). Sua principal característica é permitir que equipes de desenvolvimento, testadores e stakeholders colaborem na definição de requisitos e comportamentos esperados do software em uma linguagem natural e de fácil compreensão, conhecida como Gherkin.

O Gherkin utiliza uma sintaxe estruturada com palavras-chave como Feature, Scenario, Given, When, Then, And e But para descrever cenários de teste em um formato de "história". Essa abordagem facilita a comunicação e garante que todos os envolvidos no projeto tenham uma compreensão clara do que o software deve fazer, antes mesmo de uma linha de código ser escrita.

A magia do Cucumber reside na sua capacidade de "traduzir" esses cenários escritos em Gherkin para código executável. Cada passo (Given, When, Then) em um cenário Gherkin é mapeado para um método em um arquivo de código, geralmente escrito em linguagens como Java, Ruby, JavaScript, Python, entre outras. Esses métodos, chamados de "step definitions" (definições de passos), contêm a lógica de automação que interage com o sistema sob teste, verifica os resultados e valida o comportamento esperado.

Principais Benefícios do Cucumber:

Colaboração Aprimorada: Promove a comunicação entre equipes técnicas e não técnicas, garantindo que todos estejam alinhados com os requisitos.
Documentação Viva: Os cenários Gherkin servem como documentação executável, sempre atualizada com o comportamento real do sistema.
Reutilização de Código: As step definitions podem ser reutilizadas em múltiplos cenários, reduzindo a duplicação de código de automação.
Foco no Comportamento: Encoraja a equipe a pensar no comportamento do usuário e nos resultados esperados, em vez de apenas na implementação técnica.
Legibilidade: Os testes são escritos em uma linguagem clara e compreensível, facilitando a manutenção e o entendimento por qualquer membro da equipe.
Em resumo, o Cucumber não é apenas uma ferramenta de automação, mas uma metodologia que integra a definição de requisitos, o desenvolvimento e os testes, resultando em software de maior qualidade e com maior alinhamento às expectativas do negócio.

2. Categorização do Framework Cucumber

i) Técnicas de Teste
Classificação: Testes Baseados em Especificação e Testes de Caixa Preta.

- Testes Baseados em Especificação: O Cucumber é o epítome dos testes baseados em especificação. Os cenários Gherkin são, por natureza, especificações de comportamento. Eles descrevem o que o sistema deve fazer sob certas condições, sem se preocupar com a implementação interna. A equipe de desenvolvimento e os stakeholders colaboram para criar essas especificações, que então são transformadas em testes automatizados. O foco está em validar se o software atende aos requisitos definidos.

- Testes de Caixa Preta: Ao descrever o comportamento do sistema através dos cenários Gherkin, o Cucumber interage com o software como um usuário final faria, sem ter conhecimento da estrutura interna do código. As step definitions podem manipular a interface do usuário, chamar APIs ou interagir com o banco de dados, mas a perspectiva do teste é sempre externa, focando nas entradas e saídas do sistema. O testador não precisa saber como o código foi implementado para escrever e executar os testes.

ii) Níveis de Teste
Classificação: Testes de Aceitação e Testes de Sistema.

- Testes de Aceitação: Este é o nível de teste onde o Cucumber brilha mais intensamente. Os cenários Gherkin são frequentemente chamados de "critérios de aceitação executáveis". Eles são escritos do ponto de vista do negócio e do usuário final para verificar se o sistema atende aos requisitos de negócio e se é aceitável para entrega. A linguagem natural do Gherkin facilita a revisão e aprovação desses testes pelos stakeholders, garantindo que o software entregue o valor esperado.

- Testes de Sistema: Embora o foco principal seja a aceitação, o Cucumber também é amplamente utilizado para testes de sistema. Nesses testes, o sistema completo é testado para verificar se ele funciona como um todo, atendendo aos requisitos funcionais e não funcionais. Os cenários Gherkin podem abranger fluxos de trabalho complexos que envolvem múltiplas funcionalidades e componentes do sistema, simulando interações de usuário de ponta a ponta.

iii) Tipos de Teste
Classificação: Testes Funcionais e Testes de Regressão.

- Testes Funcionais: A principal aplicação do Cucumber é a validação da funcionalidade do software. Cada cenário Gherkin descreve uma funcionalidade específica ou um comportamento esperado. As step definitions implementam a lógica para interagir com o sistema e verificar se essa funcionalidade opera corretamente de acordo com a especificação. O Cucumber permite testar se o sistema faz o que foi projetado para fazer.

- Testes de Regressão: Uma vez que os cenários Gherkin e suas step definitions são criados, eles se tornam um conjunto robusto de testes automatizados. Esses testes podem ser executados repetidamente após cada alteração no código (seja uma nova funcionalidade, correção de bug ou refatoração) para garantir que as mudanças não introduziram novos defeitos ou quebraram funcionalidades existentes. A automação proporcionada pelo Cucumber torna os testes de regressão eficientes e confiáveis, garantindo a estabilidade do software ao longo do tempo.
