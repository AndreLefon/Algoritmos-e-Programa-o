##https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733

Nome = input()
QuantHora = float(input())

SalMininimo = 1192.40
HoraExtra = 10
SalHoraExtra = QuantHora * HoraExtra

SalBruto = 3 * SalMininimo + SalHoraExtra

if SalBruto > 2000:
  DescInss = SalBruto * 0.12

elif SalBruto < 2000:
  DescInss = SalBruto * 0.05

if SalBruto > 2500:
  DescIR = SalBruto * 0.2

elif SalBruto < 2500:
  DescIR = 0

DescTot = DescIR + DescInss
SalLiqui = SalBruto - DescTot

print("Nome: %s" %(Nome))
print("Salário bruto: R$%.2f" %(SalBruto))
print("Salário líquido: R$%.2f" %(SalLiqui))
