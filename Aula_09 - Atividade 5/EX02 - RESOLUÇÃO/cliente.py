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
        id = 0
        for ver in cls.objetos:
            if ver._id > id:
                id = ver._id
        obj._id = id + 1
        cls.objetos.append(obj)
        
    @classmethod
    def listar(cls):
        return cls.objetos
    
    @classmethod
    def listar_id(cls, id: int):
        for obj in cls.objetos:
            if obj._id == id:
                return obj
        raise ValueError("ID Cliente não encontrada")
    
    @classmethod
    def atualizar(cls, obj: Cliente):
        for i, cliente in enumerate(cls.objetos):
            if cliente._id == obj._id:
                cls.objetos[i] = obj
                return cls.objetos
        raise ValueError("Não foi achado o ID")

    @classmethod
    def excluir(cls, obj: Cliente):
        for i, cliente in enumerate(cls.objetos):
            if cliente._id == obj._id:
                del cls.objetos[i]
                return cls.objetos
        raise ValueError("Não foi encontrado ID")

    @classmethod
    def salvar(cls):
        import json
        dados_para_salvar = []
        for c in cls.objetos:
            item = {
                "_id": c._id,
                "nome": c._nome,
                "email": c._email,
                "fone": c._fone
            }
            dados_para_salvar.append(item)

        with open("cliente.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados_para_salvar, arquivo, ensure_ascii=False, indent=2)

    @classmethod
    def abrir(cls):
        import json
        try:
            with open("cliente.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                cls.objetos = [Cliente(d["_id"], d["_nome"], d["_email"], d["_fone"]) for d in dados]
        except FileNotFoundError:
            cls.objetos = []
