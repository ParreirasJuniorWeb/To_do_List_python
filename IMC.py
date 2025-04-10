class CalcularIMC():
    def __init__(self, nome, idade, peso, altura):
        self.peso = peso
        self.altura = altura
        
        self.nome = nome
        self.idade = idade
        
    def getterName(self):
        return self.nome  
    
    def getterIdade(self):
        return self.idade 
    
    def getterPeso(self):
        return self.peso 
    
    def getterAltura(self):
        return self.altura 
    
    def CalcularIMC(self):
        resultado = self.peso / (self.altura ** 2)
        return round(resultado, 2)
    
    def Status_IMC(self, resultado):
        #O Índice de Massa Corporal (IMC) é utilizado para avaliar se o peso está dentro do valor 
        # ideal para a altura1. As faixas de peso de acordo com o IMC são:
        # Fontes:
        # https://www.tuasaude.com/calculadora/imc/
        # https://blog.samisaude.com.br/imc/
        
        if(resultado < 18.5):
            return f"IMC Status => Abaixo do Peso (IMC abaixo de 18,5): IMC:{resultado}"
        elif (resultado > 18.5 and resultado < 24.9):
            return f"IMC Status => Peso Normal (IMC entre 18,5 e 24,9): IMC:{resultado}"
        elif(resultado > 25 and resultado < 29.9):
            return f"IMC Status => Sobrepeso (IMC entre 25 e 29,9): IMC:{resultado}"
        elif(resultado > 30 and resultado < 34.9):
            return f"IMC Status => Obesidade (IMC entre 30 e 34,9): IMC:{resultado}"
        elif(resultado > 35 and resultado < 39.9):
            return f"IMC Status => Obesidade Grau II (IMC entre 35 e 39,9): IMC:{resultado}"
 
peso = float(input("Enter peso: "))
altura = float(input("Enter altura: "))

nome = input("Enter your name: ")
idade = eval(input("Enter your age: "))

calcIMC = CalcularIMC(nome, idade, peso, altura)

resultadoIMC = calcIMC.CalcularIMC()

print(resultadoIMC)

print(f"IMC de {calcIMC.getterName()}, de idade: {calcIMC.getterIdade()}, é", "%.2f" % round(resultadoIMC, 2))  
print(f"Condição de IMC de {calcIMC.getterName()}, de idade: {calcIMC.getterIdade()}, é", calcIMC.Status_IMC(resultadoIMC)) 