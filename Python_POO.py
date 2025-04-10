from Clientes import Cliente
import datetime

class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo): # Método Construtor da classe Conta:
        self.numero = numero # Atributos da classe Conta
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo
        
def main():
          c1 =Conta(1, 1, 'João', 1000) # Objeto sendo instanciado
          print(f"Nome do titular da conta: {c1.nomeTitular}")
          print(f"Número da conta: {c1.numero}")
          print(f"CPF do titular da conta: {c1.cpf}")
          print(f"Saldo da conta: {c1.saldo}")  
          
          # Saída: Nome do titular da conta: Joao
                    # Número da conta: 1
                    # CPF do titular da conta: 1
                    # Saldo da conta: 1000
                    
        # Quando um script python é executado, a variável reservada
        # NAME referente a ele tem valor igual a "__main__".
        # Nesse caso, a condição do IF a seguir será TRUE.
        # Então o que está no corpo do IF será executado. No caso,
        # é um chamado ao método main do script 
if __name__ == "__main__":
    main() 

# É importante ressaltar que, em Python, não é obrigatório ter um método construtor na classe. Isso ocorrerá apenas se for necessária alguma ação na construção do objeto, como a inicialização e/ou a atribuição de valores.                      
class A():
    def f(self):
        print("\nFoo\n")
        
def main():
    obj_A = A() #Objeto sendo instanciado
    obj_A.f()      
    
if __name__ == "__main__":
    main()      
    
# Métodos: um conjunto de métodos para manipular os atributos e, por consequência, o estado do objeto.

class Conta_user:
    def __init__(self, numero, cpf, nomeTitular, saldo): # Método Construtor da classe Conta:
        self.numero = numero # Atributos da classe Conta
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo
        
    def depositar(self, valor):
        self.saldo += valor
        
    def sacar(self, valor):
        if(self.saldo > valor):
            self.saldo -= valor
        else:
            return print("Saldo insuficiente para realizar o saque!")
             
    def gerar_extrato(self):
        print(f"número: {self.numero} \n cpf: {self.cpf} \n saldo: {self.saldo}")
                    
def main():
          c1 = Conta_user(1, 1, 'João', 0) # Objeto sendo instanciado
          c1.depositar(300)
          c1.sacar(400)
          c1.gerar_extrato()
          
if __name__ == "__main__":
    main()  # Saída: numero: 1 
            # cpf: 1
            # saldo: 200        
#Em Python, não é obrigatório haver um comando para indicar quando o método deve ser finalizado. Porém, na orientação a objetos, é bastante comum, como é o caso da programação procedural, retornar um valor a partir da análise do estado do objeto.
#Método com return:

#  a criação de classe e a instanciação de objeto em Python, vamos fazer um exercício.
# Crie uma classe chamada televisão:

class Televisao():
   def __init__(self, canal, canal_min, canal_max):
       self.canal = canal
       self.canal_min = canal_min
       self.canal_max = canal_max
       
   def mudar_canal_para_baixo(self):
       self.canal -= 1
       
   def mudar_canal_para_cima(self):
       self.canal += 1

tv_1 = Televisao(2, 2, 10)
print(tv_1.canal)       
        
for x in range(1, 20):
    tv_1.mudar_canal_para_cima()
    print(tv_1.canal)

tv_2 = Televisao(10, 2, 10)

for x in range(1, 20):
    print(tv_2.canal)
    tv_2.mudar_canal_para_baixo()
    print(tv_2.canal)                                      
    
# Método construtor da classe Conta:
# class Conta:
#     def__init__(self, numero, cpf, nomeTitular, saldo):
#         self.numero = numero
#         self.cpf = cpf
#         self.nomeTitular = nomeTitular
#         self.saldo = saldo    

#  Método Depositar da classe Conta:
# def __depositar__(self,valor):
#      self.saldo += valor

# class Conta:
    # def__init__(self, numero, cpf, nomeTitular, saldo):
    #      self.numero = numero
    #      self.cpf = cpf
    #      self.nomeTitular = nomeTitular
    #      self.saldo = saldo
    # def depositar(self, valor):
    #      self.saldo += valor
    #  def sacar(self, valor):
    #      self.saldo -= valor
    
class Conta():
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo
        
    def depositar(self, valor):
        self.saldo += valor
        
    def sacar(self,valor):
        if self.saldo < valor:
            return False # O valor da tentativa de saque é maior do que estava depositado.
        else:
            self.saldo -= valor
            return True
            
    def gerar_extrato(self):
        print(f"numero: {self.numero}\n cpf: {self.cpf}\nsaldo: {self.saldo}")     
    
    def transferenciaValor(self, contaDestino, valor):
        if self.saldo < valor:
            return print("Não existe saldo suficiente!")
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return print("Transferência Realizada!")
        
def main():
        c1 = Conta(1,1,"Joao", 0)
        c1.depositar(300)
        saque = c1.sacar(400)
        c1.gerar_extrato()
        print(f"O saque foi realizado? {saque}")
        
        c2 = Conta(3, 456, 'Maria', 0)
        c3 = Conta(5, 123, 'Pedro', 0)
        
        c2.depositar(2000)
        
        c2.transferenciaValor(c3, 1000)
    
        print(c2.saldo)
        
        print(c3.saldo)

if __name__ == "__main__": 
    main()    
    
# Observe!

# >>>from Conta import Conta
# ... conta1 = Conta(1, 123,'Joao',0)
# ... conta2 = Conta(3, 456,'Maria',0)
# ... conta1.depositar(1000)
# ... conta1.transfereValor(conta2,500)
# ... print(conta1.saldo)
# ... print(conta2.saldo)
# 500
# 500   

# Em resumo, 2.000 reais foram depositados na conta2, enquanto foi realizada uma transferência no valor de 1000 reais para a conta3. 
# No final, o saldo ficou 1000 para conta2 e 1000 para conta3. 

# Devemos ressaltar que, no comando conta2.transfereValor(conta3,1000), é passada uma referência da conta2 para o objeto contaDestino por meio de um operador “=”. O comando contaDestino = conta2 é executado internamente no Python.

class ContaBancaria:
    num_contas = 0
    def __init__(self, agencia, numero, saldo):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo
        ContaBancaria.num_contas += 1
        
    def delete(self): #A palavra “self” necessita ser declarada como primeiro argumento em todos os métodos de instâncias de uma classe, pois indica uma referência a um objeto da classe. 
        ContaBancaria.num_contas -= 1
        
    def  depositar(self, valor):
        self.saldo =  self.saldo + valor  
        
    def sacar(self, valor):
        self.saldo = self.saldo - valor 
    
    def consultarSaldo(self):
        return self.saldo

def main():
    
    conta_1 = ContaBancaria('Itaú', 2023, 5000) 
    
    conta_1.depositar(1200)
    print(f"Saldo: {conta_1.consultarSaldo()}")
    
    conta_1.sacar(2000)
    print(f"Saldo: {conta_1.consultarSaldo()}")
    
    conta_1.delete() 
    print(conta_1.num_contas)        
    
if __name__ == "__main__": 
    main()    
    
    
