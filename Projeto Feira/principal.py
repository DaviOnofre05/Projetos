
pontos = 0

UMresp = str(input('Você é da escola? [S/N] ')).upper().strip()[0]

while UMresp not in 'SN':
  UMresp = str(input('Você é da escola? [S/N] '))

#é da escola
if UMresp == 'S':
  #pergunta 1, perguntas e resspostas devem ser alteradas, para a versão original
  print('Pergunta 1 sobre a escola')
  resposta1 = str(input(f'''\nAlternativa certa\n[a]...\n[b]...\n[c]...\n[d]...\n[e]...\nResposta: ''')).upper().strip()[0]
  if resposta1 == 'A':
    print('Resposta correta')
    pontos += 1
  else:
    print('Resposta incorreta')
    
  #pergunta 2, perguntas e resspostas devem ser alteradas, para a versão original
  print('Pergunta 2 sobre a escola')
  resposta2 = str(input(f'''\nAlternativa certa\n[a]...\n[b]...\n[c]...\n[d]...\n[e]...\nResposta: ''')).upper().strip()[0]
  if resposta2 == 'A':
    print('Resposta correta')
    pontos += 1
  else:
    print('Resposta incorreta')
    
  #pergunta 3, perguntas e resspostas devem ser alteradas, para a versão original
  print('Pergunta 1 sobre a escola')
  resposta3 = str(input(f'''\nAlternativa certa\n[a]...\n[b]...\n[c]...\n[d]...\n[e]...\nResposta: ''')).upper().strip()[0]
  if resposta3 == 'A':
    print('Resposta correta')
    pontos += 1
  else:
    print('Resposta incorreta')
  
  #pergunta 4, perguntas e resspostas devem ser alteradas, para a versão original
  print('Pergunta 1 sobre a escola')
  resposta4 = str(input(f'''\nAlternativa certa\n[a]...\n[b]...\n[c]...\n[d]...\n[e]...\nResposta: ''')).upper().strip()[0]
  if resposta4 == 'A':
    print('Resposta correta')
    pontos += 1
  else:
    print('Resposta incorreta')

  #pergunta 5, perguntas e resspostas devem ser alteradas, para a versão original
  print('Pergunta 1 sobre a escola')
  resposta5 = str(input(f'''\nAlternativa certa\n[a]...\n[b]...\n[c]...\n[d]...\n[e]...\nResposta: ''')).upper().strip()[0]
  if resposta5 == 'A':
    print('Resposta correta')
    pontos += 1
  else:
    print('Resposta incorreta')

#não é da escola
else:
   #pergunta 1, perguntas e resspostas devem ser alteradas, para a versão original
  print('Pergunta 1 sobre a escola')
  resposta1 = str(input(f'''\nAlternativa certa\n[a]...\n[b]...\n[c]...\n[d]...\n[e]...\nResposta: ''')).upper().strip()[0]
  if resposta1 == 'A':
    print('Resposta correta')
    pontos += 1
  else:
    print('Resposta incorreta')
    
  #pergunta 2, perguntas e resspostas devem ser alteradas, para a versão original
  print('Pergunta 2 sobre a escola')
  resposta2 = str(input(f'''\nAlternativa certa\n[a]...\n[b]...\n[c]...\n[d]...\n[e]...\nResposta: ''')).upper().strip()[0]
  if resposta2 == 'A':
    print('Resposta correta')
    pontos += 1
  else:
    print('Resposta incorreta')
    
  #pergunta 3, perguntas e resspostas devem ser alteradas, para a versão original
  print('Pergunta 1 sobre a escola')
  resposta3 = str(input(f'''\nAlternativa certa\n[a]...\n[b]...\n[c]...\n[d]...\n[e]...\nResposta: ''')).upper().strip()[0]
  if resposta3 == 'A':
    print('Resposta correta')
    pontos += 1
  else:
    print('Resposta incorreta')
  
  #pergunta 4, perguntas e resspostas devem ser alteradas, para a versão original
  print('Pergunta 1 sobre a escola')
  resposta4 = str(input(f'''\nAlternativa certa\n[a]...\n[b]...\n[c]...\n[d]...\n[e]...\nResposta: ''')).upper().strip()[0]
  if resposta4 == 'A':
    print('Resposta correta')
    pontos += 1
  else:
    print('Resposta incorreta')

  #pergunta 5, perguntas e resspostas devem ser alteradas, para a versão original
  print('Pergunta 1 sobre a escola')
  resposta5 = str(input(f'''\nAlternativa certa\n[a]...\n[b]...\n[c]...\n[d]...\n[e]...\nResposta: ''')).upper().strip()[0]
  if resposta5 == 'A':
    print('Resposta correta')
    pontos += 1
  else:
    print('Resposta incorreta')
    
print(f'Vc acertou {pontos} pontos. Parabéns!!!')
  
print('FIM')
