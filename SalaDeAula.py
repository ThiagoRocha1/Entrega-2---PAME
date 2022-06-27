from Organizacao import Organizacao

HORARIOS = {'Segunda-Feira': [8,10,12,14,16,18,20],
            'Terça-Feira': [8,10,12,14,16,18,20],
            'Quarta-Feira': [8,10,12,14,16,18,20],
            'Quinta-Feira': [8,10,12,14,16,18,20],
            'Sexta-Feira': [8,10,12,14,16,18,20]}

class SalaDeAula(Organizacao):
    def __init__ (self,nome, codigo, capacidade_maxima, horarios=HORARIOS):
        super().__init__(nome, codigo, capacidade_maxima, horarios)
        self.disciplinas = []

    #Getter#
    def get_lista_de_disciplinas (self):
        return self.lista_de_disciplinas

    def cria_aula (disciplina):
        pass