class Televisao:
    def __init__(self, pcanal, min, max):
        self.canal = pcanal
        self.cmin = min
        self.cmax = max
        
    def mudar_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
        else:
            self.canal = self.cmax
            
    def mudar_canal_para_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1
        else:
            self.canal = self.cmin 
            
tv1 = Televisao(9, 2, 10)
print(tv1.canal) # 9
tv1.mudar_canal_para_cima()
print(tv1.canal) # 10
tv1.mudar_canal_para_baixo()
print(tv1.canal) # 9           
               
tv2 = Televisao(3, 2 ,10)
print(tv2.canal) # 3

tv2.mudar_canal_para_baixo()
print(tv2.canal) # 2

tv2.mudar_canal_para_cima()
print(tv2.canal) # 3                                   

# class Cliente:
#     def __init__(self, cpf, nome, endereco):
#         self.cpf = cpf
#         self.nome = nome
#         self.endereco = endereco
class Contas:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero  
        self.saldo = saldo
    def depositar(self, valor):
        self.saldo += valor
    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor  
            return True 
    def consultarSaldo(self):
            return self.saldo  
    def transferirValor(self, contaDestino, valor):
        if self.saldo < valor:
            return print("Não existe saldo suficiente!")
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return print("Transferência Realizada!")
    def gerarExtrato(self):
        return print(f"Número: {self.numero} \n Saldo: {self.saldo} \n Clientes: {self.clientes}")           

cliente1 = Cliente(123, "João", "Rua 1")
cliente12 = Cliente(456, "Maria", "Rua 283")

conta1 = Contas([cliente1, cliente12], 45, 0) # é instanciado um objeto conta1 com dois clientes agregados: cliente1 e cliente2. Esses dois objetos são passados como parâmetros.

conta1.gerarExtrato()
conta1.depositar(1500)

conta1.sacar(500)
conta1.gerarExtrato()                     

# as necessidades do sistema de conta corrente do banco. Isso ocorre porque o banco precisa gerar extratos contendo o histórico de todas as operações realizadas para conta corrente.
# Para isso, o sistema precisa ser atualizado para adicionar uma composição de cada conta com o histórico de operações realizadas
# Essa composição representa que uma conta pode ser composta por vários extratos.

# A classe Extrato tem as responsabilidades de armazenar todas as transações realizadas na conta e de conseguir imprimir um extrato com a lista dessas transações.

class Extrato:
    def __init__(self):
        self.transacoes = []
        
def extrato(self, numeroConta):
    print(f"Extrato: {numeroConta} \n")
    for p in self.transacoes:
        return print(f"{p[0]:15s} {p[1]:10.2f} {p[2]:10s} {p[3].strftime('%d/%b/%y')}")

class Conta_Extrato():
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.sata_abertura = datetime.datetime.today()
        self.extrato = Extrato() # Criação de um atributo extrato, fazendo referência a um objeto Extrato.
        
    def depositar(self, valor):
        self.saldo += valor
        return print(self.extrato.transacoes.append(["DEPOSITO: ", valor, "Data: ", datetime.datetime.today()]))    # Adição de linhas ao array de transações do objeto Extrato por meio do atributo extrato.
    
    def sacar(self, valor):
        if self.saldo < valor:
            return print("Saldo insuficiente!", False) 
        else:
            self.saldo -= valor   
            self.extrato.transacoes.append(["SAQUE: ", valor, "Data: ", datetime.datetime.today()]) 
            return print("Saque feito.", True)  
    
    def transferirValor(self, contaDestino, valor):
        if self.saldo < valor:
            return print("Não existe saldo suficiente!")
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(['TRANSFERÊNCIA: ', valor, "Data: ", datetime.datetime.today()])
            return print("Transferência Realizada com Sucesso!")
    
    def gerarExtrato(self):
        return print(f"Número: {self.numero}\n Saldo: {self.saldo}")


conta_001 = Conta_Extrato([cliente1, cliente12], 45, 0)
conta_001.depositar(1500)
conta_001. gerarExtrato()

# conta_001.extrato.extrato(conta_001.numero)

conta_001.sacar(2000)
conta_001.gerarExtrato()   

# A composição Conta->Extrato inclusive precisa ser inicializada no construtor da classe Conta, conforme exemplificou a imagem. No construtor de Extrato, foi adicionado um atributo transações, o qual foi inicializado para receber um array de valores – transações da conta.             

# Saída: 
# >>>from clientes import Cliente]
# ... from ContasClientesExtrato import Conta
# ... cliente1 = Cliente("123","Joao","Rua X")
# ... cliente2 = Cliente ("456","Maria","Rua W")
# ... conta1 = Conta([cliente1,cliente2],1,2000)
# ... conta1.depositar(1000)
# ... conta1.sacar(1500)
# conta1.extrato.extrato(conta1.numero)
# Extrato : 1
# DEPÓSITO 1000.00 Data 14/Jun/2020
# SAQUE 1500.00 Data 14/Jun/2020

# Na agregação em Python, um objeto tem outro objeto como parte de si mesmo, mas os objetos são independentes entre si. Não há propriedade de vida; se o objeto principal for destruído, o objeto agregado não será.

# Na composição em Python, por outro lado, um objeto é composto por outros objetos e pode existir independentemente deles.
# Encapsulamento em Python é uma prática fundamental na programação orientada a objetos, que visa proteger os dados internos de uma classe e expor apenas o necessário.
# o encapsulamento é fundamental para a manutenção da integridade dos objetos e a proibição de qualquer alteração indevida nos valores dos atributos (estado) do objeto (Caelum, 2020).

# Seguindo em nosso exemplo, no caso da classe Conta, imagine que algum programa tente realizar a seguinte alteração direta no valor do saldo:

# conta1.saldo = -200

# Esse comando viola a regra de negócio do método sacar(), que indica a fim de não haver saque maior que o valor e de deixar a conta no negativo (estado inválido para o sistema).

# def sacar(self, valor):
#   if self.saldo < valor:
#      return False
#   else:
#      self.saldo -= valor
#      self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()])
#      return True

# Para tornar um atributo privado, é preciso iniciá-lo com dois underscores (‘__’). E qual seria o retorno do interpretador ao se acessar um atributo privado para classe Conta? Um erro seria gerado.

# class Conta:
#     def __init__(self, numero, saldo):
#         self.__numero = numero
#         self.__saldo = saldo

# def main():
#     conta = Conta(1, 1000)
#     saldo = conta.__saldo
#     print(saldo)
    
# if __name__ == "__main__":
#     		main()
      
# É importante ressaltar que, em Python, não há realmente atributos privados. 
# O interpretador renomeia o atributo privado para _nomedaClasse__nomedoatributo.

# O atributo, portanto, ainda pode ser acessado. Embora ele funcione, 
# isso é considerado uma prática que viola o princípio de encapsulamento da orientação 
# a objetos. 

# Na prática, deve haver uma disciplina para que os atributos como __ ou _ definido nas classes não sejam acessados diretamente.
# Decorator @property: Utilizando o decorator property nos métodos, mantém-se os atributos como protegidos, os quais, por sua vez, são acessados apenas por meio dos métodos “decorados” com property (Caelum, 2020).
#Ex:

