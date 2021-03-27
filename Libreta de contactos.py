'''
Crear una clase que administre una libreta de contactos.  Se debe almacenar el nombre de la persona, teléfono, mail y dirección.  
Debe mostrar un menú con las siguientes opciones: 
1- Crear contacto en la agenda. 
2- Listado de contactos.  
3- Buscar ingresando el nombre de la persona. 
4- Modificación de su teléfono mail o dirección. 
5- Finalizar programa.
'''

class Contactos:
  def __init__(self, nombre, telefono, mail, direccion):

    self.nombre = nombre
    self.telefono = telefono
    self.mail = mail 
    self.direccion = direccion    

print("Menu de Opciones \n")
print("Listado de Contactos")
print("Buscar ingrasando el nombre de la persona")
print("Modificacion de su telefono, mail o direccion")
print("Finalizar programa\n")

nombre = input("Digite su Nombre:")
print(f"Su nombre es:" + nombre )

telefono = int(input("Digite su Telefono:"))
print(f"Su telefono es:" + str(telefono))

mail = input("Digite su Mail:")
print(f"Su mail es:" + mail)
