import random
import datetime

def menu():
    nome_arq = 'log.txt'
    while True:
        print ('monitor logpy')
        print ('1 - gerar logs')
        print ('2 - analisar logs')
        print ('3 - gerar e analisar logs')
        print (' 4 - sair')
        opção = input ('escolhar um opção: ')
        if opção == '1':
            try:
                qtd = int(input(' Quantidade de logs'))
                gerarArquivo(nome_arq,qtd)
            except:
                print ('qtd incorreta')
        elif opção == "2":
            analisarlog(nome_arq)
        elif opção ==  '3':
            try:
                qtd = int(input(' Quantidade de logs'))
                gerarArquivo(nome_arq, qtd)
                analisarlog (nome_arq)
            except:
                print ('qtd incorreta')
        elif opção == '4':
            print ('Até mais')
            break
        else:
            print ('Opção errada')

def gerarArquivo (nome_arq, qtd):
    with open(nome_arq, 'w', encoding= 'UTF-8') as arq:
        for i in range(qtd):
            arq.write (montarlog(1)+ '\n' )
        print ('logs gerados')

def montarlog (i):
    data = gerarDataHora (i)
    ip = gerarIp(i)
    recurso = gerarRecurso(i)
    metodo = gerarMetodo(i)
    status = gerarStatus(i)
    tempo = gerarTempo (i)
    agente = gerarAgente(i)
    return f'[{data}] {ip} - {metodo} - {status} - {recurso} - {tempo} ms -500mb - HTTP/1.1 - {agente} - /home'

def gerarDataHora(i):
    base = datetime.datetime (2026, 3, 30, 22, 8, 0)
    data = datetime.timedelta (seconds=i * random.randint(5,20))
    return (base + data.strftime ('%d/%m/%y %H:%M:%S'))

def gerarIp(i):
    r = random.randint (1,6)

    if i <= 20 and i <= 30:
        return '200.0.111.345'
    
    if r == 1:
        return '192.658.9.4'
    if r == 2:
        return '192.658.9.4'
    if r == 3:
        return '192.658.9.4'
    if r == 4:
        return '192.658.9.4'
    if r == 5:
        return '192.658.9.4'
    else:
        return '192.658.9.4'


