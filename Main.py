#Esse é um programa para um controle de estoque e comercio de truffas.q
#Criador: Matheus Possidônio Gonçalves Vieira Costa.
#algumas das funções do programa:
#1 armazenar um estoque de produtor que pode ser acessado quando quiser.
#2 ele avalia o que é necessario comprar para  fazer a media de truffas. 
#3 ele pode alterar as quantidades de produtos do estoque sempre que necessario. 
#4 ele recebe uma quantidade de truffas para uma encomenda e informa se ha material suficiente para produzir essa encomenda. 
#5 ele é capaz de informar com base na sua produçao de trufas e de dias de trabalho informar quantas trufas voce tem que vender pelo menos em cada dia de trabalho alem de informar quanto sera o seu lucro apos a venda de todas as trufas

#OBSERVAÇÃO: A MEDIA DE PRODUTOS UTILIZADOS PARA PRODUZIR 300 TRUFFAS QUE É A MINHA MEDIA É: 6 PACOTES DE AMENDOIM, 6 PACOTES DE COCO, 6 PACOTES DE ACHOCOLATADO, 6 BARRAS DE CHOCOLATE, 20 CAIXAS DE LEITE CONDENSADO, 3 PACOTES DE ETIQUETAS, 3 PACOTES DE EMBALAGEM E 3 POTES DE MANTEIGA.
#Melhorias:
# -adicionar a funçao de cadastrar novas constantes para a media de uso
# -transformar a verificação de produtos para retirar o excesso de if e usar um laço para percorrer
# -ser possivel adcionar e retirar valores do dicionario
# -fazer calculos para valores de rendimento e lucros


#estoque de produtos
estoque={'amendoim':5,'coco':5,'achocolatado':5,'barra_de_chocolate':20,'leite_condensado':30,'embalagem':5,'etiquetas':5,'manteiga':0}


#função utilizada
def tela_inicial():
  print('-'*50)
  print('BEM VINDO AO PROGRAMA DE CONTROLE DAS TRUFFAS')
  print(' 1- VER O ESTOQUE ATUAL\n 2- COMPRAS PARA ESTOQUE\n 3- ALTERAR ESTOQUE ATUAL\n 4- ENCOMENDA DE TRUFFAS\n 5- VENDA DE TRUFFAS \n 6- FECHAR O PROGRAMA')
  print('-'*50)
  print('\n \n ')


#funçao para adicionar diretamente a quantidade de produto usado em media ao estoque, afim de poupar esforco de ter que alterar um de cada vez.
def media_estoque_adicionada():
  estoque['amendoim']=estoque['amendoim']+6
  estoque['coco']=estoque['coco']+6
  estoque['achocolatado']=estoque['achocolatado']+6
  estoque['barra_de_chocolate']=estoque['barra_de_chocolate']+10
  estoque['leite_condensado']=estoque['leite_condensado']+20
  estoque['embalagem']=estoque['embalagem']+3
  estoque['etiquetas']=estoque['etiquetas']+3
  estoque['manteiga']=estoque['manteiga']+3


#funçao para retirar diretamente a quantidade de produto usado em media ao estoque, afim de poupar esforco de ter que alterar um de cada vez.
def media_estoque_retirada():
  estoque['amendoim']=estoque['amendoim']-6
  estoque['coco']=estoque['coco']-6
  estoque['achocolatado']=estoque['achocolatado']-6
  estoque['barra_de_chocolate']=estoque['barra_de_chocolate']-10
  estoque['leite_condensado']=estoque['leite_condensado']-20
  estoque['embalagem']=estoque['embalagem']-3
  estoque['etiquetas']=estoque['etiquetas']-3
  estoque['manteiga']=estoque['manteiga']-3


