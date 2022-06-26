class Organizacao:
    
    def __init__ (self,nome,capacidade_maxima):

        self.nome = nome
        self.capacidade = capacidade_maxima
        self.horarios = []
        self.dias = []

    #Getters#

    def get_nome (self): # Pegar info nome
        return self.nome

    def get_capacidade (self): # Pegar info capacidade
        return self.capacidade

    def get_horarios (self): # Pegar info horarios
        return self.horarios

    def get_dias (self): # Pegar info dias
        return self.dias

    #Setters#

    def set_nome(self,nome): # Alterar nome
        self.nome = nome

    def set_capacidade_maxima (self,capacidade_maxima): # Alterar capacidade maxima
        self.capacidade_maxima = capacidade_maxima

