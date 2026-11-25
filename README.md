# Cadastro de Pessoas

Sistema de cadastro de pessoas desenvolvido ao longo da disciplina de Gestão da
Qualidade de Software (COM1024). O programa permite cadastrar, consultar, alterar e
listar pessoas, mantendo a persistência separada das regras de negócio por meio do
contrato `RepositorioPessoas`.

## Objetivo

Aplicar, em um único projeto, as práticas de qualidade trabalhadas na disciplina:
modularização, orientação a objetos, métricas de complexidade, análise estática,
testes automatizados, integração com MySQL, infraestrutura com Docker Compose e
controle de versão com Git e GitHub.

## Funcionalidades

- Cadastro de pessoa com nome, idade e e-mail
- Consulta por nome
- Alteração dos dados de uma pessoa já cadastrada
- Listagem de todas as pessoas com o total de registros
- Avaliação do cadastro: faixa etária, provedor de e-mail e completude do contato
- Escolha entre persistência em memória e persistência em MySQL

## Organização dos diretórios

| Caminho | Responsabilidade |
|---|---|
| `src/pessoa.py` | Entidade `Pessoa`, com atributos e acessores |
| `src/repositorio_pessoas.py` | Contrato abstrato (`ABC`) da persistência |
| `src/repositorio_pessoas_memoria.py` | Implementação que guarda os dados em memória |
| `src/repositorio_pessoas_mysql.py` | Implementação DAO com MySQL |
| `src/cadastro.py` | Regras de negócio sobre a coleção de pessoas |
| `src/main.py` | Menu, entrada de dados e escolha do repositório |
| `tests/test_cadastro.py` | Testes automatizados com PyTest |
| `infra/compose.yaml` | MySQL principal e réplica, com replicação configurada |
| `infra/init/01-schema.sql` | Criação automática do banco e da tabela na primeira subida |
| `documentos/checklist-inspecao.md` | Checklist de inspeção de código usado nas aulas |
| `.pylintrc` | Configuração da análise estática |
| `.pre-commit-config.yaml` | Hooks executados antes de cada commit |
| `pytest.ini` | Configuração do PyTest |

## Tecnologias e requisitos

- Python 3.11 ou superior
- MySQL 8.4 (executado em contêiner)
- Docker e Docker Compose
- Dependências de `requirements.txt`: PyTest, PyLint, RADON, pre-commit e
  `mysql-connector-python`

A versão do interpretador usada no desenvolvimento foi o Python 3.13.

## Preparando o ambiente

Os comandos abaixo assumem Linux e são executados na raiz do projeto.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
pre-commit install
```

Em novos terminais, basta repetir a ativação com `source .venv/bin/activate`.

## Executando o Cadastro de Pessoas

Com o ambiente virtual ativo:

```bash
python src/main.py
```

A constante `USAR_MYSQL`, no início de `src/main.py`, define a persistência:

- `True`: usa `RepositorioPessoasMySQL`, com os dados gravados no MySQL principal;
- `False`: usa `RepositorioPessoasMemoria`, com os dados mantidos apenas durante a
  execução.

Para usar o MySQL, os contêineres precisam estar no ar e as variáveis de ambiente
descritas na seção seguinte precisam estar definidas.

## Configurando e executando o Docker

O arquivo `infra/compose.yaml` sobe dois serviços:

| Serviço | Porta no host | Função |
|---|---:|---|
| `principal` | 3307 | recebe as escritas do programa |
| `replica` | 3308 | recebe as alterações por replicação |

```bash
cd infra
docker compose up -d
docker compose ps
```

O `up -d` apenas inicia os serviços. Na primeira inicialização, o script
`infra/init/01-schema.sql` cria o banco `cadastro`, a tabela `pessoa` e o índice por
nome. O vínculo de replicação, com a criação do usuário `repl`, o
`CHANGE REPLICATION SOURCE` e o `START REPLICA`, segue o roteiro da Aula 11. A
verificação é feita na réplica:

```sql
SHOW REPLICA STATUS\G
```

Os campos `Replica_IO_Running` e `Replica_SQL_Running` precisam estar em `Yes`.

### Banco, tabela e variáveis de ambiente

Banco: `cadastro`. Tabela: `pessoa (id, nome, idade, email)`.

```bash
export DB_HOST=localhost
export DB_PORT=3307
export DB_USER=root
export DB_PASSWORD='<senha do MySQL>'
export DB_NAME=cadastro
```

As variáveis valem apenas para a sessão atual do terminal. Senhas e arquivos `.env`
não devem ser versionados; o `.gitignore` já cobre `.env`.

A escrita acontece sempre no principal. A réplica recebe as alterações por
replicação assíncrona e pode apresentar atraso.

## Executando os testes

```bash
python -m pytest -v
```

Os testes usam `RepositorioPessoasMemoria` e uma implementação de cópia, portanto
não exigem MySQL no ar.

## Práticas de qualidade incorporadas

| Prática | Ferramenta | Como verificar |
|---|---|---|
| Análise estática | PyLint | `pylint src` |
| Complexidade ciclomática e índice de manutenibilidade | RADON | `radon cc -s -a src` e `radon mi -s src` |
| Testes automatizados | PyTest | `python -m pytest -v` |
| Padrões antes do commit | pre-commit | `pre-commit run --all-files` |
| Persistência desacoplada | DAO com `RepositorioPessoas` | troca entre memória e MySQL pela constante `USAR_MYSQL` |
| Infraestrutura reproduzível | Docker Compose | `docker compose up -d` em `infra/` |
| Versionamento e colaboração | Git e GitHub | histórico, branches e Pull Requests |

Resultados da última verificação:

```text
pylint src         10.00/10
pytest             4 passed
radon cc -a src    média A (1.77)
radon mi src       todos os módulos em A
```

As orientações de colaboração, padrões de código e convenções de commit estão em
`CONTRIBUTING.md`.
