#Importar as classes para o sistema principal organizador
from Aluno import Aluno
from Disciplina import Disciplina
from Organizacao import Organizacao
from Associado import Associado
from Professor import Professor
from SalaDeAula import SalaDeAula
################################################

#Codigo de funcionamento do sistema

class Sistema:
    def __init__(self):
        self.alunos = []
        self.professores = []
        self.salasDeAula = []
        self.disciplinas = []
    
    ############################################################################################
    
    #Getters#

    def get_lista_de_alunos_do_sistema (self):
        return self.alunos

    def get_lista_de_professores_do_sistema (self):
        return self.professores
    
    def get_lista_de_disciplinas_do_sistema (self):
        return self.disciplinas

    def get_lista_de_salas_de_aulas_do_sistema(self):
        return self.salasDeAula

    #Imprimir listas#

    #Imprime lista aluno
    def imprime_lista_de_alunos_do_sistema(self):
        print(f'{len(self.alunos)} existente(s): ')
        for aluno in self.alunos:
            print(aluno)

    #Imprime lista professor
    def imprime_lista_de_professores_do_sistema(self):
        print(f'{len(self.professores)} existente(s): ')
        for professor in self.professores:
            print(professor)


    #Imprime lista de sala de aulas
    def imprime_lista_de_salas_de_aula(self):
        print(f'{len(self.salasDeAula)} existente(s): ')
        for salas_de_aula in self.salasDeAula:
            print(salas_de_aula)

    #Imprime lista de Disciplinas

    def imprime_lista_de_disciplinas(self):
        print(f'{len(self.disciplinas)} existente(s): ')
        for disciplina in self.disciplinas:
            print(disciplina)

    def imprime_lista_de_professores_do_sistema(self):
        print(f'{len(self.professores)} existente(s): ')
        for professor in self.professores:
            print(professor)


    #Acessar dados Únicos

    #Aluno

    def acessar_aluno (self):
        
        identidade = int(input('Digite a identidade do Aluno: '))

        #Acessar Aluno
        for aluno in self.alunos:
            if aluno.get_identidade() == identidade:

                if len(aluno.disciplina) != 0:
                    print('O aluno está inscrito nas seguintes disciplinas:')
                    for disciplina in aluno.disciplina:
                        print(disciplina.nome)

                print(aluno)
                
            else:
                print('Aluno não encontrado!')

    #Professor

    def acessar_professor (self):
        
        identidade = int(input('Digite a identidade do Professor: '))

        #Acessar Professor

        for professor in self.professores:
            if professor.get_identidade() == identidade:
                if len(professor.disciplina) != 0:
                    print('O professor encontra-se responsável pela seguinte disciplina:')
                    for disciplina in professor.disciplina:
                        print(disciplina.nome)

                print(professor)
            else:
                print('Professor não encontrado!')    

    #Sala de Aula

    def acessar_sala_de_aula(self):

        codigo = int(input('Digite o codgio da sala de aula: '))
        
        #Acessar Sala de Aula
        for sala_de_aula in self.salasDeAula:
            if sala_de_aula.get_codigo() == codigo:
                if len(sala_de_aula.discipllinas) != 0:
                    print('Essa sala possui as seguintes disciplinas')
                    for disciplina in sala_de_aula.disciplinas:
                        print(disciplina.nome)

                print(sala_de_aula)
                print(sala_de_aula.HORARIOS)
            else:
                print('Sala de Aula não encontrado!')

    #Disciplina.Sala de Aula, 

    def acessar_disciplina(self):

        codigo = int(input('Digite o codgio da Disciplina: '))
        
        #Acessar Disciplina

        for disciplina in self.disciplinas:
            if disciplina.get_codigo() == codigo:
                if len(disciplina.lista_de_alunos) != 0:
                    for aluno in disciplina.lista_de_alunos:
                        print('Esses sao os Alunos da disciplina:')
                        print(aluno)

                if disciplina.professor != None:
                    print(disciplina.professor)
                else:
                    print('Essa disciplina não tem professor associado')

                if disciplina.sala_de_aula != None:
                    print (disciplina.sala_de_aula)

                print(disciplina)

            else:
                print('Sala de Aula não encontrado!')

 
    # Cadastrar/Excluir Dados do Sistema

    #Criar Aluno#
    def criar_aluno (self):
        nome = input('Digite o nome do Aluno: ')

        if len(self.alunos) == 0:
            identidade = 0
        else:
            identidade = self.alunos[-1].get_identidade() + 1

        aluno = Aluno(nome,identidade)
        self.alunos.append(aluno)

        print(f'Aluno adicionado com sucesso!')
        print(f'Aluno adicionado:{nome}, Identidade: {identidade}')


    # Excluir Aluno #
    def excluir_aluno (self):
        identidade = int(input('Digite a identidade do aluno: '))

        for aluno in self.alunos:
            if identidade == aluno.get_identidade():
                aluno_excluido = self.alunos.pop(self.alunos.index(aluno))
                print('Aluno excluido com sucesso!')
                print(f'Aluno excluido: {aluno_excluido.get_nome()} Identidade: {aluno_excluido.get_identidade()}',)


    #Adicionar Professor
    def criar_professor (self):
        nome = input('Digite o nome do Professor: ')

        if len(self.professores) == 0:
            identidade = 0
        else:
            identidade = self.professores[-1].get_identidade() + 1

        professor = Professor(nome,identidade)
        self.professores.append(professor)

        print(f'Professor adicionado com sucesso!')
        print(f'Professor adicionado:{nome}, Identidade: {identidade}')

    #Excluir Professor
    def excluir_professor (self):
        identidade = int(input('Digite a identidade do professor: '))

        for professor in self.professores:
            if identidade == professor.get_identidade():
                professor_excluido = self.professores.pop(self.professores.index(professor))
                print('Professor excluido com sucesso!')
                print(f'Professor excluido: {professor_excluido.get_nome()} Identidade: {professor_excluido.get_identidade()}')
            
    
    # Criar Disciplina
    def criar_disciplina (self): 
        nome = input('Digite o nome da disciplina: ')

        #Conferindo se a disciplina já existe
        for disciplina in self.disciplinas:
            if disciplina.get_nome().lower() == nome.lower():
                print('A disciplina já existe! Digite outro nome de disciplina para adicionar')
                break
        
        if len(self.disciplinas) == 0:
            codigo = 0
        else:
            codigo = self.disciplinas[-1].get_codigo() + 1
        
        disciplina = Disciplina(nome,codigo)

        print(f'Disciplina adicionado com sucesso!')
        print(f'Disciplina adicionada:{nome}, Codigo: {codigo}')

        self.disciplinas.append(disciplina)

    #Excluir Disciplina
    def excluir_disciplina (self):
        nome = input('Digite o nome da disciplina que deseja excluir: ')

        for disciplina in self.disciplinas:
            if disciplina.get_nome().lower() == nome.lower():
                disciplina_excluida = self.disciplinas.pop(self.disciplinas.inde(disciplina))
                print('Disciplina excluido com sucesso!')
                print(f'Disciplina excluida: {disciplina_excluida.get_nome()} Código: {disciplina_excluida.get_codigo()}')


    # Criar Sala de Aula 
    def criar_sala_de_aula (self):


        nome = input('Digite o nome da Sala: ')
        capacidade_maxima = int('Digite a capacidade máxima: ')
        
        # Conferindo se a Sala já existe 

        for sala_de_aula in self.salasDeAula:
            
            if sala_de_aula.get_nome.lower() == nome.lower():
                print('Essa sala de aula já existe!')
                break


        
        if len(self.salasDeAula) == 0:
            codigo = 0
        else:
            codigo = self.salasDeAula[-1].get_codigo() + 1

        sala_de_aula = SalaDeAula(nome,codigo,capacidade_maxima)

        print(f'Sala de Aula adicionada com sucesso!')
        print(f'Sala de Aula adicionada:{nome}, Codigo: {codigo}')

        self.salasDeAula.append(sala_de_aula)

    #Excluir Sala de Aula
    def excluir_sala_de_aula (self):

        nome = input('Digite o nome da sala: ')

        for sala_de_aula in self.salasDeAula:
            if sala_de_aula.get_nome().lower() == nome.lower():
                disciplina_excluida = self.salasDeAula.pop(self.salasDeAula.index(sala_de_aula))
                print('Sala de Aula excluída com sucesso!')
                print(f'Sala de Aula: {disciplina_excluida.get_nome()} Código: {disciplina_excluida.get_codigo()}')


    #Alterar dados

    #Alterar dado de Aluno. Nome ou Identidade 

        #Alterar Nome do Aluno

    def alterar_nome_aluno (self):

        identidade_aluno = int(input('Digite a identidade do aluno: '))

        novo_nome = input('Digite o novo nome: ')
        
        for aluno in self.alunos:
            if aluno.get_identidade == identidade_aluno:
                aluno.set_nome(novo_nome)

                print('Nome alterado com sucesso!')
                print(aluno)

        #Alterar Identidade do Aluno

    def alterar_identidade_do_aluno(self):

            identidade_aluno = int(input('Digite identidade do aluno: '))
            nova_identidade = int(input('Digite a nova identidade do aluno: '))
        
            #Verificar se nova identidade será válida

            for aluno in self.alunos:

                if nova_identidade == aluno.get_identidade():
                    print('Essa identidade nova nâo pode ser atribuída pois ela já existe!')
                    break
            
                aluno.set_identidade(nova_identidade)
                print('Identidade Alterada!')
                print(f'Nova identidade: {aluno.get_identidade()}')


    #Alterar Dados do Professor. Nome ou Identidade 

        #Alterar Nome do Professor

    def alterar_nome_professor (self):

        identidade_professor = int(input('Digite a identidade do professor: '))

        novo_nome = input('Digite o novo nome: ')
        
        for professor in self.professores:
            if professor.get_identidade == identidade_professor:
                professor.set_nome(novo_nome)

                print('Nome alterado com sucesso!')
                print(professor)

        #Alterar Identidade do Professor

    def alterar_identidade_do_professor(self):

            identidade_professor = int(input('Digite identidade do professor: '))
            nova_identidade = int(input('Digite a nova identidade do professor: '))
        
            #Verificar se nova identidade será válida

            for professor in self.professores:

                if nova_identidade == professor.get_identidade():
                    print('Essa identidade nova nâo pode ser atribuída pois ela já existe!')
                    break
            
                professor.set_identidade(nova_identidade)
                print('Identidade Alterada!')
                print(f'Nova identidade: {professor.get_identidade()}')



        #Alterar dados de Disciplina. Nome, Codigo e Capacidade Maxima

    def alterar_nome_disciplina (self):

            codigo = int(input('Digite o codigo da Disciplina: '))
            novo_nome = input('Digite o novo nome da Disciplina: ')

            for disciplina in self.disciplinas:
                if disciplina.get_codigo == codigo:
                    disciplina.set_nome(novo_nome)
                    print('O novo nome é {}'.format(novo_nome))

    def alterar_codigo_disciplina (self):

            codigo = int(input('Digite o codigo da Disciplina: '))
            novo_codigo = input('Digite o novo codigo da Disciplina: ')

            #Avaliar se novo código é válido

            for disciplina in self.disciplinas:

                if novo_codigo == disciplina.get_codigo():
                    print('Esse codigo novo nâo pode ser atribuído pois ele já existe!')
                    break

                disciplina.set_codigo(novo_codigo)
                print('Você alterou o código!')
                print(f'O novo código é {novo_codigo}')

    def alterar_capacidade_maxima_disciplina (self):

            codigo = int(input('Digite o código da disciplina: '))
            
            nova_capacidade_maxima = int(input('Digite a nova capacidade máxima: '))

            for disciplina in self.disciplinas:
                if disciplina.get_codigo == codigo:
                    disciplina.set_capacidade_maxima(nova_capacidade_maxima)
                    print(f'A nova capacidade é de {nova_capacidade_maxima}')

        
        #Alterar dados da Sala de Aula. Nome, Codigo e Capacidade Maxima.

    def alterar_nome_sala_de_aula (self):

            codigo = int(input('Digite o codigo da Sala de Aula: '))
            novo_nome = input('Digite o novo nome da Sala de Aula: ')

            for sala_de_aula in self.salasDeAula:
                if sala_de_aula.get_codigo == codigo:
                    sala_de_aula.set_nome(novo_nome)
                    print('O novo nome é {}'.format(novo_nome))

    def alterar_codigo_da_sala_de_aula (self):

            codigo = int(input('Digite o codigo da Sala de Aula: '))
            novo_codigo = input('Digite o novo codigo da Sala de Aula: ')

            #Avaliar se novo código é válido

            for sala_de_aula in self.salasDeAula:

                if novo_codigo == sala_de_aula.get_codigo():
                    print('Esse codigo novo nâo pode ser atribuído pois ele já existe!')
                    break

                sala_de_aula.set_codigo(novo_codigo)
                print('Você alterou o código!')
                print(f'O novo código é {novo_codigo}')

    def alterar_capacidade_maxima_sala_de_aula (self):

            codigo = int(input('Digite o código da Sala de Aula: '))
            
            nova_capacidade_maxima = int(input('Digite a nova capacidade máxima: '))

            for sala_de_aula in self.salasDeAula:
                if sala_de_aula.get_codigo == codigo:
                    sala_de_aula.set_capacidade_maxima(nova_capacidade_maxima)
                    print(f'A nova capacidade é de {nova_capacidade_maxima}')


    


