class Associado:

    def __init__ (self,nome,identidade):

        self.nome = nome
        self.identidade = identidade
        self.disciplina = []
        self.ocupacao = None

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

    #Padronização do print do Associado#
    def __str__(self):
	    return f'{self.nome} ({self.identidade})'






