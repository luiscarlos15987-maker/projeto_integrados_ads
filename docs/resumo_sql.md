## 1 Visão geral e plano de estudo

O roteiro de Programação e Desenvolvimento de Banco de Dados contém 22 páginas e organiza a revisão em quatro unidades: estrutura de repositórios; manipulação de dados e estruturas; consultas avançadas; e recursos avançados. Trata-se de material de estudo e não de um terceiro enunciado de projeto integrado. Os dois PDFs curtos de articulação teórico-prática são páginas de acesso aos projetos e não acrescentam tarefas às propostas completas.

Plano sugerido de quatro sessões: criar tabelas e relacionamentos; manipular dados e validar restrições; consultar com JOIN e agregações; revisar transações, rotinas, permissões e recuperação. Em cada sessão, executar exemplos em banco de laboratório, conferir o resultado e escrever uma explicação própria.

## 2 Unidades 1 e 2

Unidade 1: tabelas representam entidades, colunas definem atributos e linhas representam registros. CREATE DATABASE e CREATE TABLE definem estruturas; SELECT, FROM e WHERE consultam dados. PRIMARY KEY identifica registros, enquanto FOREIGN KEY expressa relações. Preferir utf8mb4 para compatibilidade ampla de caracteres no MySQL.

Unidade 2: INSERT adiciona linhas; UPDATE altera valores; DELETE remove linhas. ALTER TABLE modifica a estrutura. NOT NULL impede ausência de valor; UNIQUE restringe duplicidade dos valores não nulos; FOREIGN KEY preserva referências válidas. DROP TABLE remove a tabela e seus dados.

Revisão técnica: ON DELETE CASCADE refere-se à exclusão de linhas relacionadas, e não à remoção automática de tabelas dependentes por DROP TABLE. NULL é tratado com IS NULL ou IS NOT NULL, não com igualdade. WHERE em UPDATE e DELETE delimita o conjunto afetado e deve ser conferido antes da execução.

## 3 Unidade 3 e esclarecimentos

INNER JOIN retorna combinações com correspondência; LEFT JOIN preserva todas as linhas da tabela esquerda; RIGHT JOIN preserva as da direita. Uma relação de um para muitos pode multiplicar linhas no resultado; isso afeta contagens e precisa ser considerado antes de agregar.

COUNT(*) conta linhas, inclusive aquelas com colunas nulas; COUNT(coluna) conta valores não nulos daquela coluna; COUNT(DISTINCT coluna) conta valores distintos não nulos. Assim, a frase do roteiro de que COUNT(*) conta todas as colunas deve ser corrigida para todas as linhas. SUM e AVG resumem valores; MIN e MAX identificam extremos. WHERE filtra antes do agrupamento e HAVING filtra grupos.

Subconsultas permitem usar o resultado de uma consulta dentro de outra, mas não são automaticamente mais rápidas: o desempenho depende do plano de execução. Views armazenam definições de consulta e facilitam abstração; uma view comum não é, por si só, garantia de ganho de desempenho. Índices auxiliam buscas, porém consomem armazenamento e aumentam o custo de escrita.

## 4 Unidade 4 e esclarecimentos

COMMIT confirma a transação; ROLLBACK reverte alterações ainda não confirmadas; SAVEPOINT cria um ponto para reversão parcial. No MySQL, vários comandos DDL provocam commit implícito. Não presumir que um ROLLBACK desfará CREATE TABLE ou ALTER TABLE.

Procedures podem produzir conjuntos de resultados e utilizar parâmetros OUT e INOUT; portanto, não é preciso dizer que nunca retornam informações. Funções armazenadas retornam um valor e possuem restrições próprias. CREATE ROLE cria papéis e DROP ROLE remove papéis no MySQL; o comando Destroy Role citado pelo roteiro não corresponde à sintaxe MySQL.

GRANT concede privilégios e REVOKE os retira. Aplicar menor privilégio e contas individuais. RAID 1 espelha discos e pode tolerar a falha de um deles; não substitui backup, pois exclusões e corrupção podem atingir as duas cópias. Recuperação deve ser testada com cópias separadas.

## 5 Exercício de fixação e referências

O arquivo sql/revisao_mysql.sql cria um pequeno banco de laboratório, insere produtos e categorias e demonstra JOIN, contagens, agregação e transação. Não foi executado em um servidor MySQL nesta sessão; as saídas comentadas são expectativas para conferência local.

Perguntas para revisão: por que COUNT(*) e COUNT(preco) podem divergir? Qual lado um LEFT JOIN preserva? Qual a diferença entre DELETE e DROP TABLE? Por que RAID não recupera um arquivo apagado? Quando uma procedure pode devolver dados?

Respostas: valores NULL podem ser ignorados por COUNT(preco); LEFT JOIN preserva a tabela à esquerda; DELETE atua em linhas e DROP remove a tabela; o espelhamento replica também alterações indesejadas; procedures podem fornecer resultados e parâmetros OUT/INOUT.

ANHANGUERA. Programação e Desenvolvimento de Banco de Dados. Revisão das unidades. Roteiro de estudos, 22 p. Arquivo fornecido: 053b8325-ae93-41c0-8dba-43a276c6a478-KRT-f3ae9a4c-a4c6-4d74-9d1d-ecb380e3f42a.pdf.

ORACLE. MySQL 8.4 Reference Manual. Disponível em: https://dev.mysql.com/doc/refman/8.4/en/ . Consultar aggregate-functions.html, drop-role.html, create-procedure.html e implicit-commit.html. Acesso em: 16 nov. 2026.
