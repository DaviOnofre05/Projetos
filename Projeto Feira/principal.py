import random

pontos = acertos = pontos1 = acertos1 = 0


while True:
  
  UMresp = str(input('\033[1;32mVocê é da escola? [S/N] ')).upper().strip()[0]

  while UMresp not in 'SN':
    UMresp = str(input('\033[1;32mVocê é da escola? [S/N] ')).upper().strip()[0]

  def escol1():
    global pontos
    global acertos
    #pergunta 1, perguntas e resspostas devem ser alteradas, para a versão original
    print('\033[1;32;Qual a principal função do processador em um computador?')
    resposta1 = str(input(f'''\033[1;32m\nAlternativa certa é:
        A) Executar programas
        B) Armazenar arquivos
        C) Permitir o acesso a internet 
        D) Guardar memória temporariamente 
        Resposta: ''')).upper().strip()[0]
      
    while resposta1 not in 'ABCD':
        resposta1 = str(input('\033[1;32mDigite uma resposta válida: ')).upper().strip()[0]
      
    if resposta1 == 'A':
      print('\033[1;32mResposta correta')
      pontos += 10
      acertos += 1
    else:
      print('\033[1;32mResposta incorreta, a resposta certa era: A) Executar programas')
      
  def escol2():
    
    global pontos
    global acertos
    #pergunta 2, perguntas e resspostas devem ser alteradas, para a versão original
    print('\033[1;32mQual o nome da pessoa responsável pela biblioteca e ainda por cima é um ótimo cantor?')
    resposta2 = str(input(f'''\nAlternativa certa é:
        A) Bismuto
        B) Biscaia
        C) Bisteca
        D) Biscoito
        Resposta: ''')).upper().strip()[0]
      
    while resposta2 not in 'ABCD':
      resposta2 = str(input('\033[1;32mDigite uma resposta válida: ')).upper().strip()[0]
      
    if resposta2 == 'B':
      print('\033[1;32mResposta correta')
      pontos += 10
      acertos += 1
    else:
        print('\033[1;32mResposta incorreta, a resposta certa era: B) Biscaia')
        
  def escol3():
    
    global pontos
    global acertos
    #pergunta 3, perguntas e resspostas devem ser alteradas, para a versão original
    print('\033[1;32mQual as cores da camiseta do 3°CDS?')
    resposta3 = str(input(f'''\033[1;32m\nAlternativa certa é:
        A) Vermelho, branco e preto 
        B) Roxo, branco e preto
        C) Azul, branco e preto
        D) Azul, rosa, branco e preto
        Resposta: ''')).upper().strip()[0]
      
    while resposta3 not in 'ABCD':
        resposta3 = str(input('\033[1;32mDigite uma resposta válida: ')).upper().strip()[0]
      
    if resposta3 == 'C':
      print('\033[1;32mResposta correta')
      pontos += 10
      acertos += 1
    else:
      print('\033[1;32mResposta incorreta, a resposta certa era: C) Azul, branco e preto')

  def escol4():
    
    global pontos
    global acertos
    #pergunta 4, perguntas e resspostas devem ser alteradas, para a versão original
    print('\033[1;32mQuantos meses tem 28 dias?')
    resposta4 = str(input(f'''\033[1;32m\nAlternativa certa é:
        A) 1
        B) 2
        C) 6
        D) 12
        Resposta: ''')).upper().strip()[0]
      
    while resposta4 not in 'ABCD':
      resposta4 = str(input('\033[1;32mDigite uma resposta válida: ')).upper().strip()[0]
      
    if resposta4 == 'D':
        print('\033[1;32mResposta correta')
        pontos += 10
        acertos += 1
    else:
        print('\033[1;32mResposta incorreta, a resposta certa era: D) 12')
    
  def escol5():
    
    global pontos
    global acertos
    #pergunta 5, perguntas e resspostas devem ser alteradas, para a versão original
    print('\033[1;32mQuantos blocos tem na escola?')
    resposta5 = str(input(f'''\033[1;32m\nAlternativa certa é:
        A) 5
        B) 1
        C) 3
        D) 2
        Resposta: ''')).upper().strip()[0]
      
    while resposta5 not in 'ABCD':
      resposta5 = str(input('\033[1;32mDigite uma resposta válida: ')).upper().strip()[0]
      
    if resposta5 == 'C':
        print('\033[1;32mResposta correta')
        pontos += 10
        acertos += 1
    else:
        print('\033[1;32mResposta incorreta, a resposta certa era: C) 3')
        
