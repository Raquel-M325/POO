import json

class Categoria:
    def __init__(self, id: int, d: str):
        self._id = id
        self.descricao = d
  
    def __str__(self):
        return f"Id: {self._id} \nDescrição: {self.descricao}"


class CategoriaDAO:
    objetos = []

    @classmethod
    def inserir(cls, obj: Categoria):
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
        raise ValueError("ID da Categoria não foi encontrada")
    
    @classmethod
    def atualizar(cls, obj: Categoria):
        for i, categoria in enumerate(cls.objetos):
            if categoria._id == obj._id:
                cls.objetos[i] = obj
                return cls.objetos
        raise ValueError('Não foi achado ID')
  
    @classmethod
    def excluir(cls, obj: Categoria):
        for i, categoria in enumerate(cls.objetos):
            if categoria._id == obj._id:
                del cls.objetos[i]
                return cls.objetos
        raise ValueError('Não foi encontrado o ID')

    @classmethod
    def salvar(cls):
        import json
        dados_para_salvar = []
        for c in cls.objetos:
            item = {
                "_id": c._id,
                "descricao": c.descricao
            }
            dados_para_salvar.append(item)

        with open("categoria.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados_para_salvar, arquivo, ensure_ascii=False, indent=2)

    @classmethod
    def abrir(cls):
        import json
        try:
            with open("categoria.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                cls.objetos = [Categoria(d["_id"], d["descricao"]) for d in dados]
        except FileNotFoundError:
            cls.objetos = []
