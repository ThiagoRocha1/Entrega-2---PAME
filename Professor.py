from Associado import Associado


class Professor(Associado):
        def __init__(self,nome,identidade):
               super().__init__(nome,identidade)
               self.ocupacao = 'Professor'