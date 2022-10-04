##https://www.beecrowd.com.br/judge/pt/problems/view/1009

nome = input()
salfixo = float(input())
qtdvendas = float(input())

bonus = float(qtdvendas * (15/100))

total = salfixo + bonus

print("TOTAL = R$ %0.2f" %total)