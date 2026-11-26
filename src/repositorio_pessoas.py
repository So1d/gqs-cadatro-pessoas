"""Contrato de persistência de pessoas.

Define as operações que qualquer implementação de repositório precisa
oferecer, mantendo as regras de negócio independentes do mecanismo de
armazenamento utilizado.
"""

from abc import ABC, abstractmethod
from typing import List, Optional

from pessoa import Pessoa


class RepositorioPessoas(ABC):
    """Interface comum aos repositórios de pessoas."""
    @abstractmethod
    def cadastrar(self, pessoa: Pessoa) -> None:
        """Persiste uma pessoa."""
        raise NotImplementedError

    @abstractmethod
    def buscar(self, nome: str) -> Optional[Pessoa]:
        """Busca a primeira pessoa com o nome informado."""
        raise NotImplementedError

    @abstractmethod
    def listar(self) -> List[Pessoa]:
        """Devolve todas as pessoas persistidas."""
        raise NotImplementedError

    @abstractmethod
    def alterar(self, nome: str, nova_pessoa: Pessoa) -> bool:
        """Atualiza a pessoa e informa se encontrou o registro."""
        raise NotImplementedError
