class Organizacao:
    
    def __init__ (self,nome,codigo,capacidade_maxima):

        self.nome = nome
        self.codigo = codigo
        self.capacidade = capacidade_maxima
        self.horarios = {}

    #Getters#

    def get_nome (self): # Pegar info nome
        return self.nome

    def get_capacidade (self): # Pegar info capacidade
        return self.capacidade

    def get_horarios (self): # Pegar info horarios
        return self.horarios
    
    def get_codigo (self): # Pegar info do codigio
        return self.codigo
    
    #Setters#

    def set_nome(self,nome): # Alterar nome
        self.nome = nome

    def set_capacidade_maxima (self,capacidade_maxima): # Alterar capacidade maxima
        self.capacidade_maxima = capacidade_maxima

    def set_codigo (self,codigo):
        self.codigo = codigo

    #Padronização do print da Organização#
    def __str___(self):
        return f"Nome: {self.nome}\n Código: {self.codigo}\n Capacidade: {self.capacidade_maxima}\n Horários: {self.horarios}\n Dias: {self.dias}"
