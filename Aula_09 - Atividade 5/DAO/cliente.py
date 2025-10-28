import json

class Cliente:
    def __init__(self, id: int, n: str, e: str, f: str):
        self._id = id
        self._nome = n
        self._email = e
        self._fone = f

    def __str__(self):
        return f"Id: {self._id} \nNome: {self._nome} \nEmail: {self._email} \nFone: {self._fone}"

class ClienteDAO:
    objetos = []

    @classmethod
    def inserir(cls, obj: Cliente):

        
    @classmethod
    def listar(cls):

    @classmethod
    def listar_id(cls, id: int):

    @classmethod
    def atualizar(cls, obj: Cliente):

    @classmethod
    def excluir(cls, obj: Cliente):

    @classmethod
    def abrir(cls):

    @classmethod
    def salvar(cls):