#não é da escola
        
  def fora1():
    global pontos1
    global acertos1
    #pergunta 1, perguntas e resspostas devem ser alteradas, para a versão original
    print('\033[1;32mQual o nome da escola?')
    resposta1 = str(input(f'''\033[1;32m\nAlternativa certa é:
      A) Gastão Vidigal
      B) Júlio szymanski
      C) Marista
      D) Helena Watson
      Resposta: ''')).upper().strip()[0]
    
    while resposta1 not in 'ABCD':
      resposta1 = str(input('\033[1;32mDigite uma resposta válida: ')).upper().strip()[0]
    
    if resposta1 == 'B':
      print('\033[1;32mResposta correta')
      pontos1 += 10
      acertos1 += 1
    else:
      print('\033[1;32mResposta incorreta, a resposta certa era: B) Júlio szymanski')
        
  def fora2():
      
    global pontos1
    global acertos1
    #pergunta 2, perguntas e resspostas devem ser alteradas, para a versão original
    print('\033[1;32mEm qual país fica a Torre Eiffel?')
    resposta2 = str(input(f'''\033[1;32m\nAlternativa certa
      A) França 
      B) Itália 
      C) Espanha
      D) Portugal
      Resposta: ''')).upper().strip()[0]
    
    while resposta2 not in 'ABCD':
      resposta2 = str(input('\033[1;32mDigite uma resposta válida: ')).upper().strip()[0]
    
    if resposta2 == 'A':
      print('\033[1;32mResposta correta')
      pontos1 += 10
      acertos1 += 1
    else:
      print('\033[1;32mResposta incorreta, a resposta certa era: A) França')
          
  def fora3():
      
    global pontos1
    global acertos1
    #pergunta 3, perguntas e resspostas devem ser alteradas, para a versão original
    print('\033[1;32mQual é o planeta mais próximo do Sol?')
    resposta3 = str(input(f'''\033[1;32m\nAlternativa certa
      A) Marte
      B) Plutão 
      C) Mercúrio 
      D) Vênus
      Resposta: ''')).upper().strip()[0]
    
    while resposta3 not in 'ABCD':
      resposta3 = str(input('\033[1;32mDigite uma resposta válida: ')).upper().strip()[0]
    
    if resposta3 == 'C':
      print('\033[1;32mResposta correta')
      pontos1 += 10
      acertos1 += 1
    else:
      print('\033[1;32mResposta incorreta, a resposta certa era: C) Mercúrio')

  def fora4():
      
    global pontos1
    global acertos1
    #pergunta 4, perguntas e resspostas devem ser alteradas, para a versão original
    print('\033[1;32mQual é o país com maior extensão territorial?')
    resposta4 = str(input(f'''\033[1;32m\nAlternativa certa
      A) EUA
      B) Rússia
      C) Índia 
      D) China
      Resposta: ''')).upper().strip()[0]
    
    while resposta4 not in 'ABCD':
      resposta4 = str(input('\033[1;32mDigite uma resposta válida: ')).upper().strip()[0]
    
    if resposta4 == 'B':
      print('\033[1;32mResposta correta')
      pontos1 += 10
      acertos1 += 1
    else:
      print('\033[1;32mResposta incorreta, a resposta certa era: B) Rússia')
      
  def fora5():
      
    global pontos1
    global acertos1
    #pergunta 5, perguntas e resspostas devem ser alteradas, para a versão original
    print('\033[1;32mQual a principal função do processador em um computador?')
    resposta5 = str(input(f'''\033[1;32m\nAlternativa certa
      A) Guardar memória temporariamente
      B) Armazenar arquivos
      C) Permitir o acesso a internet 
      D) Executar programas 
      Resposta: ''')).upper().strip()[0]
    
    while resposta5 not in 'ABCD':
      resposta5 = str(input('\033[1;32mDigite uma resposta válida: ')).upper().strip()[0]
    
    if resposta5 == 'D':
      print('\033[1;32mResposta correta')
      pontos1 += 10
      acertos1 += 1
    else:
      print('\033[1;32mResposta incorreta, a resposta certa era: D) Executar programas')
        
  perguntas = [escol1, escol2, escol3, escol4, escol5]
  perguntas_2 = [fora1, fora2, fora3, fora4, fora5]

  random.shuffle(perguntas)
  random.shuffle(perguntas_2)

    #é da escola
  if UMresp == 'S':
    for pergunta in perguntas: 
      pergunta()
    print(f'\033[1;32mVocê acertou {acertos} perguntas e ganhou {pontos} pontos.')
    pontos = acertos = 0
      
  elif UMresp == 'N':
    for pergunta in perguntas_2:
      pergunta()
    print(f'\033[1;32mVocê acertou {acertos} perguntas e ganhou {pontos} pontos.')
    pontos1 = acertos1 = 0
  
  retorno = str(input('\033[1;32mPara recomeçar digite R: ')).upper().strip()[0]
  while retorno not in 'R':
    retorno = str(input('\033[1;32mPor favor digite algo válido para recomeçar digite R: ')).upper().strip()[0]
    
  if retorno != 'R':
        break
