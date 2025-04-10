class itemTodoList:
    def __init__(self, item_nome_todo, ID, completed):
        self.item_nome_todo = item_nome_todo
        self.ID = ID
        self.completed = completed
        
    def consultarNome(self):
            return self.item_nome_todo
        
    def consultarID(self):
            return self.ID
        
    def consultarCompleted_todo(self):
            return self.completed
    
    def settarNome(self, nome):
        self.item_nome_todo = nome
        
    def settarID(self, ID):
            self.ID = ID
        
    def settarCompleted_todo(self, completed):
            self.completed = completed    

class TodoList_in_Python(itemTodoList):
    def __init__(self, nome_todo, ID_todo, completed):
        super().__init__(nome_todo, ID_todo, completed)
        self.List_todos = []
    
    def addItemTodo(self, itemTodo_user):
        self.List_todos.append(itemTodo_user)
        
    def MudarEstadoDaTarefa(self, status, nome_todo):
        for todo in self.List_todos:
            if(todo.consultarNome() in nome_todo):
                todo.settarCompleted_todo(status) 
                print(f"A tarefa {todo.consultarNome()} foi concluída com sucesso.")
                self.Listar_todos() 
            else:
                return print(f"A tarefa '{nome_todo}' NÃO está na lista.")
                
    def ExcluirItemTodo(self, nome_todo):
        for todo in self.List_todos:
            if(todo.consultarNome() in nome_todo):
                if(todo.consultarCompleted_todo() == True):
                    indice_itemTodo = self.List_todos.index(todo)
                    x = self.List_todos.pop(indice_itemTodo)
                    print(f"Tarefa removida com sucesso: Tarefa '{x.consultarNome()}' ID [{x.consultarID()}] Está concluída: {x.consultarCompleted_todo()}")
                    self.Listar_todos()
                else:
                    print(f"A Tarefa '{todo.consultarNome()}' NÃO pode ser excluída porque ela NÃO está CONCLUÍDA [status: {todo.consultarCompleted_todo()}]. Conclua a tarefa!")    
            else:
                print(f"A tarefa '{nome_todo}' NÃO está no ID [{todo.consultarID()}] da lista.") 
                   
    def AlterarItemTodo(self, nome_todo, itemTodo_user):
        for todo in self.List_todos:
            if(todo.consultarNome() in nome_todo):
                tarefaAntiga = todo.consultarNome()  
                tarefaAntiga_id = self.List_todos.index(todo)
                print(f"ÍNDICE na Lista: {tarefaAntiga_id}")
        
                if(todo.consultarNome() == nome_todo):
                    todo.settarNome(itemTodo_user.consultarNome()) 
                    todo.settarID(itemTodo_user.consultarID()) 
                    todo.settarCompleted_todo(itemTodo_user.consultarCompleted_todo()) 
                    print(f"Tarefa alterada com sucesso: ÍNDICE: [{tarefaAntiga_id}], Nome: {tarefaAntiga}.")
                    self.Listar_todos() 
            else:
                print(f"A tarefa '{nome_todo}' NÃO está no ID [{todo.consultarID()}] da lista.") 
            
    def Listar_todos(self):
        print("\nOs elementos no ArrayList são: ")
   
        for todo in self.List_todos:
            print("Tarefa Nome: " + todo.consultarNome())
            print("Tarefa ID: " + str(todo.consultarID()))
            print("Tarefa Está concluída: " + str(todo.consultarCompleted_todo()) + "\n")
            
    def VerificarSeTarefaExiste(self, nome_tarefa):
        for todo in self.List_todos:
            if(todo.consultarNome() == nome_tarefa):
                resultado = self.List_todos.count(todo)
        if(resultado > 0):
            return print("Tarefa encontrada: " + str(resultado) + " => Tarefa: " + str(todo.consultarNome()))
        return print("Tarefa NÃO encontrada: " + str(resultado) + " => Tarefa: " + str(todo.consultarNome()))
        
    def Apagar_todos(self):
            self.List_todos.clear()
            self.Listar_todos()
            
            for todo in self.List_todos:
                for index in range(self.List_todos.index(todo.consultarID())):     
                    eh_vazio_ArrayList = self.List_todos.count(index)
                    print(f"ArrayList todos está vazio: [0] para vazio e [1...] para cheio " + str(eh_vazio_ArrayList))	
            print("Os elementos no ArrayList foram excluídos com sucesso.")
    
    def VerificarIndice(self, id_TarefaDesejada_alterar, antigoValor):
        for todo in self.List_todos:
            Array_id_todos = [todo.consultarID()]
            
            while(id_TarefaDesejada_alterar in Array_id_todos):
                if(id_TarefaDesejada_alterar in Array_id_todos):
                    id_TarefaDesejada_alterar = int(input("Informe o número dessa tarefa novamente - ID de tarefa já existente: \n")) # Tarefa nova id      
                    return id_TarefaDesejada_alterar
                else:
                    return antigoValor
                
