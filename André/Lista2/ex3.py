##https://www.beecrowd.com.br/judge/pt/custom-problems/view/1714

Compra = float(input())
if Compra < 20:
  print(f'Valor de venda: R$%.2f' %(Compra * 1.45))
else:
  print(f'Valor de venda: R$%.2f' %(Compra * 1.3))
