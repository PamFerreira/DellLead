# Módulo Classes - Cadastro Simples
print('Cadastro de cliente')
class Pessoa:
  def __init__(self, nome, idade, endereço, telefone):
    self.nome = nome
    self.idade = idade
    self.endereço = endereço
    self.telefone = telefone
            
p1 = Pessoa('Jo', 37 , 'Ida_Ceratti', 5555555)

print("Nome do cliente: " + p1.nome)
print("Idade do cliente: " + str(p1.idade))
print("Endereço: " + p1.endereço)
print("Telefone: " + str(p1.telefone))

class Pet:
  def __init__(self, nome_pet, tipo_pet, idade_pet, peso_pet, doença_pet):
    self.nome_pet = nome_pet
    self.tipo_pet = tipo_pet
    self.idade_pet = idade_pet
    self.peso_pet = peso_pet
    self.doença_pet  = doença_pet
    
b1 = Pet ('Cláudio', 'Porquinho da Índia', 4, 1.1, 'Obesidade')
    
print("Nome do animal: " + b1.nome_pet)
print("Tipo de animal: " + b1.tipo_pet)
print("Idade: " + str(b1.idade_pet))
print("Peso do animal: " + str(b1.peso_pet))
print("Patologia do pet: " + str(b1.doença_pet))
