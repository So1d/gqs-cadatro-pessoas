"""Regras de negócio para o cadastro de pessoas."""

from typing import List, Optional

from pessoa import Pessoa
from repositorio_pessoas import RepositorioPessoas
from repositorio_pessoas_memoria import RepositorioPessoasMemoria

class CadastroPessoas:
    """Gerencia as operações de cadastro de pessoas."""

    def __init__(
        self, repositorio: Optional[RepositorioPessoas] = None
    ) -> None:
        if repositorio is None:
            repositorio = RepositorioPessoasMemoria()

        self.__repositorio = repositorio

    def cadastrar(self, nome, idade, email):
        """Cria e persiste uma pessoa, devolvendo a entidade criada."""
        pessoa = Pessoa(nome, idade, email)
        self.__repositorio.cadastrar(pessoa)
        return pessoa

    def buscarPorNome(self, nome):
        """Busca uma pessoa pelo nome."""
        return self.__repositorio.buscar(nome)

    def listar(self) -> List[Pessoa]:
        """Devolve todas as pessoas cadastradas."""
        return self.__repositorio.listar()

    def alterar(self, nome, novo_nome, nova_idade, novo_email):
        """Atualiza os dados da pessoa identificada pelo nome atual."""
        pessoa = self.buscarPorNome(nome)

        if pessoa is None:
            return None

        nova_pessoa = Pessoa(novo_nome, nova_idade, novo_email)

        if self.__repositorio.alterar(nome, nova_pessoa):
            return nova_pessoa
        return None
