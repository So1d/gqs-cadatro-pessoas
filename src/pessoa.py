"""Classe pessoa."""


class Pessoa:
    """Representa uma pessoa cadastrada."""

    def __init__(self, nome, idade, email):
        """Inicializa os dados da pessoa."""
        self.__nome = nome
        self.__idade = idade
        self.__email = email

    def getNome(self):
        """Devolve o nome da pessoa."""
        return self.__nome

    def getIdade(self):
        """Devolve a idade da pessoa."""
        return self.__idade

    def getEmail(self):
        """Devolve o e-mail da pessoa."""
        return self.__email

    def setNome(self, nome):
        """Atualiza o nome da pessoa."""
        self.__nome = nome

    def setIdade(self, idade):
        """Atualiza a idade da pessoa."""
        self.__idade = idade

    def setEmail(self, email):
        """Atualiza o e-mail da pessoa."""
        self.__email = email
