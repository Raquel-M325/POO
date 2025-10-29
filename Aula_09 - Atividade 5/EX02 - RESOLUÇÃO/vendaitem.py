import json

class VendaItem:
    def __init__(self, id: int, qtd: int, preco_unitario: float, venda, produto):
        self.id = id
        self.qtd = qtd
        self.preco_unitario = preco_unitario
        self.venda = venda
        self.produto = produto

    def __str__(self):
        # Verifica produto
        if self.produto:
            prod_nome = self.produto.descricao
        else:
            prod_nome = "Sem produto"

        # Verifica venda
        if self.venda:
            venda_id = self.venda._id   # <- aqui estava "id", agora "_id"
        else:
            venda_id = "Sem venda"

        # Calcula total
        total = self.qtd * self.preco_unitario

        return (
            f"ID: {self.id}\n"
            f"Produto: {prod_nome}\n"
            f"Quantidade: {self.qtd}\n"
            f"Preço unitário: {self.preco_unitario}\n"
            f"Total: {total}\n"
            f"Venda ID: {venda_id}"
        )

class VendaItemDAO:
    objetos = []

    @classmethod
    def inserir(cls, obj: VendaItem):
        id = 0
        for ver in cls.objetos:
            if ver._id > id:
                id = ver._id
        obj._id = id + 1    # tem que especificar o obj para verificar no VendaItem que irá usar, nesse caso será o id dele
        cls.objetos.append(obj)
    
    @classmethod
    def listar(cls):
        return cls.objetos
    
    @classmethod
    def listar_id(cls, id: int):
        for obj in cls.objetos:
            if obj._id == id:
                return obj
        raise ValueError('o ID VendaItem não foi encontrado')
    
    @classmethod
    def atualizar(cls, obj: VendaItem):
        for i, vendaitem in enumerate(cls.objetos):
            if vendaitem._id == obj._id:
                cls.objetos[i] = obj
                return cls.objetos
        raise ValueError('Não foi achado o ID')
    
    @classmethod
    def excluir(cls, obj: VendaItem):
        for i, vendaitem in enumerate(cls.objetos):
            if vendaitem._id == obj._id:
                del cls.objetos[i]
                return cls.objetos
        raise ValueError('Não foi encontrado ID')

    @classmethod
    def salvar(cls):
        with open("vendaitens.json", mode="w", encoding="utf-8") as arquivo:
            lista = []
            for vi in cls.objetos:
                if vi.venda:
                    venda_id = vi.venda._id
                else:
                    venda_id = None

                if vi.produto:
                    produto_id = vi.produto._id
                else:
                    produto_id = None

                lista.append({
                    "id": vi._id,
                    "quantidade": vi.qtd,
                    "preco_unitario": vi.preco_unitario,
                    "venda": venda_id,
                    "produto": produto_id
                })

            json.dump(lista, arquivo, indent=4, ensure_ascii=False)


    @classmethod
    def abrir(cls, vendas, produtos):
        import json
        try:
            with open("vendaitem.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                cls.objetos = []
                for d in dados:
                    # Buscar os objetos Venda e Produto correspondentes
                    venda_obj = next((v for v in vendas if v._id == d["venda_id"]), None)
                    produto_obj = next((p for p in produtos if p._id == d["produto_id"]), None)

                    vi = VendaItem(
                        d["_id"],
                        d["qtd"],
                        d["preco_unitario"],
                        venda_obj,
                        produto_obj
                    )
                    cls.objetos.append(vi)
        except FileNotFoundError:
            cls.objetos = []