# @property
# def saldo(self):
#    return self._saldo

# Os métodos decorados com a property @setter forçam todas alterações de valor dos atributos privados a passar por esses métodos.

# Observe a notação.

# @<nomedometodo>.setter     

# @saldo.setter
# def saldo(self, saldo):
#   if (self.saldo < 0):
#     print(“saldo inválido”)
#   else:
#     self._saldo = saldo
 
# Os properties ajudam a garantir o encapsulamento no Python.
# Uma boa prática implementada em todas as linguagens orientadas a objetos será a de definir esses métodos apenas se realmente houver regra de negócios diretamente associada ao atributo. Caso não haja, deve-se deixar o acesso aos atributos conforme definido na classe.    

# No código a seguir, demonstraremos como acessar os métodos decorados com @property e @<nomedometodo>.setter.

class Conta:
    def __init__(self, numero):
        self.numero = numero
        self._saldo = 0
        
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print ("saldo inválido")
        else:
            self._saldo = saldo
            
def main():
    conta = Conta(1)
    conta.saldo = 1000 # usando o @saldo.setter
    print(f'saldo da conta = {conta.saldo}') # usando o @property
    
if __name__ == "__main__":
    main()
# Saída: saldo da conta = 1000

# Existem algumas situações em que os sistemas precisam controlar valores associados à classe, e não aos objetos (instâncias) das classes. É o caso, por exemplo, ao se desenvolver um aplicativo de desenho, como o Paint, 
# que precisa contar o número de círculos criados na tela.   Có.:

class Circulo():
    
    _total_circulos = 0
    
    def __init__(self, pontox, pontoy, raio):
        self.pontox = pontox 
        self.pontoy = pontoy
        self.raio = raio
        
        # é necessário controlar a quantidade de círculos criados. Veja!
        self._total_circulos += 1 
        # indicamos para o interpretador que seja criada uma variável total_circulos. Como a declaração está localizada antes do init, o interpretador “entende” que se trata de uma variável de classe, ou seja, que terá um valor único para todos objetos da classe.
        # o valor da variável de classe a cada instanciação de um objeto da classe Círculo é atualizado.
circ1 = Circulo(1, 1, 10)
print(circ1._total_circulos)

circ2 = Circulo(2, 2, 20)
print(circ2._total_circulos)

print(Circulo._total_circulos)  #Referente à Classe Circulo!     
# O acesso direto ao valor da variável de classe não é desejado. Deve-se colocar a variável com atributo privado com o underscore ‘_’.
# Os métodos de classe são a maneira indicada para se acessar os atributos de classe. Eles têm acesso diretamente à área de memória que contém os atributos de classe.
# Para definir um método como estático, deve-se usar o decorator @classmethod.:

class Circulo_alter:
    _total_circulos = 0
    
    def __init__(self, pontox, pontoy, raio):
        self.pontox = pontox
        self.pontoy = pontoy
        self.raio = raio
        type(self)._total_circulos += 1
    
    @classmethod
    def get_total_circulos(cls): #é criado o parâmetro cls como referência para classe. Na linha 12, 
                                # é retornado o valor do atributo de classe _total_circulos.
        return cls._total_circulos    
