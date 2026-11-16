## 1 Introdução e instruções de entrega

O Projeto Integrado Inovação apresenta a Clínica Vida+, situada na cidade fictícia de São Lucas. A proposta integra planejamento ágil, programação Python, lógica proposicional, filas e modelagem de casos de uso. A solução inicial organiza cadastros e fundamenta os demais módulos de gestão clínica.

Fonte principal: PROJETO_INTEGRADO_INOVACAO_ADS_2025.2.pdf, páginas 2 a 7. A entrega é individual, obrigatoriamente em Word, com capa e folha de rosto conforme o modelo institucional do AVA. O enunciado proíbe entrega em PDF. O PDF deste pacote serve apenas para consulta. O prazo deve ser conferido no AVA; o enunciado não define aqui uma data nem um limite numérico de páginas.

O modelo oficial do AVA não foi fornecido. Aplicou-se uma base acadêmica em A4, Arial 12, espaçamento 1,5 e margens superior/esquerda de 3 cm e inferior/direita de 2 cm. Isso não equivale a uma confirmação de aderência ao template específico.

## 2 Planejamento Scrum e evidências

Criar no Trello o quadro Desenvolvimento de uma Plataforma de Saúde - Luis Carlos Silva Rodrigues. Listas obrigatórias: Backlog, Sprint Atual, Em Progresso e Concluído. O arquivo vida_backlog.csv fornece cartões para cadastro manual. A duração proposta é de uma semana por sprint, ajustável ao calendário real do AVA.

Sprint | Objetivo | Itens e aceite
1 | Cadastro e estatísticas | Cadastrar nome, idade e telefone; listar; calcular total, média e extremos.
2 | Busca e robustez | Buscar por nome sem distinguir maiúsculas; tratar entradas inválidas; manter menu até sair.
3 | Modelagem e revisão | Concluir tabelas lógicas, fila, casos de uso e conferir o relatório.

Para cada cartão: registrar descrição, critério de aceite, checklist, prazo e observações. Mover para Sprint Atual ao selecionar o trabalho, Em Progresso ao iniciar e Concluído somente após verificar o aceite. Registrar capturas reais antes, durante e ao final da execução.

Relatório de cada sprint a preencher com a execução real: período; objetivo; cartões planejados; cartões concluídos com evidências; obstáculos; resultado dos testes; melhoria para a próxima sprint. Nenhuma sprint foi declarada executada no Trello nesta versão. O quadro de gestão individual adapta os conceitos de Scrum ao exercício e não representa, por si só, uma equipe Scrum completa.

## 3 Programa Python e verificação

O arquivo vida_plus/main.py implementa cadastro de pacientes com listas de dicionários, menu com cinco opções, estatísticas, busca e listagem. O cadastro rejeita nomes vazios, idades fora de 0 a 130 e telefones sem 10 ou 11 dígitos. O limite etário e a regra de telefone são decisões do protótipo e podem ser ajustados. A idade média é calculada por soma das idades dividida pelo total; em lista vazia, não há divisão.

A busca usa correspondência parcial, sem distinguir maiúsculas e minúsculas. Em empate de idade mínima ou máxima, todos os pacientes correspondentes são exibidos. Os dados permanecem apenas na memória e são perdidos ao encerrar: persistência não é requisito do Passo 2. O protótipo não implementa prontuário, agendamento ou autenticação.

Executar no VS Code com Python 3: python vida_plus/main.py. Executar as verificações: python -m unittest discover -s tests -v. Para capturas de execução, usar somente dados fictícios, sem documentos, telefones ou informações médicas reais. O arquivo VALIDACAO.txt registra o resultado efetivamente obtido.

## 4 Lógica proposicional

A representa agendamento; B, documentos em dia; C, disponibilidade médica; D, pagamentos em dia. Consulta normal: (A ∧ B ∧ C) ∨ (B ∧ C ∧ D). Pela distributividade, equivale a B ∧ C ∧ (A ∨ D). Emergência: C ∧ (B ∨ D). A regra não exige negação; inserir NOT artificialmente alteraria ou complicaria desnecessariamente a expressão.

