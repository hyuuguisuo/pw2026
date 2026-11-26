# Orientações para agentes de IA

## Escopo do projeto

- Este projeto é uma aplicação Django. O comando de gestão é `python manage.py`
  e o app principal é `locadora`.
- Antes de alterar uma funcionalidade, leia os modelos, as views, os formulários,
  os templates e os testes diretamente relacionados.
- Faça alterações pequenas e coerentes com os padrões que já existem. Não
  reformule a interface, os estilos, a navegação ou o fluxo de uso sem pedido
  explícito.
- Preserve o catálogo público da página inicial. As telas de gestão devem
  continuar limitando os registros ao usuário proprietário, conforme as regras
  já implementadas.

## Padrões Django

- Ao criar ou alterar CRUD, mantenha as verificações de autenticação e
  autorização. Registros com `cadastrado_por` devem ser limitados ao usuário
  atual em consultas de listagem, detalhe, edição e exclusão.
- Em formulários que aceitam relações com outros registros, limite as opções
  aos registros que o usuário pode utilizar.
- Use Django Messages e os templates existentes para feedback de operações.
- Preserve os `FilterSet`, a paginação do Django e os parâmetros de filtro.
- Use os componentes visuais e os plugins já instalados em vez de adicionar
  componentes ou dependências paralelas.
- Não inclua credenciais, tokens ou dados de usuários em código, logs, testes
  ou respostas.

## Skills do projeto

Consulte as instruções aplicáveis em `.agents/skills/<nome>/SKILL.md` antes de
executar a tarefa:

- `bootbox-confirmacoes`: confirmações e diálogos de ações no front-end.
- `datatables-listagens`: tabelas de listagem com DataTables.
- `django-filter-listagens`: filtros e paginação nas listagens.
- `django-acesso-por-usuario`: propriedade e autorização de registros.
- `django-testes-regressao`: seleção e execução de validações.
- `git-commit-messages`: mensagens de commit.

## Validação

- Execute `python manage.py check` após mudanças em código Django.
- Execute os testes relevantes; para mudanças que afetam o app, prefira
  `python manage.py test locadora`.
- A configuração padrão pode apontar para um banco compartilhado. Não permita
  que testes criem ou removam bancos em serviços compartilhados; use uma
  configuração de teste isolada quando necessário.
- Confira `git diff --check` e revise as alterações para evitar mudanças
  incidentais em arquivos gerados, dados locais ou arquivos fora do escopo.
- Informe claramente validações que não puderam ser executadas e o motivo.