# Métodos públicos e privados:
# Ex:
class Circulo():
    def __init__(self,clientes,numero,saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        
def __gerarsaldo(self):
    print(f"numero: {self.numero}\n saldo:{self.saldo}")
# No código, foi definido o método __gerarsaldo como privado. Portanto, ele pode ser acessado apenas internamente pela classe Conta.
# Um dos principais padrões da orientação a objetos consiste nos métodos públicos e nos atributos privados. Desse modo, respeita-se o encapsulamento.        
# Métodos estáticos: 
# São métodos que podem ser chamados sem haver uma referência para um objeto da classe, ou seja, não existe a obrigatoriedade da instanciação de um objeto da classe. O método pode ser chamado diretamente. Observe!
import math
class Math:

    @staticmethod
    def sqrt(x):
        return math.sqrt(x)
# num = Math() 
# num.sqrt(5) 
# print(num)
 # >>> Math.sqrt(20): 4.47213595499958  
 # Aqui, o método sqrt da classe Math foi chamado sem que um objet da classe Math fosse instanciado.

# Os métodos estáticos não são uma boa prática na programação orientada a objetos. Eles devem ser utilizados apenas em casos especiais, como o de classes de log em sistemas.

#Obs: @classmethod recebe a classe como primeiro argumento, permitindo acessar ou modificar o estado da classe. 
# @staticmethod não recebe argumentos especiais e não pode alterar o estado da classe ou da instância, funcionando como uma função comum dentro da classe.

class Livro():
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        
    def consultarTitulo(self, isbn):
            return self.titulo
        
    def consultarAutor(self, isbn):
            return self.autor
        
    def consultarIsbn(self, titulo, autor):
            return self.isbn
        
class Biblioteca(): # Código errado - Não usar o objeto puro e sim um ARRAY com o conteúdo do objeto para conseguir manipular os objectos dentro de um ARRAy.
    def __init__(self, nome, listLivros):
        self.nome = nome
        self.listaLivros = listLivros
    
    def AdicionarLivro(self, add):
        self.listaLivros = add
        return print(f"Livro adicionado com sucesso. Livro: {self.listaLivros.consultarTitulo(add.isbn)}")
    def RemoverLivro(self, remove):
        self.listaLivros -= remove
        return print(f"Livro removido com sucesso. Livro: {self.listaLivros.consultarTitulo(remove.isbn)}")         
    def ListarTodosLivros(self):
        return print(f"Todos os Livros: {self.listaLivros.titulo}, {self.listaLivros.autor}, {self.listaLivros.isbn}")

livro = Livro("Senhor dos Anéis", "Não Sei o nome dele", '4567')                    
biblioteca = Biblioteca('Saraiva', livro)

biblioteca.AdicionarLivro(livro) 
biblioteca.ListarTodosLivros() # Agregação    

# print(livro.consultarTitulo(4567))
# print(livro.consultarAutor(4567))
# print(livro.consultarIsbn("Senhor dos Anéis", "Não Sei o nome dele"))   

# Cenário 2:

nome = input("Entre com o seu nome: ")
idade = eval(input("Entre com sua idade: "))
anoNasc = eval(input("Entre com o ano de nascimento: "))

class Pessoa():
    def __init__(self, nome, idade, anoNasc):
        self.nome = nome
        self.idade = idade
        self.anoNasc = anoNasc
        
    def AnoNasc(self):
        return print(f"Ano de Nascimento: {self.anoNasc}")
    def mostrarNome_Idade(self):
        return print(f"Nome: {self.nome}, idade: {self.idade}")
    @staticmethod
    def MaiorIdade(idade):
        if(idade < 18):
            return print(f"Pessoa menor de idade. Idade: {idade}")
        else:
            return print(f"Pessoa maior de idade. Idade: {idade}")
        
pessoa1 = Pessoa(nome, idade, anoNasc) 
pessoa1.AnoNasc()
pessoa1.mostrarNome_Idade() 
pessoa1.MaiorIdade(idade)     

class Biblioteca_Correcao:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []
        
    def adicionar_livros(self, livro):
        self.livros.append(livro)
        print(f'Livro "{livro.titulo}" adicionado à biblioteca "{self.nome}".')  
          
    def remover_livro(self, isbn):
        
        for livro in self.livros:
            
            if livro.isbn == isbn:
                self.livros.remove(livro)
                
                print(f'Livro "{livro.titulo}" removido da biblioteca "{self.nome}".') 
                return True
            else:
                return print(f'Livro com ISBN {isbn} não encontrado na biblioteca "{self.nome}".')
    
    def listar_livros(self):
        if not self.livros:
            return print(f'A biblioteca "{self.nome}" não tem livros.')
        else:
            print(f'Livros na biblioteca "{self.nome}": ')
            
            for livro in self.livros:
                    return print(f'-{livro.titulo} por {livro.autor} (ISBN: {livro.isbn})')

#Testando as Classes:

#Criando alguns livros:

livro1 = Livro('O Senhor dos Anéis', 'J.R.R. Tolkien', '1234567890')
livro2 = Livro('1984', 'George Orwell', '0987654321')
livro3 = Livro('O Apanhador no Campo de Centeio', 'J.D. Salinger', '1122334455')                         

# Criando uma biblioteca:
biblioteca_correcao = Biblioteca_Correcao('Biblioteca Central')

# Adicionado livros à biblioteca:
biblioteca_correcao.adicionar_livros(livro1)
biblioteca_correcao.adicionar_livros(livro2)
biblioteca_correcao.adicionar_livros(livro3) 

# Listando todos os livros na biblioteca:
biblioteca_correcao.listar_livros()

# Removendo um livro da biblioteca:
biblioteca_correcao.remover_livro('0987654321') 

# Listando todos os livros na biblioteca após a remoção
biblioteca_correcao.listar_livros()             

class itemToDo:
    def __init__(self, id, nome, completed):
        self.id = id
        self.nome = nome
        self.completed = completed
class Todo_Do_List:
    def __init__(self):
        self.list_to_do = []
        
    def adicionarTarefa(self, todo):
        self.list_to_do.append(todo)
        print(f'Tarefa: {todo.nome} foi adicionada à lista.')
        
    def removerTarefa(self):
        
        for todo in self.list_to_do:
            
            if self.list_to_do[todo.id].completed == True: 
                self.list_to_do.remove(todo)
                print(f"A tarefa {todo.nome} foi removida com sucesso.")
                return True
            else:
                return print(f"A tarefa {todo.nome} não foi encontrada na lista. ")
    
    def listar_tarefas(self):
        if not self.list_to_do:
            return print("Não há tarefas.")
        else:
            print(f'Tarefas na listagem: ')
            
            for todo in self.list_to_do:
                print(f'-{todo.id}: {todo.nome}: (status) => {todo.completed}.')

    def TarefaConcluida(self, todo_nome, completed):
        for todo in self.list_to_do:
            if self.list_to_do[todo.id].nome != todo_nome:
                return print("\nNão há esta tarefa na lista.\n")
            else:
                if self.list_to_do[todo.id].nome == todo_nome:
                    self.list_to_do[todo.id].completed = completed
                    if completed == True:
                        return print(f"A tarefa {self.list_to_do[todo.id].nome} foi concluída com sucesso!")
                    else:
                        return print(f"A tarefa {self.list_to_do[todo.id].nome} NÃO foi concluída!")

#Testando as Classes:

#Criando algumas Tarefas:

todo1 = itemToDo(1, 'Lavar a roupa', False)
todo2 = itemToDo(2, 'Lavar o carro', False)
todo3 = itemToDo(3, 'Tomar banho', False)                         
            
# Criando uma Tarefa:
TarefaLista = Todo_Do_List()

# Adicionado livros à biblioteca:
TarefaLista.adicionarTarefa(todo1)
TarefaLista.adicionarTarefa(todo2)
TarefaLista.adicionarTarefa(todo3)

# Listando todos os livros na biblioteca:
TarefaLista.listar_tarefas()                
              
# Tarefa já foi concluída?
TarefaLista.TarefaConcluida('Lavar o carro', True)                

# Listando todos os livros na biblioteca:
TarefaLista.listar_tarefas() 

#Removendo Tarefas:
TarefaLista.removerTarefa()

# Listando todos os livros na biblioteca:
TarefaLista.listar_tarefas() 

# Herança:

import datetime

class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo, limite):
        super().__init__(clientes, numero, saldo)
        self.limite = limite
        
    def sacar(self, valor):
        if(self.saldo + self.limite) < valor:
            print(f"Não existe saldo suficiente conta numero: {self.numero}, cliente {self.clientes.cpf}")
            return False
        else:
            self.saldo -= valor
            if(self.saldo < 0):
                self.limite += self.saldo
            self.extrato.transacoes.append(["SAQUE", valor, datetime.datetime.today()])
            return True
# A classe tem de ser instanciada com a passagem do limite como um parâmetro da construção do objeto. O método __Init__ foi sobrescrito da superclasse Conta. 
# Já o método super(), que foi utilizado para chamar um método da superclasse, pode ser usado em qualquer método da subclasse (Real Phyton, 2020).

# Adicionado apenas na subclasse ContaEspecial, em que ele será utilizado para implementar a regra de saques além do valor do saldo (linha 7). => Atributo Limite.add()
# Método Sacar:  O método precisa verificar se o valor a ser sacado, passado como parâmetro, é menor que a soma do saldo atual mais o limite da conta especial.

# Nesse caso, a classe Conta Especial reescreveu o método sacar da superclasse Conta. Essa característica é conhecida como sobrescrita (override) dos métodos, 
# instancia as classes Conta e ContaEspecial.

cliente_ABC_1 = Cliente("123", "João", "Rua X")
cliente_ABC_2 = Cliente("456", "Maria", "Rua W")
cliente_ABC_3 = Cliente("789", "Joana", "Rua H")

#As três contas foram instanciadas, as contas comuns com saldo 2000 e a conta espacial com 3000. 

conta_01 = Conta(cliente_ABC_2, 1, 2000)
conta_02 = Conta(cliente_ABC_2, 2, 2000)
conta_03 = Conta(cliente_ABC_3, 3, 3000, 2000)  

#impressão do saldo das três contas

print(f"Cliente: {cliente_ABC_1.cpf} da conta comum {conta_01.numero} possui saldo R$ {conta_01.saldo}")             
print(f"Cliente: {cliente_ABC_2.cpf} da conta comum {conta_02.numero} possui saldo R$ {conta_02.saldo}")
print(f"Cliente: {cliente_ABC_3.cpf} da conta especial {conta_03.numero} possui saldo R$ {conta_03.saldo} e limite R$ {conta_03.limite}\n")

#depositou 500 e tentou sacar 3000 da conta comum que não terá saldo
conta_02.depositar(500)
#mensagem indicando saldo após depósito
print(f"Cliente: {cliente_ABC_2.cpf} da conta comum {conta_02.numero} possui saldo R$ {conta_02.saldo} \n")

conta_02.sacar(3000)
#mensagem indicando que não foi possível sacar e o saldo atual
print(f"Cliente: {cliente_ABC_2.cpf} da conta comum {conta_02.numero} possui saldo R$ {conta_02.saldo} \n")

