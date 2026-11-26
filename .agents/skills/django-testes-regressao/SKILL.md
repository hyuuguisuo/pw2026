---
name: django-testes-regressao
description: Use ao validar mudanças Django ou investigar regressões. Define uma sequência mínima e segura de verificações sem acessar ou destruir dados compartilhados.
---

# Testes e regressão Django

## Escolha das verificações

1. Para mudanças de configuração, rotas ou imports, execute
   `python manage.py check`.
2. Para comportamento alterado, escreva ou atualize testes focados que falhem
   sem a correção e cubram o comportamento anterior que precisa ser preservado.
3. Execute primeiro o teste focado; para mudanças abrangentes, execute também
   `python manage.py test locadora`.
4. Revise mensagens de erro, status HTTP, dados persistidos e HTML apresentado,
   conforme o comportamento que mudou.

## Segurança dos dados

- Antes de executar a suíte, verifique qual banco a configuração de teste usa.
- Nunca permita que a suíte crie, remova ou limpe um banco de dados compartilhado
  ou de produção.
- Se a configuração apontar para um serviço compartilhado, use uma configuração
  local isolada de teste, por exemplo SQLite temporário, e remova apenas os
  arquivos temporários criados para a validação.
- Não altere a configuração persistente do banco do projeto apenas para fazer
  um teste passar.

## Conclusão

- Registre quais comandos foram executados e seus resultados reais.
- Diferencie teste aprovado de teste que não pôde ser executado.
- Não trate apenas uma verificação de sintaxe ou `manage.py check` como prova de
  comportamento funcional.
- Finalize conferindo `git diff --check` e se somente arquivos do escopo foram
  modificados.
