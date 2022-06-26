class Associado:

    def __init__ (self,nome,identidade,ocupacao):

        self.nome = nome
        self.identidade = identidade
        self.ocupacao = ocupacao
        self.disciplina = []

        # Getters #

        def get_nome(self): # Pegar info nome
            return self.nome

        def get_identidade(self): # Pegar info identidade
            return self.identidade

        def get_ocupacao(self): # Pegar info ocupacao
            return self.ocupacao

        def get_disciplina(self): # Pegar info Disciplina
            return self.disciplina

        #Setters#

        def set_nome(self,nome): # Alterar nome
            self.nome = nome 
        
        def set_identidade (self,identidade): # Alterar identidade
            self.identidade = identidade

        def set_ocupacao(self,ocupacao): # Alterar ocupacao
            self.ocupacao = ocupacao