#depositou 100 e tentou sacar 2000 da conta especial que tem limite
conta_03.depositar(100)
#mensagem indicando saldo após depósito
print(f"Cliente: {cliente_ABC_3.cpf} da conta especal {conta_03.numero} possui saldo R$ {conta_03.saldo} e limite {conta_03.limite}\n")

conta_03.sacar(2000)
#mensagem indicando que foi possível sacar e saldo negativo
print(f"Cliente: {cliente_ABC_3.cpf} da conta especal {conta_03.numero} possui saldo R$ {conta_03.saldo} e limite {conta_03.limite}\n")

#tentativa de saque acima do limite
conta_03.sacar(2000)
print(f"Cliente: {cliente_ABC_3.cpf} da conta comum {conta_03.numero} possui saldo R$ {conta_03.saldo} e limite R$ {conta_03.limite}\n") 

# A saída do programa será:

# Cliente: 123 da conta comum 1 possui saldo R$ 2000
# Cliente: 456 da conta comum 2 possui saldo R$ 2000
# Cliente: 789 da conta especial 3 possui saldo R$ 1000 e limite R$ 2000
# Cliente: 456 da conta comum 2 possui saldo R$ 2500 
# Cliente: 456 da conta comum 2 possui saldo R$ 2500 
# Cliente: 789 da conta especal 3 possui saldo R$ 1000 e limite 2000
# Cliente: 789 da conta especal 3 possui saldo R$ -1000 e limite 1000
# Não existe saldo suficiente conta numero 3 cliente 789
# Cliente: 789 da conta comum 3 possui saldo R$ -1000 e limite R$ 1000 

# O programa começa com a criação de três clientes: João (cliente1), Maria(cliente2) e Joana(cliente3). Cada cliente é identificado por seu CPF, nome e endereço.
# o programa cria três contas bancárias:

# Conta1: Uma conta comum para João, com um saldo inicial de R$ 2000.
# Conta2: Outra conta comum, desta vez para Maria, também com um saldo inicial de R$ 2000.
# Conta3: Uma conta especial para Joana, que tem um saldo inicial de R$ 1000 e um limite de crédito adicional de R$ 2000.

# Antes de realizar qualquer transação, o programa imprime os saldos iniciais das três contas. Essa ação permite que o usuário visualize o estado inicial de cada conta. Em particular, a conta especial de Joana é destacada por seu limite de crédito, além do saldo inicial.

# A primeira operação realizada no programa é um depósito de R$ 500 na conta de Maria. Este depósito é simples e direto, aumentando o saldo de Maria para R$ 2500. 

# No entanto, como o saldo de Maria não é suficiente para cobrir esse saque, a operação falha. O saldo permanece inalterado em R$ 2500, e o programa informa ao usuário que o saque não foi possível devido ao saldo insuficiente.

#  o programa foca na conta especial de Joana. Primeiro, R$ 100 são depositados, elevando o saldo de Joana para R$ 1100. Em seguida, o programa realiza um saque de R$ 2000. Como esse valor excede o saldo disponível, a conta entra no limite de crédito, resultando em um saldo negativo de R$ -900 e reduzindo o limite de crédito de Joana para R$ 1100. O sistema permite essa transação e atualiza os valores adequadamente, refletindo o uso do limite de crédito.

# o programa tenta realizar um segundo saque de R$ 2000 na conta de Joana, que já está utilizando parte de seu limite. Desta vez, o saque falha, pois o valor solicitado ultrapassa o limite de crédito restante. O programa então exibe uma mensagem informando que a operação não pode ser concluída e mantém os valores do saldo e do limite inalterados.

# A ContaEspecial é uma classe comum e pode ser instanciada como todas as outras classes independentes da instanciação de objetos da classe Conta.

# Herança múltipla: 
# É um mecanismo que possibilita a uma classe herdar o código de duas ou mais superclasses.

# A Classe Poupança também será criada para armazenar a taxa de renumeração e o cálculo do rendimento mensal da poupança.

class Poupanca:
    def __init__(self, taxa_remuneracao):
        self.taxa_remuneracao = taxa_remuneracao
        self.data_abertura = datetime.datetime.today()
        
    def remunerarConta(self):
        self.saldo += self.saldo * self.taxa_remuneracao

class ContaRemuneradaPoupanca(Conta, Poupanca):
    #  a classe é herdeira de Conta e de Poupança (nessa ordem). Tal ordem tem importância, pois existem dois métodos no pai com o mesmo nome. O Python dá prioridade para a primeira classe que implementa esse método na ordem da declaração
    
    def __init__(self, taxa_remuneracao, clientes, numero, saldo):
        Conta.__init__(self, clientes, numero, saldo)
        Poupanca.__init__(self, taxa_remuneracao)
        # Deve ser chamado o construtor explicitamente das superclasses com o seguinte formato: nomeclasse.__init__(construtores).
    
    def remunerarConta(self):
        self.saldo += self.saldo * (self.taxa_remuneracao / 30)  
    
    def gerar_saldo(self):
        return self.saldo             
          
cliente1 = Cliente("123", "Joao", "Rua X")
cliente2 = Cliente("456", "Maria", "Rua W")

conta1 = Conta([cliente1, cliente2], 1, 2000)
contapoupanca1 = Poupanca(0.1)
contaremunerada1 = ContaRemuneradaPoupanca(0.1, [cliente1], 5, 1000)

contaremunerada1.remunerarConta()
contaremunerada1.gerar_saldo()

# Sa´pida: numero: 5 saldo: 1003.3333333333334     

# A herança em Python permite que uma classe filha herde atributos e métodos de uma classe pai. A alternativa d) destaca corretamente que, ao herdar de uma classe pai, a classe filha pode substituir os métodos da classe pai com suas próprias implementações, se necessário.

# Polimorfismo:

# Polimorfismo em Python permite que objetos de diferentes classes sejam tratados através de uma interface comum, adaptando comportamentos conforme necessário.        

# Polimorfismo é o mecanismo que permite a um método com o mesmo nome ser executado de modo diferente a depender do objeto que está chamando o método. 

# Todos os descontos são realizados em cima do valor bruto após o rendimento mensal. Uma vez por mês, o banco executa o cálculo do rendimento de todos os tipos de contas. 

class ContaCliente:
    def __init__(self, numero, IOF, IR, valor_investido, taxa_rendimento):
        self.numero = numero
        self.IOF = IOF
        self.IR = IR
        self.valor_investido = valor_investido
        self.taxa_rendimento = taxa_rendimento

    def calculoRendimento(self):
        remuneracao = self.valor_investido * self.taxa_rendimento
        valorIOF = remuneracao * self.IOF
        ValorIR = remuneracao * self.IR
        self.valor_investido += remuneracao - valorIOF - ValorIR
# Classe ContaCliente

class ContaComum(ContaCliente):
    def __init__(self, numero, IOF, IR, valor_investido, taxa_rendimento):
        super().__init__(numero, IOF, IR, valor_investido, taxa_rendimento)

    def calculoRendimento(self):  # (2)
        remuneracao = self.valor_investido * self.taxa_rendimento
        valorIOF = remuneracao * self.IOF
        self.valor_investido += remuneracao - valorIOF
