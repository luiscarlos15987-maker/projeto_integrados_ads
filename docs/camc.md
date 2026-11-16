## 1 Introdução e instruções de entrega

O Projeto Integrado Síntese analisa a CAMC, startup familiar que produz mel, chia e uma barra energética. Os registros de produção, estoque, finanças, atendimento e feedback estão fragmentados. Propõe-se integração por um CRM associado a registros rastreáveis de lotes e pedidos, com segurança, comunicação entre unidades e interface de avaliação simples.

Fonte principal: PROJETO_INTEGRADO_SINTESE_–_ANALISE_E_DESENVOLVIMENTO_DE_SISTEMAS.pdf, páginas 3 a 8. A entrega final é individual, no Modelo disponível no AVA, em um único Word ou PDF de até 10 MB. Os passos 2 a 5 pedem documentos PDF; para cumprir também a regra final de arquivo único, reunir essas seções no PDF consolidado. Não há limite explícito de páginas neste enunciado.

Critérios: clareza e coesão 10%; aplicação interdisciplinar 50%; riqueza de argumentação 20%; organização 10%; normalização 10%. O material informa aprovação com pelo menos 60 de 100 pontos. O Modelo oficial do AVA e o print real do backlog permanecem pendentes.

## 2 Backlog do CRM

O Product Backlog deve centralizar solicitações de WhatsApp, e-mail e telefone, relacionando atendimento, histórico e contexto de pedidos. A integração automática com esses canais é uma evolução proposta; o MVP admite registro manual do canal para evitar prometer integrações externas não implementadas.

ID | Funcionalidade | Critério de aceite
CRM01 | Cadastro de clientes | Validar nome e contato; pesquisar antes de criar duplicidade.
CRM02 | Histórico unificado | Exibir tickets e pedidos do cliente em ordem cronológica.
CRM03 | Tickets de atendimento | Criar protocolo com canal, categoria, descrição e responsável.
CRM04 | Status e acompanhamento | Registrar Aberto, Em atendimento, Aguardando cliente e Resolvido; preservar histórico.
CRM05 | Associação a pedidos e lotes | Vincular reclamação ao pedido e lote; permitir pesquisa rastreável.
CRM06 | Avaliação de produto | Registrar nota de 1 a 5 e comentário opcional após entrega.
CRM07 | Indicadores | Apurar tempo de resolução, volume por canal e nota média com período.
CRM08 | Permissões e auditoria | Bloquear acesso incompatível com papel e registrar alterações críticas.

Prioridade inicial: CRM01, CRM03, CRM04 e CRM08; depois histórico, rastreabilidade, avaliação e indicadores. Registrar os itens na ferramenta com os critérios acima e capturar o backlog real. camc_backlog.csv oferece os dados dos cartões. Autoavaliação a completar pelo estudante: explicar como priorizou, qual dificuldade real encontrou e o que aprendeu.

## 3 Plano de segurança e auditoria

Aplicar contas individuais, menor privilégio, autenticação multifator para administradores e acesso remoto, revisão trimestral de permissões e desligamento imediato de contas sem necessidade. Criptografar a comunicação e as cópias de segurança; manter chaves e credenciais fora do código. Os períodos abaixo são parâmetros propostos, sujeitos à validação operacional.

Papel | Acesso permitido | Limite
Produção | Criar registros de colheita e lotes | Sem alterar registros financeiros.
Estoque e logística | Movimentações, pedidos e rastreio | Sem aprovar o próprio ajuste crítico.
Atendimento | Contatos, tickets e feedback | Sem editar volumes colhidos ou finanças.
Financeiro | Lançamentos e conciliação | Sem apagar trilhas de auditoria.
Gestão e auditoria | Relatórios e leitura dos logs | Aprovar ajustes; sem edição dos logs.
Administrador técnico | Infraestrutura e recuperação | Acesso excepcional aos dados registrado e justificado.

Backup proposto: cópia completa diária e registros transacionais horários; três cópias em dois meios, uma externa e uma isolada ou imutável. Retenção inicial: diários por 30 dias e mensais por 12 meses. Metas de RPO de uma hora e RTO de quatro horas, a validar em restauração mensal documentada.

Auditoria: registrar ator, horário sincronizado, operação, lote ou pedido, valores anteriores e novos e justificativa. Excluir senhas e dados completos de pagamento dos logs. Encaminhar eventos a repositório separado, com escrita restrita, retenção imutável e alertas para exclusões e ajustes críticos.

Fraudes internas: separar solicitação e aprovação de ajustes; reconciliar colheita, estoque, insumos e vendas; exigir justificativa e dupla aprovação de correções críticas. Hashes ajudam a detectar alterações quando o histórico é protegido e ancorado externamente. Autoavaliação pendente: justificar um controle para um risco concreto.

## 4 Plano de redes de computadores

Adotar topologia física em estrela em cada unidade: estações, servidor e pontos de acesso conectados a switch gerenciável; o switch se conecta a firewall e roteador de borda. Laboratório e fábrica comunicam-se logicamente por VPN site a site autenticada. Como o enunciado não informa distância, visada ou disponibilidade de fibra, a escolha final do enlace depende de levantamento local.

Para unidades próximas no mesmo terreno, avaliar fibra óptica entre prédios; para unidades distantes, contratar acesso à internet em cada local e estabelecer VPN. Um segundo enlace de operadora distinta, quando viável, reduz indisponibilidade por falha de conectividade. A aplicação deve operar com TLS mesmo dentro da VPN.

