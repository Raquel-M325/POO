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
    return raise ValueError("ID da Categoria não foi encontrada")
    
  @classmethod
  def atualizar(cls, obj: Categoria):
    for cliente in cls.objetos:
      #quero achar o id
  
  @classmethod
  def excluir(cls, obj: Categoria):


  @classmethod
  def abrir(cls):

  @classmethod
  def salvar(cls):
  