A | B | C | D | Normal | Emergência
F | F | F | F | F | F
F | F | F | V | F | F
F | F | V | F | F | F
F | F | V | V | F | V
F | V | F | F | F | F
F | V | F | V | F | F
F | V | V | F | F | V
F | V | V | V | V | V
V | F | F | F | F | F
V | F | F | V | F | F
V | F | V | F | F | F
V | F | V | V | F | V
V | V | F | F | F | F
V | V | F | V | F | F
V | V | V | F | V | V
V | V | V | V | V | V

Consulta normal permite atendimento em 3 das 16 combinações. Emergência permite atendimento em 6 das 16. Para A=F, B=V, C=V e D=F: consulta normal é falsa e emergência é verdadeira. A tabela conjunta contém as 16 linhas completas de cada modalidade; as colunas podem ser separadas no template se necessário.

Essas condições reproduzem apenas o exercício de lógica apresentado no PDF; não devem ser tomadas como regras reais para atendimento em serviços de saúde.

## 5 Fila e casos de uso

Pseudocódigo FIFO solicitado:
INÍCIO
  fila ← lista vazia
  PARA i DE 1 ATÉ 3 FAÇA
    LEIA nome, cpf
    INSIRA_NO_FINAL(fila, {nome, cpf})
  FIM PARA
  atendido ← REMOVA_DO_INÍCIO(fila)
  ESCREVA atendido.nome
  PARA CADA paciente EM fila FAÇA
    ESCREVA paciente.nome, paciente.cpf
  FIM PARA
FIM

A ordem de saída é a mesma da chegada. Após inserir Ana, Bruno e Carla, o primeiro atendimento remove Ana; permanecem Bruno e Carla. Os nomes são exemplos fictícios. O CPF deve ser tratado como texto para preservar zeros à esquerda.

Atores do sistema de consultas: Secretária e Médico. A secretária participa de Cadastrar paciente, Agendar consulta, Confirmar consulta e Cancelar consulta. O médico participa de Cancelar consulta e Gerar receita. Gerar receita inclui obrigatoriamente Imprimir receita, com relação «include» direcionada de Gerar receita para Imprimir receita.

Agendar e Confirmar têm como pré-condição o paciente estar cadastrado. Não se deve modelar «include» para Cadastrar paciente, porque um paciente já cadastrado não precisa ser recadastrado em toda consulta. Opcionalmente, Agendar e Confirmar incluem Verificar cadastro para tornar a verificação explícita. O arquivo casos_uso.puml contém o diagrama UML editável. O paciente é entidade do domínio, sem interação direta com a aplicação descrita no enunciado.

## 6 Diagrama de casos de uso

Figura disponível no documento consolidado.

Figura autoral elaborada a partir do Passo 5. A direção de cada relação include parte do caso base e aponta para o comportamento incluído.

## 7 Conclusão e pendências

A solução articula organização do trabalho, estruturas de dados e representação formal de regras. O programa cobre o escopo introdutório de cadastro e consulta; tabelas e modelagem documentam as regras solicitadas. Uma evolução futura poderá incluir armazenamento persistente e módulos clínicos, sem confundir propostas futuras com funcionalidades já construídas.

Antes da postagem: aplicar o Modelo do AVA; incluir prints reais do Trello e os relatórios reais de cada sprint; renderizar e conferir o Word no editor disponível; confirmar prazo e disciplina. Esta versão é material revisado para complementação e não deve ser apresentada como entrega integral já comprovada.

## Referências

ANHANGUERA. Projeto Integrado Inovação Análise e Desenvolvimento de Sistemas. Arquivo PROJETO_INTEGRADO_INOVACAO_ADS_2025.2.pdf. Material fornecido, sem data editorial confirmada.

SCHWABER, Ken; SUTHERLAND, Jeff. The Scrum Guide. 2020. Disponível em: https://scrumguides.org/scrum-guide.html . Acesso em: 16 nov. 2026.

PYTHON SOFTWARE FOUNDATION. Python 3 Documentation. Disponível em: https://docs.python.org/3/ . Referência complementar para listas, dicionários e execução do projeto.