Elemento | Proposta | Finalidade
Borda | Dois firewalls com VPN, um por local | Filtragem e túnel entre unidades.
Acesso | Dois switches gerenciáveis gigabit | Conectar equipamentos e separar VLANs.
Rede sem fio | Pontos de acesso com rede de visitantes separada | Mobilidade sem acesso à produção.
Segmentação | VLAN 10 gestão; 20 servidores; 30 operação; 40 visitantes | Conter acessos e movimento lateral.
Infraestrutura | Cat6, rack, patch panel, nobreak e fibra quando aplicável | Organização física e continuidade.

Endereçamento proposto: laboratório 10.10.VLAN.0/24 e fábrica 10.20.VLAN.0/24, substituindo VLAN por 10, 20, 30 ou 40. Redes distintas evitam sobreposição na VPN. Permitir somente origens, destinos e portas necessários; banco de dados acessível apenas pelo servidor de aplicação. Visitantes não alcançam redes internas. Monitorar perda, latência, disponibilidade e falhas do túnel.

Validação proposta: testar isolamento entre VLANs, comunicação aplicação-banco, queda do enlace, recuperação e alimentação do nobreak. Autoavaliação pendente: justificar a topologia e o compromisso entre custo e disponibilidade a partir das condições reais ou das premissas adotadas.

## 5 Wireframe e usabilidade

Fluxo proposto após o pedido ser entregue: 1) tocar em Avaliar produto no pedido entregue; 2) tocar na nota de 1 a 5; 3) tocar em Enviar avaliação. O comentário fica visível na mesma tela e é opcional. Digitar comentário adiciona ações, portanto a meta de três cliques vale para registrar a nota sem texto. Não inserir uma tela adicional de confirmação.

Tela de avaliação | Conteúdo e comportamento
Cabeçalho | Avalie sua barra Mel e Chia; contexto do pedido entregue.
Pergunta | Como foi sua experiência com o produto?
Nota | Botões 1, 2, 3, 4 e 5 com rótulos acessíveis de ruim a excelente.
Comentário | Campo opcional com limite proposto de 500 caracteres.
Enviar | Habilitado após selecionar nota; impedir envio duplicado.
Retorno | Mensagem Avaliação enviada na própria tela.

O wireframe navegável encontra-se em camc/wireframe.html. Ele demonstra a sequência de interação e acessibilidade básica, sem enviar dados para servidor. A escolha da nota deve ser perceptível por texto e foco, sem depender apenas de cor. O pedido e o cliente deverão ser identificados com autorização adequada no sistema real.

Critérios de validação: completar a nota em três cliques a partir do pedido entregue; navegar por teclado; explicar o significado das notas; recuperar falha de envio preservando a nota e o comentário. Autoavaliação pendente: registrar um teste real de uso e uma melhoria observada.

## 6 Wireframe da tela de avaliação

Figura disponível no documento consolidado.

Figura autoral de baixa fidelidade. O acesso Avaliar produto corresponde ao primeiro clique; selecionar a nota ao segundo e Enviar avaliação ao terceiro. A figura representa a segunda tela do fluxo e não uma captura de sistema implantado.

## 7 Plano de arquitetura de computadores

Dimensionamento inicial proposto para piloto de pequeno porte, com até 10 usuários simultâneos e anexos limitados. CPU de quatro núcleos, 16 GB de RAM e dois SSDs empresariais de 1 TB em RAID 1, com capacidade útil aproximada de um SSD. Rede gigabit e nobreak dimensionado conforme consumo real e autonomia necessária. Esses valores são premissas de projeto, não medições de carga.

O espelhamento mantém os dados disponíveis em caso de falha de um SSD, desde que o restante do sistema continue funcionando. RAID 1 não garante alta disponibilidade completa: há falhas possíveis de controlador, energia, servidor, sistema operacional e aplicação. Para requisitos mais rigorosos, prever servidor secundário, replicação, monitoramento e procedimento de failover testado.

Separar aplicação e banco por serviços e contas, limitar recursos e acessos e manter atualizações. Monitorar CPU, RAM, latência de disco, crescimento do banco, espaço livre e tempo de resposta. Expandir os recursos quando a carga medida ultrapassar os limites definidos. A cópia externa e o teste de restauração continuam obrigatórios mesmo com RAID.

Autoavaliação pendente: explicar o risco que o RAID reduz, o que o backup resolve e por que o dimensionamento precisa ser validado.

## 8 Conclusão e preparação final

A proposta integra relacionamento com clientes, rastreabilidade de produtos e infraestrutura. O maior benefício esperado é substituir registros dispersos por dados relacionados e acessos verificáveis. As escolhas de segurança, rede e hardware foram apresentadas como propostas, sem afirmar que houve implantação.

Antes de entregar: aplicar o Modelo do AVA, incluir print real do backlog e escrever as cinco autoavaliações com base na própria experiência. Conferir referências, paginação e tamanho final inferior a 10 MB. O documento inclui um esboço autoral do wireframe; o HTML fornece o protótipo local para teste.

## Referências

ANHANGUERA. Projeto Integrado Síntese Análise e Desenvolvimento de Sistemas. Material fornecido pelo estudante, sem data editorial confirmada. Páginas 3 a 8.

CISA. StopRansomware Guide. Disponível em: https://www.cisa.gov/stopransomware/ransomware-guide . Referência complementar para backup protegido e restauração.

SCHWABER, Ken; SUTHERLAND, Jeff. The Scrum Guide. 2020. Disponível em: https://scrumguides.org/scrum-guide.html . Acesso em: 16 nov. 2026.

W3C. Web Content Accessibility Guidelines 2.2. Disponível em: https://www.w3.org/TR/WCAG22/ . Referência complementar para teclado, foco e identificação de controles.