#função para realizar encomendas de truffas,porde ser um pouco feio por conta de condições dentro de condiçoes mas foi a melhor maneira que consegui pensar.
def encomenda_truffa():

  if truffa_amendoim*0.02<=estoque['amendoim']:
  
    if truffa_coco*0.02<=estoque["coco"]:
    
      if truffa_achocolatado*0.02<=estoque["achocolatado"]:
      
        if truffa_total*0.02<=estoque["barra_de_chocolate"]:
        
          if truffa_total*0.06<=estoque["leite_condensado"]:
          
            if truffa_total*0.01<=estoque["etiquetas"]:
            
              if truffa_total*0.01<=estoque["embalagem"]:
              
                if truffa_total*0.01<=estoque["manteiga"]:
                  print('°VOCÊ POSSUI TODO O MATERIAL PARA FAZER AS TRUFAS DESSA ENCOMENDA \n')


              
                else:
                  print('°NÃO POSSUI MANTEIGA  SUFICIENTE NO ESTOQUE PARA FAZER ESSA ENCOMENDA \n ')
            
              else:
               print('°NÃO POSSUI EMBALAGEM  SUFICIENTE NO ESTOQUE PARA FAZER ESSA ENCOMENDA \n  ')
          
            else:
             print('°NÃO POSSUI ETIQUETAS  SUFICIENTE NO ESTOQUE PARA FAZER ESSA ENCOMENDA \n ')
        
          else:
           print('°NÃO POSSUI LEITE CONDENSADO  SUFICIENTE NO ESTOQUE PARA FAZER ESSA ENCOMENDA \n ')
      
        else:
          print('°NÃO POSSUI BARRAS DE CHOCOLATE  SUFICIENTE NO ESTOQUE PARA FAZER ESSA ENCOMENDA \n ')
    
      else:
       print('°NÃO POSSUI ACHOCOLATADO SUFICIENTE NO ESTOQUE PARA FAZER ESSA ENCOMENDA \n ')
  
    else:
      print('°NÃO POSSUI COCO SUFICIENTE NO ESTOQUE PARA FAZER ESSA ENCOMENDA \n  ')

  else:
    print('°NÃO POSSUI AMENDOIM SUFICIENTE NO ESTOQUE PARA FAZER ESSA ENCOMENDA \n  ')

#print de recomendação para uso para melhorar a experiencia do usuario e diminuir as falhas do programa>
print("ATENÇÃO AS RECOMENDAÇÕES:\n °UTILIZAR APENAS NUMEROS NESSE PROGRAMA.\n °ATENÇÃO AOS COMANDO REALIZADOS.\n °OBRIGADO POR UTILIZAR O PROGRAMA, BOM PROVEITO\n")

while True:
  menu_principal = str(input(tela_inicial()))
  

  #condição que mostra o estoque de produtos>
  if menu_principal == '1':
    for k,v in estoque.items():
      print(f' ° O PRODUTO {k} POSSUI A QUANTIDADE {v} \n ')
    print('\n \n')

