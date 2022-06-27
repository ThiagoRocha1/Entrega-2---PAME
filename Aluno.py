from Associado import Associado

class Aluno (Associado):

	def __init__(self,nome,identidade):
		super().__init__(nome,identidade)
		self.ocupacao = 'Aluno'