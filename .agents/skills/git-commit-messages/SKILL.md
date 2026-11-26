---
name: git-commit-messages
description: Use quando criar ou revisar uma mensagem de commit Git neste projeto. Padroniza o formato Conventional Commits em português e evita mensagens vagas ou que exagerem o escopo.
---

# Mensagens de commit

## Formato

Escreva a primeira linha neste formato:

`<tipo>(<escopo opcional>): <resumo>`

Use um tipo Conventional Commit:

- `feat`: funcionalidade nova.
- `fix`: correção de comportamento incorreto.
- `docs`: documentação ou instruções para agentes.
- `style`: formatação sem alterar comportamento.
- `refactor`: reorganização interna sem mudança funcional intencional.
- `test`: inclusão ou ajuste de testes.
- `build`: dependências, empacotamento ou configuração de build.
- `chore`: manutenção que não se encaixa nos tipos anteriores.

## Regras

1. Escreva o resumo em português, de forma específica, curta e no imperativo.
2. Use minúsculas após o prefixo, exceto nomes próprios ou identificadores
   que exijam outra capitalização.
3. Não termine o resumo com ponto.
4. Descreva o resultado da mudança, não cada arquivo editado.
5. Não misture alterações independentes em um único commit.
6. Para mudanças incompatíveis intencionais, marque `!` após o tipo ou escopo e
   explique `BREAKING CHANGE:` no corpo.
7. Use um corpo somente quando contexto, motivação ou ressalvas não couberem no
   resumo. Separe-o da primeira linha por uma linha em branco.
8. Ao criar commits com o Copilot, acrescente ao final:

   `Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>`

## Exemplos

- `docs(agents): documentar orientações do projeto`
- `feat(locadora): adicionar recuperação de usuário por e-mail`
- `fix(locadora): restringir edição aos registros do proprietário`
- `test(locadora): cobrir isolamento entre usuários`