# Classe ContaComum.

class ContaRemunerada(ContaCliente):
    def __init__(self, numero, IOF, IR, valor_investido, taxa_rendimento):
        super().__init__(numero, IOF, IR, valor_investido, taxa_rendimento)

    def calculoRendimento(self): #(3)
        self.valor_investido += self.valor_investido * self.taxa_rendimento
# ContaRemunerada

# Em (1), foi definido um método Extrato, que é igual para as três classes, ou seja, as subclasses herdarão o código completo desse método.
# Em (2) e (3), as subclasses possuem regras de negócios diferentes; portanto, elas sobrescrevem o método CalculoRendimento para atender às suas necessidades.

# implementação da classe Banco e do programa que a utiliza.

class Banco:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
        self.contas = []

    def adiciona_conta(self, conta_cliente):
        self.contas.append(conta_cliente)

    def calcular_rendimento_mensal(self):
        for c in self.contas:
            c.calculoRendimento()

    def imprime_saldo_contas(self):
        for c in self.contas:
            c.extrato()
# classe Banco

banco1 = Banco(999, "teste")
contacliente1 = ContaCliente(1,0.01,0.1,1000,0.05)
contacomum1 = ContaComum(2,0.01,0.1,2000,0.05)
contaremunerada1 = ContaRemunerada(3,0.01,0.1,2000,0.05)

banco1.adicionaconta(contacliente1) #(4)
banco1.adicionaconta(contacomum1) #(5)
banco1.adicionaconta(contaremunerada1) #(6)
banco1.calcularendimentomensal#(7)
banco1.imprimesaldocontas() #(8)
          
# Em (4), (5) e (6), o banco adiciona todas as contas da hierarquia em um único método devido ao teste “É-UM” das linguagens orientadas a objetos.
# Em (4), o objeto é da própria classe ContaCliente. Em (5), o objeto contacomoum1 passado é uma ContaComum, que passa no teste “É-UM”, pois uma ContaComum também é uma ContaCliente.
# Em (6), o objeto contarenumerada1 “É-UM” objeto ContaComum.
# Em (7), acontece a “mágica” do polimorfismo, pois, em (4), (5) e (6), são adicionadas contas de diferentes tipos para o array conta da classe Banco. Assim, no momento da execução do método c.calculorendimentomensal(), o valor de c recebe, em cada loop, um tipo de objeto diferente da hierarquia da classe ContaCliente.  
# na instrução c.CalculoRendimento(), o interpretador tem de identificar dinamicamente de qual objeto da hierarquia ContaCliente deve ser chamado o método CalculoRendimento. 
# Em (8), acontece uma característica que vale ser ressaltada. Pelo polimorfismo, o interpretador verificará o teste “É-UM”, porém esse método não foi sobrescrito pelas subclasses da hierarquia ContaCliente. Portanto, será chamado o método Extrato da superclasse. 
 
# O polimorfismo é bastante interessante em sistemas com dezenas de subclasses herdeiras de uma única classe; assim, todas as subclasses redefinem esse método. 
                                     
# O polimorfismo em Python refere-se à capacidade de diferentes classes implementarem métodos com o mesmo nome, mas com comportamentos específicos a cada classe.

# Isso permite que funções e métodos utilizem objetos de diferentes classes de forma intercambiável, contanto que esses objetos implementem o método requerido. Esse conceito é fundamental para a flexibilidade e reutilização de código em programação orientada a objetos.

# a implementar polimorfismo e herança em Python, criando um sistema de classes que modela diferentes tipos de animais e suas habilidades de movimento e fala

# Classe base para todos os animais:
class Animal:
    def __init__(self, nome):
        self.nome = nome
        
    def falar(self):
        pass
    
    def mover(self):
        pass
        
# Subclasse Cachorro que sobrescreve os métodos falar e mover:

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome) 
        
    def falar(self):
        return "Au!"
    
    def mover(self):
        return f"{self.nome} está andando."

# Subclasse Gato que sobrescreve os métodos falar e mover

class Gato(Animal):
    
    def falar(self):
        return f"Miau!"  
    
    def mover(self):
        return f"{self.nome} está andando."
    
# Subclasse Vaca que sobrescreve os métodos falar e mover:

class Vaca(Animal):
    
    def falar(self):
        return "Muu!"
    
    def mover(self):
        return f"{self.nome} está andando."
    
class Voador: 
    def voar(self):
        return f"{self.nome} está voando."
    
# Mixin para animais que podem nadar

class Nadador:
    def nadar(self):
        return f"{self.nome} está nadando."
    
# Subclasse Pato que herda de Animal, Voador e Nadador:

class Pato(Animal, Voador, Nadador):
    
    def falar(self):
        return "Quack!"
    
    def mover(self):
        return f"{self.andar()}, {self.nadar()} E {self.voar()}"
    
    def andar(self):
        return f"{self.nome} estaá andando."
    
# Função que usa Polimorfismo para chamar o método falar:

def fazer_som(animal):
    return animal.falar() 

# Função que usa Polimorfismo para chamar o método mover:

def fazer_movimento(animal):
    return animal.mover()                             

# Instâncias das classes:
cachorro = Cachorro('Lug')
gato = Gato('Floquinho')
vaca = Vaca('Mimosa')
pato = Pato('Pato Donald')

# Chamando os métodos polimórficos:

print(fazer_som(cachorro))  # Saída: Au!
print(fazer_som(gato))      # Saída: Miau!
print(fazer_som(vaca))      # Saída: Muu!
print(fazer_som(pato))      # Saída: Quack!

print(fazer_movimento(cachorro))  # Saída: O cachorro está andando.
print(fazer_movimento(gato))      # Saída: O gato está andando.
print(fazer_movimento(vaca))      # Saída: A vaca está andando.
print(fazer_movimento(pato))      # Saída: Pato Donald está andando, Pato Donald está nadando E Pato Donald está voando.

# Saída no Console: 
# Au!
# Miau!
# Muu!
# Quack!
# Lug está andando.
# Floquinho está andando.
# Mimosa está andando.
# Pato Donald estaá andando., Pato Donald está nadando. E Pato Donald está voando.

class Jacare(Animal, Nadador):
        
    def falar(self):
        return f"CHRROOOOO!"
    
    def mover(self):
        return f"{self.andar()} E {self.nadar()}"   
    
    def andar(self):
        return f"{self.nome} está andando."

# Função que usa Polimorfismo para chamar o método mover:

# def fazer_movimento(animal):  -- Já está definida à cima!
#     return animal.mover() 

# Instâncias das classes 
 
jacare = Jacare("Jacaré")

# Chamando os métodos polimórficos
# Testando a nova classe Jacare
    
print(fazer_som(jacare)) # Saída: CHRROOOOO!
print(fazer_movimento(jacare))    # Saída: Jacaré está andando E Jacaré está nadando.

# Classe abstrata e classe para tratamento de exceções:

