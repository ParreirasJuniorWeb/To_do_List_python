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