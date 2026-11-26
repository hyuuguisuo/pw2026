---
name: django-acesso-por-usuario
description: Use ao criar, alterar ou revisar modelos, formulários, views ou endpoints que leem ou modificam registros associados a um usuário. Garante isolamento por proprietário sem ampliar permissões.
---

# Acesso a registros por usuário

## Antes de alterar

1. Identifique o campo que relaciona o registro ao usuário, por exemplo
   `cadastrado_por`, e localize todos os fluxos de leitura e escrita.
2. Confira autenticação, grupos/permissões, relacionamentos dos formulários e
   templates que expõem ações. Preserve as permissões adicionais já existentes.
3. Diferencie o catálogo público e outras páginas públicas das telas de gestão.
   Não torne conteúdo público privado nem altere a experiência pública sem
   requisito explícito.

## Regras de implementação

1. Limite a queryset do usuário em listagens, detalhes, atualizações e exclusões.
   Um identificador de registro fornecido na URL não concede acesso: registros
   de outra pessoa devem ficar indisponíveis pela view.
2. Em operações de criação, defina o proprietário no servidor com o usuário da
   requisição; não confie em um campo enviado pelo cliente.
3. Limite os `ModelChoiceField` e filtros de relações aos objetos que o usuário
   pode usar. Faça isso também nos formulários de edição.
4. Não amplie o queryset usando condições alternativas que incluam registros de
   outros usuários sem uma regra de negócio expressa.
5. Preserve o comportamento de filtragem, ordenação, paginação, mensagens e
   retorno para registros próprios.

## Testes essenciais

- Usuário autenticado lista e visualiza os próprios registros.
- Outro usuário não encontra o registro ao tentar detalhe, edição ou exclusão.
- Uma criação atribui o proprietário autenticado mesmo que o pedido tente
  fornecer outro proprietário.
- Campos de relações não oferecem objetos de outro usuário.
- Conteúdo público existente continua disponível anonimamente quando aplicável.