# Classes abstratas:
# Uma classe abstrata não pode ser instanciado durante a execução do programa orientado a objetos, ou seja, não pode haver objetos dessa classe executados na memória.
# O termo “abstrato” remete a um conceito do mundo real, considerando a necessidade apenas de objetos concretos no programa. 

# Houve apenas a adição de esteréotipo <> para indicar que Conta Cliente é uma classe abstrata. O Python utiliza um módulo chamado abc para definir uma classe como abstrata, a qual será herdeira da superclasse ABC (Abstract Base Classes).
# Toda classe abstrata é uma subclasse da classe ABC (Caelum, 2020). Para tornar a classe Conta Cliente abstrata, muda-se sua definição.

# Para uma classe ser considerada abstrata, ela precisa ter pelo menos um método abstrato. Esse método pode ter implementação, embora isso não faça sentido, pois ele deverá obrigatoriamente ser implementado pelas subclasses.

# Para uma classe ser considerada abstrata, ela precisa ter pelo menos um método abstrato. Esse método pode ter implementação, embora isso não faça sentido, pois ele deverá obrigatoriamente ser implementado pelas subclasses.

# O decorator @abstractmethod indica para a linguagem que o método é abstrato (Standard Library, 2020), o que ocorre no código a seguir.

from abc import ABC, abstractmethod

class ContaCliente(ABC):
    
    def __init__(self, numero, IOF, IR, valor_investido, taxa_rendimento):
         self.numero = numero
         self.IOF = IOF
         self.IR = IR
         self.valor_investido = valor_investido
         self.taxa_rendimento = taxa_rendimento 
         
    @abstractmethod
    
    def calculo_rendimento(self):
        pass  
    # Definição de método abstrato.
    
# Quando se tentar instanciar um objeto da classe, será obtido um erro indicando que essa classe não pode ser instanciada.       
# Saída: 
# TypeError: Can't instantiate abstract class ContaCliente with abstract methods calculo_rendimento

# Ao tentar criar uma instância de ContaCliente com cc1 = ContaCliente(1, 0.1, 0.25, 1000, 0.1), o Python irá lançar um erro do tipo TypeError. Esse erro ocorre porque ContaCliente é uma classe abstrata e possui métodos abstratos que não foram implementados.

# Para que o código funcione, você deve criar uma subclasse concreta de ContaCliente que implemente o método calculo_rendimento. Somente depois disso, você poderá instanciar essa subclasse.

# As classes mencionadas devem obrigatoriamente implementar os métodos. Caso contrário, elas serão classes abstratas e delegarão para as suas subclasses a implementação concreta do método abstrato.

# Uma solução seria:

class ContaComum(ContaCliente):
    
    def calculo_rendimento(self):
        #Implementação fictícia para cálculo de rendimento
        return self.valor_investido * self.taxa_rendimento - (self.IOF + self.IR) 

# Instanciando a subclasse concreta!
    
cc1 = ContaComum(1, 0.1, 0.25, 1000, 0.1)
print(cc1.calculo_rendimento())   

# Saída: 99.65

# Tratamento de Exceções em Python:

# O que São Exceções?

# Exceções são eventos que ocorrem durante a execução de um programa, interrompendo seu fluxo normal. 
# Em Python, quando uma exceção é lançada e não é tratada, o programa encerra sua execução abruptamente, exibindo uma mensagem de erro. 
# Para evitar esse comportamento indesejado, é fundamental entender como capturar e tratar exceções, 
# garantindo que o programa continue funcionando de forma controlada.

# Python permite a criação de exceções personalizadas, 
# o que possibilita a diferenciação entre os erros inerentes à linguagem e aqueles específicos da lógica da aplicação. 
# Isso contribui para um código mais claro e fácil de manter.

# Ex:

def divide(a, b):
    return a / b

try:
    resultado = divide(10, 0)
    
except ZeroDivisionError as ex:
    print(f"Erro: {ex}")    # Saída: Erro: division by zero
    
# Neste código, ao tentar dividir 10 por 0, Python lança uma exceção ZeroDivisionError. 
# O bloco try...except captura essa exceção, permitindo que o programa lide com o erro de forma controlada, 
# imprimindo uma mensagem de erro personalizada em vez de interromper a execução do programa.    

# Criando Exceções Personalizadas: Python também permite a criação de exceções personalizadas, que são úteis quando se deseja capturar e tratar erros específicos de um determinado contexto da aplicação.
# Para criar uma exceção personalizada, utilizamos a herança da classe Exception, conforme o exemplo a seguir:

class ExcecaoCustomizada(Exception):
    pass 

# A classe ExcecaoCustomizada define uma nova exceção que pode ser lançada e tratada separadamente das exceções padrão de Python. O uso do comando pass indica que não há necessidade de adicionar 
# comportamento específico à exceção; a distinção pelo nome é o suficiente.

 # Lançando Exceções: Uma vez que uma exceção personalizada tenha sido criada, ela pode ser lançada em situações específicas, usando a instrução raise.
 
def checa_valor(valor):
    if valor < 0:
        raise ExcecaoCustomizada("Valor não pode ser negativo!")
# Considere o exemplo abaixo, onde um método lança a exceção ExcecaoCustomizada caso o valor passado seja negativo:    
# Neste exemplo, ao detectar um valor negativo, a função checa_valor interrompe sua execução normal e lança a exceção ExcecaoCustomizada, transmitindo uma mensagem explicativa.

# Tratando Exceções com try...except: 
try:
    checa_valor(-10)
except ExcecaoCustomizada as ex:
    print(f"Exceção lançada: {ex}") 

# a função checa_valor é chamada com um valor negativo, o que resulta na exceção ExcecaoCustomizada sendo lançada. O bloco try...except captura essa exceção, e o programa trata o erro de forma controlada, exibindo a mensagem associada à exceção.    

# Outro exemplo:

class ExcecaoCustomizada(Exception):
    pass

def checa_valor(valor):
    if valor < 0:
        raise ExcecaoCustomizada("Valor não pode ser negativo!")

def divide(a, b):
    return a / b


try:
    resultado = divide(10, 0)
    print(f"Resultado: {resultado}")
except ZeroDivisionError as ex:
    print(f"Erro de divisão por zero: {ex}")
    print(f"Resultado: {resultado}")

try:
    check = checa_valor(-10)
    print(f"Verifcação: {check}")
except ExcecaoCustomizada as ex:
    print(f"Exceção personalizada lançada: {ex}")
    print(f"Verifcação: {check}")
    
# Definição da Exceção Personalizada: 

# A classe ExcecaoCustomizada é criada para representar uma exceção específica que pode ser lançada em nosso código. 
# Ela herda de Exception, a classe base para todas as exceções em Python. 
# Isso permite que ExcecaoCustomizada seja usada e tratada como qualquer outra exceção no Python.    

# Funções que Podem Lançar Exceções:

# A função checa_valor(valor) verifica se um valor é negativo. Se for, ela lança uma ExcecaoCustomizada com uma mensagem explicativa.
# A função divide(a, b) realiza a divisão de dois números. Se b for zero, o Python automaticamente lança uma ZeroDivisionError.

# Tratamento de Exceções:

