##https://www.beecrowd.com.br/judge/pt/custom-problems/view/1715

tipoCliente = int(input())
valorInicial = float(input())

if tipoCliente == 1:
  print(f'Valor total a ser pago: R$%.2f' %(valorInicial * 1))

if tipoCliente == 2:
  print(f'Valor total a ser pago: R$%.2f' %(valorInicial * 0.87))

if tipoCliente == 3:
  print(f'Valor total a ser pago: R$%.2f' %(valorInicial * 0.93))

else:
  print('OPÇÃO INVÁLIDA!')