#Associar um Aluno, Professor e Sala de Aula a uma Disciplina sem tratamento de exceção

#Aluno em Disciplina
    def associar_aluno_disciplina(self):

        identidade_aluno = int(input('Digite a identidade do aluno que deseja adicionar: '))
        codigo_disciplina = int(input('Digite o código da Disciplina que deseja associar o aluno: '))

        for aluno in self.alunos:
            if aluno.get_identidade() == identidade_aluno:
                aluno = aluno
            for disciplina in self.disciplinas:
                if codigo_disciplina == disciplina.get_codigo():
                    disciplina.set_aluno(aluno)
                    print('Aluno adicionado:')
                    print(aluno)

# Professor em Disciplina

    def associar_professor_disciplina(self):

        identidade_professor = int(input('Digite a identidade do professor que deseja adicionar: '))
        codigo_disciplina = int(input('Digite o código da Disciplina que deseja associar o professor: '))

        for professor in self.professores:
            if professor.get_identidade() == identidade_professor:
                professor = professor
            for disciplina in self.disciplinas:
                if codigo_disciplina == disciplina.get_codigo():
                    disciplina.set_professor(professor)
                    print('Professor adicionado:')
                    print(professor)

#Sala de Aula em disciplina

    def associar_sala_de_aula_disciplina(self):

        codigo_sala_de_aula= int(input('Digite o codigo da sala de aula que deseja associar: '))
        codigo_disciplina = int(input('Digite o código da Disciplina: '))

        for sala_de_aula in self.salasDeAula:
            if sala_de_aula.get_codigo() == codigo_sala_de_aula:
                sala_de_aula = sala_de_aula
            for disciplina in self.disciplinas:
                if codigo_disciplina == disciplina.get_codigo():
                    disciplina.set_sala_de_aula(sala_de_aula)
                    print('Sala adicionada:')
                    print(sala_de_aula)






