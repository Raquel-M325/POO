import json

class Produto:
    def __init__(self, id: int, descricao: str, preco: float, estoque: int, categoria):
        self.id = id
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
        self.categoria = categoria

    def __str__(self):
    # Categoria
        if self.categoria:
            cat_nome = self.categoria.descricao  # <- aqui era "nome"
        else:
            cat_nome = "Sem categoria"

        return (
            f"ID: {self.id}\n"
            f"Descrição: {self.descricao}\n"
            f"Preço: {self.preco}\n"
            f"Estoque: {self.estoque}\n"
            f"Categoria: {cat_nome}"
        )


class ProdutoDAO:
    objetos = []

    @classmethod
    def inserir(cls, obj: Produto):
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
        raise ValueError("ID Produto não encontrado")

    @classmethod
    def atualizar(cls, obj: Produto):
        for i, produto in enumerate(cls.objetos):  
            if produto._id == obj._id:  
                cls.objetos[i] = obj
                return cls.objetos
        raise ValueError("Não foi achado o ID")

    @classmethod
    def excluir(cls, obj: Produto):
        for i, produto in enumerate(cls.objetos): 
            if produto._id == obj._id:  
                del cls.objetos[i]
                return cls.objetos
        raise ValueError("Não foi encontrado ID")

    @classmethod
    def salvar(cls):
        with open("produtos.json", mode="w", encoding="utf-8") as arquivo:
            lista = []
            for p in cls.objetos:
                if p.categoria:
                    cat_id = p.categoria._id
                else:
                    cat_id = None

                lista.append({
                    "id": p._id,
                    "descricao": p.descricao,
                    "preco": p.preco,
                    "estoque": p.estoque,
                    "categoria": cat_id
                })

            json.dump(lista, arquivo, indent=4, ensure_ascii=False)

    @classmethod
    def abrir(cls, categorias):
        import json
        try:
            with open("produto.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                cls.objetos = []
                for d in dados:
                    cat_obj = next((c for c in categorias if c._id == d["idCategoria"]), None)
                    cls.objetos.append(Produto(d["_id"], d["descricao"], d["preco"], d["estoque"], cat_obj))
        except FileNotFoundError:
            cls.objetos = []