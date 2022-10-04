##https://www.beecrowd.com.br/judge/pt/custom-problems/view/1716

plano = (input())
salarioAtual = float(input())

A = 'A'
B = 'B'
C = 'C'

if plano == A:
  print(f'Novo Salário: R$%.2f' %(salarioAtual * 1.1))

if plano == B:
  print(f'Novo Salário: R$%.2f' %(salarioAtual * 1.15))

if plano == C:
  print(f'Novo Salário: R$%.2f' %(salarioAtual * 1.2))
