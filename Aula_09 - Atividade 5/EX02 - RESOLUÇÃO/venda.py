import json

class Venda:
    def __init__(self, id: int, Cliente):
        self._id = id
        self.data = None
        self.carrinho = True
        self.total = 0.0
        self._IdCliente = Cliente
        self.itens = [] # Lista de VendaItem para somar total

    def __str__(self):
        if self._IdCliente:
            cliente_resposta = self._IdCliente
        else:
            cliente_resposta = "Não há cliente"
        return f"Id: {self._id} \nData: {self.data} \nCarrinho: {self.carrinho} \nTotal: {self.total} \nCliente: {cliente_resposta}"

class VendaDAO:
    objetos = []

    @classmethod
    def inserir(cls, obj: Venda):
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
        raise ValueError('ID Venda não encontrada')

    @classmethod
    def atualizar(cls, obj: Venda):
        for i, venda in enumerate(cls.objetos):
            if venda._id == obj._id:
                cls.objetos[i] = obj
                return cls.objetos
        raise ValueError('Não foi achado ID')
          
    @classmethod
    def excluir(cls, obj: Venda):
        for i, venda in enumerate(cls.objetos):
            if venda._id == obj._id:
                del cls.objetos[i]
                return cls.objetos
        raise ValueError('Não foi encontrado ID')
    
    @classmethod
    def salvar(cls):
        import json
        dados_para_salvar = []
        for v in cls.objetos:
            if v._IdCliente:
                id_cliente = v._IdCliente._id
            else:
                id_cliente = None

            item = {
                "_id": v._id,
                "data": v.data,
                "_IdCliente": id_cliente
            }
            dados_para_salvar.append(item)

        with open("venda.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados_para_salvar, arquivo, ensure_ascii=False, indent=2)

    @classmethod
    def abrir(cls, clientes):
        import json
        try:
            with open("venda.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                cls.objetos = []
                for d in dados:
                    cli_obj = next((c for c in clientes if c._id == d["_IdCliente"]), None)
                    venda = Venda(d["_id"], cli_obj)
                    venda.data = d["data"]
                    cls.objetos.append(venda)
        except FileNotFoundError:
            cls.objetos = []