from Organizacao import Organizacao


class Disciplina(Organizacao):

    def __init__(self, nome, codigo, capacidade_maxima):
        super().__init__(nome, codigo , capacidade_maxima)
        self.lista_de_alunos = []
        self.professor = None
        self.sala_de_aula = None

    #Getters#
    def get_lista_de_alunos (self):
        return self.lista_de_alunos

    def get_professor (self):
        return self.professor
    
    def get_sala_de_aula (self):
        return self.sala_de_aula