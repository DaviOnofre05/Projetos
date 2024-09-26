
pontos = acertos = 0

while True:
  
  UMresp = str(input('Você é da escola? [S/N] ')).upper().strip()[0]

  while UMresp not in 'SN':
    UMresp = str(input('Você é da escola? [S/N] ')).upper().strip()[0]
  
  #é da escola
  if UMresp == 'S':
    #pergunta 1, perguntas e resspostas devem ser alteradas, para a versão original
    print('Qual a principal função do processador em um computador?')
    resposta1 = str(input(f'''\nAlternativa certa é:
      A) Executar programas
      B) Armazenar arquivos
      C) Permitir o acesso a internet 
      D) Guardar memória temporariamente 
      Resposta: ''')).upper().strip()[0]
    if resposta1 == 'A':
      print('Resposta correta')
      pontos += 10
      acertos += 1
    else:
      print('Resposta incorreta')
      
    #pergunta 2, perguntas e resspostas devem ser alteradas, para a versão original
    print('Qual o nome da pessoa responsável pela biblioteca e ainda por cima é um ótimo cantor?')
    resposta2 = str(input(f'''\nAlternativa certa é:
      A) Bismuto
      B) Biscaia
      C) Bisteca
      D) Biscoito
      Resposta: ''')).upper().strip()[0]
    if resposta2 == 'B':
      print('Resposta correta')
      pontos += 10
      acertos += 1
    else:
      print('Resposta incorreta')
      
    #pergunta 3, perguntas e resspostas devem ser alteradas, para a versão original
    print('Qual as cores da camiseta do 3°CDS?')
    resposta3 = str(input(f'''\nAlternativa certa é:
      A) Vermelho, branco e preto 
      B) Roxo, branco e preto
      C) Azul, branco e preto
      D) Azul, rosa, branco e preto
      Resposta: ''')).upper().strip()[0]
    if resposta3 == 'C':
      print('Resposta correta')
      pontos += 10
      acertos += 1
    else:
      print('Resposta incorreta')
    
    #pergunta 4, perguntas e resspostas devem ser alteradas, para a versão original
    print('Quantos meses tem 28 dias?')
    resposta4 = str(input(f'''\nAlternativa certa é:
      A) 1
      B) 2
      C) 6
      D) 12
      Resposta: ''')).upper().strip()[0]
    if resposta4 == 'D':
      print('Resposta correta')
      pontos += 10
      acertos += 1
    else:
      print('Resposta incorreta')

    #pergunta 5, perguntas e resspostas devem ser alteradas, para a versão original
    print('Quantos blocos tem na escola?')
    resposta5 = str(input(f'''\nAlternativa certa é:
      A) 5
      B) 1
      C) 3
      D) 2
      Resposta: ''')).upper().strip()[0]
    if resposta5 == 'C':
      print('Resposta correta')
      pontos += 10
      acertos += 1
    else:
      print('Resposta incorreta')

  #não é da escola
  else:
    #pergunta 1, perguntas e resspostas devem ser alteradas, para a versão original
    print('Qual o nome da escola?')
    resposta1 = str(input(f'''\nAlternativa certa é:
      A) Gastão Vidigal
      B) Júlio szymanski
      C) Marista
      D) Helena Watson
      Resposta: ''')).upper().strip()[0]
    if resposta1 == 'B':
      print('Resposta correta')
      pontos += 10
      acertos += 1
    else:
      print('Resposta incorreta')
      
    #pergunta 2, perguntas e resspostas devem ser alteradas, para a versão original
    print('Em qual país fica a Torre Eiffel?')
    resposta2 = str(input(f'''\nAlternativa certa
      A) França 
      B) Itália 
      C) Espanha
      D) Portugal
      Resposta: ''')).upper().strip()[0]
    if resposta2 == 'A':
      print('Resposta correta')
      pontos += 10
      acertos += 1
    else:
      print('Resposta incorreta')
      
    #pergunta 3, perguntas e resspostas devem ser alteradas, para a versão original
    print('Qual é o planeta mais próximo do Sol?')
    resposta3 = str(input(f'''\nAlternativa certa
      A) Marte
      B) Plutão 
      C) Mercúrio 
      D) Vênus
      Resposta: ''')).upper().strip()[0]
    if resposta3 == 'C':
      print('Resposta correta')
      pontos += 0
      acertos += 1
    else:
      print('Resposta incorreta')
    
    #pergunta 4, perguntas e resspostas devem ser alteradas, para a versão original
    print('Qual é o país com maior extensão territorial?')
    resposta4 = str(input(f'''\nAlternativa certa
      A) EUA
      B) Rússia
      C) Índia 
      D) China
      Resposta: ''')).upper().strip()[0]
    if resposta4 == 'B':
      print('Resposta correta')
      pontos += 10
      acertos += 1
    else:
      print('Resposta incorreta')

    #pergunta 5, perguntas e resspostas devem ser alteradas, para a versão original
    print('Qual a principal função do processador em um computador?')
    resposta5 = str(input(f'''\nAlternativa certa
      A) Guardar memória temporariamente
      B) Armazenar arquivos
      C) Permitir o acesso a internet 
      D) Executar programas 
      Resposta: ''')).upper().strip()[0]
    if resposta5 == 'D':
      print('Resposta correta')
      pontos += 10
      acertos += 1
    else:
      print('Resposta incorreta')
      
  print(f'Vc acertou {acertos} e ganhou {pontos} pontos. Parabéns!!!')
    
  retorno = str(input('Para recomeçar digite R: ')).upper().strip()[0]
  while retorno not in 'R':
    retorno = str(input('Por favor digite algo válido para recomeçar digite R: ')).upper().strip()[0]
  
  if retorno != 'R':
      break

print('FIM')