#Desassociar um  Aluno, Professor e Sala de Aula a uma Disciplina sem tratamento de exceção

#Aluno
    def desassociar_aluno (self):

        identidade_aluno= int(input('Digite a identidade do aluno que deseja desassociar: '))
        codigo_disciplina = int(input('Digite o código da Disciplina: '))

        for aluno in self.alunos:#Achar Aluno
            if aluno.get_identidade() == identidade_aluno:
                aluno = aluno

            for disciplina in self.disciplinas:#Achar Disciplina
                if codigo_disciplina == disciplina.get_codigo():
                    disciplina.lista_de_alunos().pop(disciplina.lista_de_alunos.index(aluno))

#Professor

    def desassociar_professor (self):

        identidade_professor= int(input('Digite a identidade do professor que deseja desassociar: '))
        codigo_disciplina = int(input('Digite o código da Disciplina: '))

        for professor in self.professor:#Achar professor
            if professor.get_identidade() == identidade_professor:
                professor = professor

            for disciplina in self.disciplinas:#Achar Disciplina
                if codigo_disciplina == disciplina.get_codigo():
                    disciplina.professor = None
        
# Sala de Aula
    def desassociar_sala_de_aula (self):

        codigo_sala_de_aula= int(input('Digite o codigo da sala de aula que deseja desassociar: '))
        codigo_disciplina = int(input('Digite o código da Disciplina: '))

        for sala_de_aula  in self.salasDeAula:#Achar a Sala 
            if sala_de_aula.get_codigo() == codigo_sala_de_aula:
                sala_de_aula = sala_de_aula

            for disciplina in self.disciplinas:#Achar Disciplina
                if codigo_disciplina == disciplina.get_codigo():
                    disciplina.salaDeAula = None
                    sala_de_aula.disciplinas.pop(sala_de_aula.disciplinas.index(disciplina))
    

      

    
