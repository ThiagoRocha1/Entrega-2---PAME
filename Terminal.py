from Disciplina import Disciplina
from Organizacao import Organizacao
from Associado import Associado
from Professor import Professor
from SalaDeAula import SalaDeAula
from Sistema import Sistema



ufrj = Sistema()

while True:

    print('Olá,seja bem vindo ao terminal!O que deseja fazer?')
    print('1 - Criar: Sala,Professor,aluno e/ou disciplina')
    print('2 - Excluir: Sala,Professor,aluno e/ou disciplina ')
    print('3 - Alterar Dados de: Sala,Professor,aluno e/ou disciplina')
    print('4 - Mostrar Dados Únicos de: Sala,Professor,aluno e/ou disciplina')
    print('5 - Imprimir: Sala,Professor,aluno e/ou disciplina ')
    print('6- Associar: Sala,Professor,aluno em disciplina')
    print('7 - Desassociar: Sala,Professor,aluno de disciplina')
    print('-1 - Sair do sistema')

    escolha = int(input('Digite sua escolha: '))

    #Criar no Sistema
    if escolha == 1:
        print('O que deseja criar? ')
        print('1- Aluno 2 - Professor 3- Sala de Aula 4-Disciplina ')

        escolha2 = int(input('Digite sua escolha: '))

        if escolha2 == 1:
            ufrj.criar_aluno()
            print('Aluno Criado')

        elif escolha2 ==2:
            ufrj.criar_professor()
            print('Professor Criado')

        elif escolha2 ==3:
            ufrj.criar_sala_de_aula()
            print('Sala de Aula criada!')

        elif escolha2 ==4:
            ufrj.criar_disciplina()
            print('Disciplina Criada!')

    #Excluir do Sistema       
    if escolha == 2:

        print('O que deseja excluir? ')
        print('1- Aluno 2 - Professor 3- Sala de Aula 4-Disciplina ')

        escolha2 = int(input('Digite sua escolha: '))

        if escolha2 == 1:
            ufrj.excluir_aluno()
            print('Excluído')

        elif escolha2 ==2:
            ufrj.excluir_professor()
            print('Professor Excluído')

        elif escolha2 ==3:
            ufrj.excluir_sala_de_aula()
            print('Sala de Aula excluída!')

        elif escolha2 ==4:
            ufrj.excluir_disciplina()
            print('Disciplina excluída!')

    #Alterar no Sistema        
    if escolha == 3:

        print('O que deseja alterar? ')
        print('1- Aluno 2 - Professor 3- Sala de Aula 4-Disciplina ')

        escolha2 = int(input('Digite sua escolha: '))

        if escolha2 == 1:#Aluno

            print('Digite o que deseja fazer com aluno: ')
            print('1- Alterar Nome 2 - Alterar Identidade')

            escolha3 = int(input('Digite sua escolha: '))

            if escolha3 == 1:
                ufrj.alterar_nome_aluno()
                print('Aluno Alterado!')

            if escolha3 == 2:
                ufrj.alterar_identidade_do_aluno()
                print('Identidade Alterada!')

        if escolha2 == 2: #Professor 

            print('Digite o que deseja fazer com Professor: ')
            print('1- Alterar Nome 2 - Alterar Identidade')

            escolha3 = int(input('Digite sua escolha: '))

            if escolha3 == 1:
                ufrj.alterar_nome_professor()
                print('Professor Alterado!')

            if escolha3 == 2:
                ufrj.alterar_identidade_do_professor()
                print('Identidade Alterada!')

        if escolha2 == 3:#Sala de Aula

            print('Digite o que deseja fazer com a Sala de Aula: ')
            print('1- Alterar Nome 2 - Alterar Código 3- Capacidade Máxima')

            escolha3 = int(input('Digite sua escolha: '))

            if escolha3 == 1:
                ufrj.alterar_nome_sala_de_aula()
                print('Aluno Alterado!')

            if escolha3 == 2:
                ufrj.alterar_codigo_da_sala_de_aula()
                print('Código Alterado!')

            if escolha3 == 3:
                ufrj.alterar_capacidade_maxima_sala_de_aula()
                print('Capacidade Máxima Alterada!')

        if escolha2 == 4:#Disciplina

            print('Digite o que deseja fazer com a Disciplina: ')
            print('1- Alterar Nome 2 - Alterar Código 3- Capacidade Máxima')

            escolha3 = int(input('Digite sua escolha: '))

            if escolha3 == 1:
                ufrj.alterar_nome_disciplina()
                print('Aluno Alterado!')

            if escolha3 == 2:
                ufrj.alterar_codigo_disciplina()
                print('Código Alterado!')

            if escolha3 == 3:
                ufrj.alterar_capacidade_maxima_disciplina()
                print('Capacidade Máxima Alterada!')            

    #Mostrar Dados Únicos
    if escolha == 4:

        print('O que deseja acessar? ')
        print('1- Aluno 2 - Professor 3- Sala de Aula 4-Disciplina ')

        escolha2 = int(input('Digite sua escolha: '))

        if escolha2 == 1: #Aluno
            ufrj.acessar_aluno()
            print('Acessado')

        elif escolha2 ==2: #Professor
            ufrj.acessar_professor()
            print('Acessado')

        elif escolha2 ==3: #Sala de Aula
            ufrj.acessar_sala_de_aula()
            print('Acessado')

        elif escolha2 ==4: #Disciplina
            ufrj.acessar_disciplina()
            print('Acessado')        
    #imprimir Lista
    if escolha == 5:

        print('O que deseja imprimir? ')
        print('1- Aluno 2 - Professor 3- Sala de Aula 4-Disciplina ')

        escolha2 = int(input('Digite sua escolha: '))

        if escolha2 == 1: #Aluno
            ufrj.imprime_lista_de_alunos_do_sistema
            print('Impresso')

        elif escolha2 ==2: #Professor
            ufrj.imprime_lista_de_professores_do_sistema()
            print('Impresso')

        elif escolha2 ==3: #Sala de Aula
            ufrj.imprime_lista_de_salas_de_aula()
            print('Impresso')

        elif escolha2 ==4: #Disciplina
            ufrj.imprime_lista_de_disciplinas()
            print('Impresso')               
    #Associar
    if escolha == 6:

        print('O que deseja Associar ')
        print('1- Aluno 2 - Professor 3- Sala de Aula')

        escolha2 = int(input('Digite sua escolha: '))

        if escolha2 == 1: #Aluno
            ufrj.associar_aluno_disciplina()
            print('Associado')

        elif escolha2 ==2: #Professor
            ufrj.associar_professor_disciplina()
            print('Associado')

        elif escolha2 ==3: #Sala de Aula
            ufrj.associar_sala_de_aula_disciplina()
            print('Associada')
        

    #Desassociar
    if escolha == 7:

        print('O que deseja desassociar ')
        print('1- Aluno 2 - Professor 3- Sala de Aula')

        escolha2 = int(input('Digite sua escolha: '))

        if escolha2 == 1: #Aluno
            ufrj.desassociar_aluno()
            print('Desassociado')

        elif escolha2 ==2: #Professor
            ufrj.desassociar_professor()
            print('Desassociado')

        elif escolha2 ==3: #Sala de Aula
            ufrj.desassociar_sala_de_aula()
            print('Desassociada')

    if escolha == -1:
        print('Até a próxima!')
        break
