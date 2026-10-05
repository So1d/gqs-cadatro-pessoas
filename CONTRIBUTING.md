# Contribuindo com o projeto Cadastro de Pessoas

Este documento reúne as orientações básicas para contribuir com o projeto:
convenções de código, uso do PyLint e organização dos commits.

## Como contribuir

1. Crie um branch a partir de `main` usando o tipo da mudança
   (`feat/...`, `fix/...`, `refactor/...`, `docs/...`, `chore/...`).
2. Faça alterações pequenas e focadas em um único assunto.
3. Execute o PyLint localmente antes de commitar (ver seção abaixo).
4. Envie a mudança com mensagens de commit no padrão Conventional Commits.
5. Revise o diff completo antes de abrir o merge.

## Convenções de código

- Linguagem Python 3, seguindo as recomendações do [PEP 8](https://peps.python.org/pep-0008/).
- Arquivos de módulo em `snake_case` (ex.: `cadastro.py`).
- Indentação de 4 espaços, sem tabulação.
- Linhas de no máximo 100 caracteres.
- Espaço após `#` nos comentários e ponto final nos comentários explicativos.
- Todo módulo, função e classe deve possuir docstring.
- Nomes de variáveis devem descrever sua finalidade; nomes curtos aceitos
  pelo projeto (`n`, `e`, `b`, `i`, `op`, `qnd`) estão declarados em
  `.pylintrc`, na opção `good-names`.
- Preferir nomes verbais para funções e valores literais nomeados em vez de
  números mágicos.
- Não desativar mensagens do PyLint diretamente no código (`# pylint: disable`)
  sem justificativa registrada na descrição do commit.

## Uso do PyLint

O PyLint é a ferramenta de análise estática do projeto e a configuração
adotada fica registrada em `.pylintrc` na raiz do projeto.

Instalação (se necessário):

```
pip install pylint
```

Análise do projeto a partir da raiz (a configuração é carregada
automaticamente):

```
pylint Cadastro.py
```

Analisando explicitamente a configuração do projeto:

```
pylint --rcfile=.pylintrc Cadastro.py
```

Analisando todos os arquivos Python do projeto:

```
pylint *.py
```

Ao rodar a análise:

- leia cada apontamento e corrija o código quando fizer sentido para a
  qualidade e a legibilidade do projeto;
- não corrija o código apenas para aumentar a nota;
- se um aviso não puder ser corrigido, explique o motivo no commit.

O repositório possui um hook de pré-commit (`.pre-commit-config.yaml`) que
executa o PyLint automaticamente em cada commit. Para instalá-lo:

```
pip install pre-commit
pre-commit install
```

Para rodá-lo manualmente em todos os arquivos:

```
pre-commit run --all-files
```

## Organização dos commits

Mensagens de commit no formato Conventional Commits:

```
<tipo>: <descrição curta no imperativo, em português>
```

Tipos utilizados neste projeto:

| Tipo       | Quando usar                                                   |
| ---------- | ------------------------------------------------------------- |
| `feat`     | nova funcionalidade ou requisito                              |
| `fix`      | correção de defeito                                           |
| `refactor` | reestruturação interna sem mudar o comportamento externo      |
| `docs`     | apenas documentação (`README.md`, `CONTRIBUTING.md`, ...)     |
| `chore`    | manutenção e organização do projeto (configurações, CI, ...)  |
| `test`     | criação ou ajuste de testes                                   |

Boas práticas:

- um commit = uma ideia;
- não misturar formatação/comentários com mudanças de lógica;
- o corpo do commit (quando necessário) explica o **porquê** da mudança;
- nunca commitar arquivos de ambiente (`.venv/`, `__pycache__/`) — o
  `.gitignore` já trata os artefatos do projeto.

Exemplos:

```
feat: adiciona listagem de pessoas cadastradas
fix: corrige consulta de pessoa inexistente
refactor: adequa código aos padrões definidos pelo pylint
chore: adiciona padrões de contribuição e configuração do pylint
```