# O bloco try...except é utilizado para tentar executar as funções e capturar qualquer exceção que seja lançada. 
# No primeiro bloco, tentamos dividir 10 por 0, o que gera uma ZeroDivisionError. 
# Essa exceção é capturada e uma mensagem de erro é exibida.

# No segundo bloco try...except, chamamos checa_valor(-10),
# o que resulta na exceção personalizada ExcecaoCustomizada sendo lançada. 
# O bloco except captura essa exceção e exibe a mensagem associada. 

# O tratamento de exceções é uma prática fundamental na programação em Python, permitindo que os programas sejam mais robustos e resilientes a erros
#  Esse exemplo destaca a flexibilidade de Python em permitir a criação de exceções personalizadas, que podem ser utilizadas para capturar e tratar condições específicas da lógica do seu programa.
# Isso é especialmente útil em projetos maiores, onde a clareza e a especificidade dos erros são cruciais para a manutenção e depuração do código.

# Classes Abstratas:

# Em Python, uma classe abstrata (A) é uma classe que não pode ser instanciada diretamente e pode conter métodos concretos (com implementações) e métodos abstratos (sem implementações). 
#  Métodos abstratos são métodos que devem ser implementados por subclasses concretas, garantindo uma estrutura consistente na hierarquia de classes. 
# classes abstratas podem ser herdadas por outras classes e podem conter métodos concretos
# uma classe abstrata em Python pode conter métodos abstratos.  
# uma classe abstrata em Python não pode ser instanciada diretamente.  
# Python suporta classes abstratas usando o módulo abc.  

# Classe Abstrata Veículo:

from abc import ABC, abstractmethod

class Veiculo(ABC):
    
    def __init__(self, modelo, cor, ano):
         self.modelo = modelo
         self.cor = cor
         self.ano = ano 
         
    @abstractmethod
    
    def mover(self):
        pass  
    # Definição de método abstrato.
    
    @abstractmethod
    
    def ligar(self):
        pass  
    # Definição de método abstrato.

# Subclasse Carro    
class Carro(Veiculo):
    
    def mover(self):
        #Implementação fictícia para o método abstrato!
        return f"{self.modelo}, {self.cor}, {self.ano} - O carro está movendo!" 
    
    def ligar(self):
        #Implementação fictícia para o método abstrato!
        return f"{self.modelo}, {self.cor}, {self.ano} - O carro está ligado!" 

#Subclasse Bicicleta
class Bicicleta(Veiculo):
    
    def mover(self):
        #Implementação fictícia para o método abstrato!
        return f"{self.modelo}, {self.cor}, {self.ano} - A bicicleta está movendo!" 
    
    def ligar(self):
        #Implementação fictícia para o método abstrato!
        return f"{self.modelo}, {self.cor}, {self.ano} - A bicicleta automática/elétrica está ligado!" 

# Subclasse Carro    
class Aviao(Veiculo):
    
    def mover(self):
        #Implementação fictícia para o método abstrato!
        return f"{self.modelo}, {self.cor}, {self.ano} - O Aviao está movendo e vai voar!!!" 
    
    def ligar(self):
        #Implementação fictícia para o método abstrato!
        return f"{self.modelo}, {self.cor}, {self.ano} - O Aviao está ligado e pronto para a decolagem!" 
        
# Instanciando as subclasses concretas!  
    
carro = Carro("Lifan", "vermelho", 2003)
print(carro.mover())
print(carro.ligar())

# Saída:
# Lifan, vermelho, 2003 - O carro está movendo!
# Lifan, vermelho, 2003 - O carro está ligado!

bicicleta = Bicicleta("Hot Driver", "vermelha", 1989)
print(bicicleta.mover())
print(bicicleta.ligar())

#Saída:
# Hot Driver, vermelha, 1989 - A bicicleta está movendo!
# Hot Driver, vermelha, 1989 - A bicicleta automática/elétrica está ligado!   

aviao = Aviao("Azul", "azul", 1990)
print(aviao.mover())
print(aviao.ligar())

# Saída:

# Azul, azul, 1990 - O Avião está movendo e vai voar!!!
# Azul, azul, 1990 - O Avião está ligado e pronto para a decolagem!

# Classe Calculadora - classe Abstrata:

class Calculadora(ABC):
    
    def __init__(self, num1, num2):
         self.num1 = num1
         self.num2 = num2 
         
    @abstractmethod
    
    def adicao(self):
        pass  
    # Definição de método abstrato.
    
    @abstractmethod
    
    def subtracao(self):
        pass  
    # Definição de método abstrato.
    
    @abstractmethod
    
    def multiplicacao(self):
        pass  
    # Definição de método abstrato.
    
    @abstractmethod
    
    def divisao(self):
        pass  
    # Definição de método abstrato.

# Subclasse Carro    
class Calculadora_concreta(Calculadora):
    
    def adicao(self):
        #Implementação fictícia para o método abstrato!
        try:
            return f"{self.num1} + {self.num2} = (Resultado) {self.num1 + self.num2}" 
        except TypeError:
            return "Erro: Tipos de dados inválidos para adição."
        
    def subtracao(self):   
        #Implementação fictícia para o método abstrato!
        try:
            
            if(self.num1 - self.num2 > 0):
                return f"{self.num1} - {self.num2} = (Resultado) {self.num1 - self.num2}"
            else:
                return f"Valor não pode ser negativo! Resultado = {self.num1 - self.num2}"
        
        except TypeError:
            return "Erro: Tipos de dados inválidos para subtração."
        
    def multiplicacao(self):
        try:
            #Implementação fictícia para o método abstrato!
            return f"{self.num1} x {self.num2} = (Resultado) {self.num1 * self.num2}"
        
        except TypeError:
            return "Erro: Tipos de dados inválidos para multiplicação."
        
    def divisao(self):
        try:
            #Implementação fictícia para o método abstrato!
            return f"{self.num1} / {self.num2} = (Resultado) {self.num1 / self.num2}"
        
        except TypeError:
            return "Erro: Tipos de dados inválidos para divisão."
        
# Instanciando as subclasses concretas!  
    
calc = Calculadora_concreta(10, 20)

print(calc.adicao())
print(calc.subtracao()) 
print(calc.multiplicacao())
try:
    print(calc.divisao())
except ZeroDivisionError as ex:
    print(f"Erro de divisão por zero: {ex}")

# Saída:

# 10 + 20 = (Resultado) 30
# 10 - 20 = (Resultado) -10
# 10 x 20 = (Resultado) 200
# 10 / 20 = (Resultado) 0.5  

# Saída Atualizada:

# 10 + 20 = (Resultado) 30
# Valor não pode ser negativo! Resultado = -10
# 10 x 20 = (Resultado) 200
# 10 / 20 = (Resultado) 0.5

# Saída com Divisão por zero:

# 10 + 0 = (Resultado) 10
# 10 - 0 = (Resultado) 10
# 10 x 0 = (Resultado) 0
# Erro de divisão por zero: division by zero

# Saída Atualizada com Try...Exception:

# Erro: Tipos de dados inválidos para adição.
# Erro: Tipos de dados inválidos para subtração.
# 10 x asn = (Resultado) asnasnasnasnasnasnasnasnasn
# Erro: Tipos de dados inválidos para divisão.