#condição que compara o estoque com oq ele deve usar de acordo com a media e informa se precisa comprar algo ou nao.
  elif menu_principal=='2':
    if estoque['amendoim']<6:
      print(f'°É NECESSARIO COMPRAR AMENDOIM POIS POSSUI APENAS {estoque["amendoim"]} DE QUANTIDADE NO ESTOQUE \n ')
      
    if estoque['coco']<6:
      print(f'°É NECESSARIO COMPRAR COCO POIS POSSUI APENAS {estoque["coco"]} DE QUANTIDADE NO ESTOQUE \n ')

    if estoque['achocolatado']<6:
      print((f'°É NECESSARIO COMPRAR ACHOCOLATADO POIS POSSUI APENAS {estoque["achocolatado"]} DE QUANTIDADE NO ESTOQUE \n '))

    if estoque['barra_de_chocolate']<6:
      print((f'°É NECESSARIO COMPRAR BARRAS DE CHOCOLATE POIS POSSUI APENAS {estoque["barra_de_chocolate"]} DE QUANTIDADE NO ESTOQUE \n '))

    if estoque['leite_condensado']<20:
      print((f'°É NECESSARIO COMPRAR LEITE CONDENSADO POIS POSSUI APENAS {estoque["leite_condensado"]} DE QUANTIDADE NO ESTOQUE \n '))

    if estoque['embalagem']<3:
      print((f'°É NECESSARIO COMPRAR EMBALAGEM POIS POSSUI APENAS {estoque["embalagem"]} DE QUANTIDADE NO ESTOQUE \n '))

    if estoque['etiquetas']<3:
      print((f'°É NECESSARIO COMPRAR ETIQUETAS POIS POSSUI APENAS {estoque["etiquetas"]} DE QUANTIDADE NO ESTOQUE \n '))

    if estoque['manteiga']<3:
      print((f'°É NECESSARIO COMPRAR MANTEIGA POIS POSSUI APENAS {estoque["manteiga"]} DE QUANTIDADE NO ESTOQUE \n '))
    


    else:
      print('NAO E NECESSARIO COMPRAR OS MATERIAIS QUE NAO ESTAO NA LISTA ACIMA MATERIAL \n ')
    
    

 #condiçao para alterar as quantidades de produtos no estoque 
  elif menu_principal=='3':
    while True:
      alterar_estoque=str(input('. \n 1- PARA MUDAR A QUANTIDADE DE UM PRODUTO NO ESTOQUE. \n 2- PARA ADICIONAR DIRETAMENTE A QUANTIDADE DE MATERIAL USADO EM MEDIA AO ESTOQUE. \n 3- PARA RETIRAR DIRETAMENTE A QUANTIDADE DE MATERIAL USADO EM MEDIA AO ESTOQUE. \n 4- PARA VOLTAR AO MENU PRINCIPAL.\n \n'))
      if alterar_estoque=='1':
        while True:
         muda_produto=str(input("QUAL PRODUTO DESEJA ALTERAR NO ESTOQUE ?\n 1- ALTERAR A QUANTIDADE DE AMENDOIM \n 2- ATERAR A QUANTIDADE DE COCO \n 3- ATERAR A QUANTIDADE DE ACHOCOLATADO \n 4- ATERAR A QUANTIDADE DE BARRAS DE CHOCOLATE \n 5- ATERAR A QUANTIDADE DE LEITE CONDENSADO \n 6- ATERAR A QUANTIDADE DE EMBALAGEM \n 7- ATERAR A QUANTIDADE DE ETIQUETAS \n 8- ALTERAR A QUANTIDADE DE MANTEIGA \n 9- PARA CONCLUIR AS ALTERAÇÕES \n"))
         if muda_produto=='1':
           estoque['amendoim']=float(input('°INFORME A NOVA QUANTIDADE DE AMENDOIM: \n'))

         elif muda_produto=='2':
           estoque['coco']=float(input('°INFORME A NOVA QUANTIDADE DE COCO: \n'))

         elif muda_produto=='3':
           estoque['achocolatado']=float(input('°INFORME A NOVA QUANTIDADE DE ACHOCOLATADO: \n'))
           
         elif muda_produto=='4':
           estoque['barra_de_chocolate']=float(input('°INFORME A NOVA QUANTIDADE DE BARRAS DE CHOCOLATE: \n'))

         elif muda_produto=='5':
           estoque['leite_condensado']=float(input('°INFORME A NOVA QUANTIDADE DE LEITE CONDENSADO: \n'))

         elif muda_produto=='6':
           estoque['embalagem']=float(input('°INFORME A NOVA QUANTIDADE DE EMBALAGEM: \n'))

         elif muda_produto=='7':
           estoque['etiquetas']=float(input('°INFORME A NOVA QUANTIDADE DE ETIQUETAS: \n'))

         elif muda_produto=='8':
           estoque['manteiga']=float(input('°INFORME A NOVA QUANTIDADE DE MANTEIGA: \n'))

         elif muda_produto=='9':
          break

         else:
           print('°COMANDO INVÁLIDO POR FAVOR INFORME UM COMANDO VÁLIDO \n ')

      elif alterar_estoque=='2':
        while True:

         adicionar_media=str(input(' DESEJA MESMO ADICICIONAR A QUANTIDADE MEDIA DE TODOS OS PRODUTOS AO ESTOQUE ? \n 1- SIM \n 2- NÃO \n'))

         if adicionar_media=='1':
            media_estoque_adicionada()
            print('ESTOQUE ATUALIZADO COM SUCESSO\n')
            break


        
         elif adicionar_media=='2':
           break
        
         else:
           print('°COMANDO INVÁLIDO POR FAVOR INFORME UM COMANDO VÁLIDO\n')


      elif alterar_estoque=='3':
        while True:

         retirar_media=str(input(' DESEJA MESMO RETIRAR A QUANTIDADE MEDIA DE TODOS OS PRODUTOS AO ESTOQUE ? \n 1- SIM \n 2- NÃO \n'))

         if retirar_media=='1':
           media_estoque_retirada()
           print('ESTOQUE ATUALIZADO COM SUCESSO\n')
           break

        
         elif retirar_media=='2':
           break
        
         else:
           print('°COMANDO INVÁLIDO POR FAVOR INFORME UM COMANDO VÁLIDO\n')



      elif alterar_estoque=='4':
        break

      else:
         print('°COMANDO INVÁLIDO POR FAVOR INFORME UM COMANDO VÁLIDO\n')

          