item_todo = TodoList_in_Python("Padrão", 0, False)  
controle = "s"   
deletarTarefa = "NÃO"  
nome_tarefa = ""
ConfirmarSelecaoDelecao = "NÃO"
alterarTarefa = "NÃO"
TarefaAlterar = 0
TarefaDesejada_alterar = ""
findTarefa = "NÃO"
TarefaEncontrada = 0
limpar_array = "NÃO"

mudarStatusTarefa = "NÃO"

while(controle != "NÃO"):
 
    tarefa1 = input("Insira uma tarefa nova: ")
    tarefa2 = input("Insira uma tarefa nova: ")
    tarefa3 = input("Insira uma tarefa nova: ")
    tarefa4 = input("Insira uma tarefa nova: ")
    tarefa5 = input("Insira uma tarefa nova: ")    
    
    item_todo_1 = TodoList_in_Python(tarefa1, 0, False)
    item_todo_2 = TodoList_in_Python(tarefa2, 1, False)
    item_todo_3 = TodoList_in_Python(tarefa3, 2, False)
    item_todo_4 = TodoList_in_Python(tarefa4, 3, False)
    item_todo_5 = TodoList_in_Python(tarefa5, 4, False)
    
    item_todo.addItemTodo(item_todo_1)
    item_todo.addItemTodo(item_todo_2)
    item_todo.addItemTodo(item_todo_3)
    item_todo.addItemTodo(item_todo_4)
    item_todo.addItemTodo(item_todo_5)
    
    item_todo.Listar_todos()
    
    mudarStatusTarefa = input("Deseja concluir alguma dessas tarefas: SIM ou NÃO\n").upper()
    
    if(mudarStatusTarefa == "SIM"):
        nome_tarefa = input("Entre com a tarefa:\n")
        set_status = bool(input("Deseja concluí-la? True [Concluir] ou False [NÃO concluir]\n").capitalize())
        
        item_todo.MudarEstadoDaTarefa(set_status, nome_tarefa)
        
    deletarTarefa = input("Deseja deletar alguma dessas tarefas: SIM ou NÃO\n").upper()
    
    if(deletarTarefa == "SIM"):
        nome_tarefa = input("Entre com a tarefa:\n")
        
        ConfirmarSelecaoDelecao = input(f"Deseja confirmar a exclução da tarefa: {nome_tarefa} - SIM ou NÃO\n").upper()
        if (ConfirmarSelecaoDelecao == "SIM"):
            
            item_todo.ExcluirItemTodo(nome_tarefa)
    
    alterarTarefa = input("Deseja alterar alguma dessas tarefas: SIM ou NÃO\n").upper()
    
    if(alterarTarefa == "SIM"):
        TarefaAlterar = input("Informe qual das tarefas deseja alterar: \n") # Tarefa antiga nome
        
        id_TarefaDesejada_alterar = int(input("Informe o número da nova tarefa: \n")) # Tarefa nova id
        TarefaDesejada_alterar = input("Entre com a NOVA tarefa:\n") # Tarefa nova nome   
            
        user_novoObjeto_alteracao = TodoList_in_Python(TarefaDesejada_alterar, item_todo.VerificarIndice(id_TarefaDesejada_alterar, id_TarefaDesejada_alterar), False)
        
        item_todo.AlterarItemTodo(TarefaAlterar, user_novoObjeto_alteracao)
        
        findTarefa = input("Deseja encontrar alguma tarefa? SIM ou NÃO\n").upper()
        
        if(findTarefa == "SIM"):
            TarefaEncontrada = input("Entre com o nome dela: \n")
            
            item_todo.VerificarSeTarefaExiste(TarefaEncontrada)   
            
    limpar_array = input("Deseja limpar a lista de tarefas: SIM ou NÃO\n").upper() 
    
    if(limpar_array == "SIM"):
        
        item_todo.Apagar_todos()
          
    controle = input("Deseja Repetir o processo: SIM ou NÃO\n").upper()    