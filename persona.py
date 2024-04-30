class Persona:
  
  def __init__(self, nombre: str = "john", apellido: str = "doe", du: int = 1234567):
    self.__nombre__ = nombre
    self.__apellido__ = apellido
    self.__du__ = du 

  def __str__(self):
        return f'Nombre: {self.__nombre__}, Apellido: {self.__apellido__}, Documento: {self.__du__}'