#condição para ver ser se o estoque possui material para fazer as trufas de uma encomenda separada das trufas truffas vendidas na universidade
  elif menu_principal=='4':
    while True:
     encomenda=str(input('DESEJA FAZER UMA ENCOMENDA ? \n 1- SIM \n 2- NÃO \n'))
     if encomenda=='1':
        truffa_total=float(input("DIGITE QUANTAS TRUFFAS DESEJA FAZER NO TOTAL: \n "))
        truffa_amendoim=float(input("DIGITE QUANTAS TRUFFAS DESEJA FAZER DE AMENDOIM: \n "))
        truffa_coco=float(input("DIGITE QUANTAS TRUFFAS DESEJA FAZER DE COCO: \n "))
        truffa_achocolatado=float(input("DIGITE QUANTAS TRUFFAS DESEJA FAZER DE COCO: \n "))
        encomenda_truffa()
     
     elif encomenda=='2':
       break
     
     else:
       print('°COMANDO INVÁLIDO POR FAVOR INFORME UM COMANDO VÁLIDO\n')

#condição para ver quanto precisa vender por dia alem de informar quanto sera o lucro semanal 
  elif menu_principal=='5':
    print("ATENÇÃO INFORME APENAS NÚMEROS: \n ")
    truffas_produzidas=float(input('INFORME QUANTAS TRUFAS FORAM PRODUZIDAS: \n'))
    dias_de_trabalho=float(input('INFORME QUANTOS DIAS VOCÊ VAI TRABALHAR ESSA SEMANA:  \n'))
    lucro_medio= truffas_produzidas*0.3
    media=truffas_produzidas/dias_de_trabalho
    print(f'°DE ACORDO COM SUA PRODUÇÃO E DIAS QUE DESEJA TRABALHAR VOCÊ DEVE VENDER AO MENOS {media} TRUFFAS POR DIA.\n' )
    print(f'°SEU LUCRO MEDIO A PARTIR DAS TRUFAS PRODUZIDAS SERÁ DE R$ {lucro_medio} REAIS .\n')

#condição para fechar o programa 
  elif menu_principal=='6':
    print('°OBRIGADO POR UTILIZAR O PROGRAMA, VOLTE SEMPRE.\n')
    break

  else:
    print("COMANDO INVÁLIDO, POR FAVOR INSIRA UM COMANDO VÁLIDO.\n") 

#obrigado por utilizar o programa,Obs: Este programa é apenas uma base demonstrativo de algumas das funções que o nosso querido Python oferece.
#Há bem poucas funções e alguns bugs, fica a seu critério modifica-los.

