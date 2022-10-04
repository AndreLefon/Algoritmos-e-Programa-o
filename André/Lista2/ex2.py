##https://www.beecrowd.com.br/judge/pt/custom-problems/view/1713

ganhoHora = float(input())
horas = float(input())
salarioBruto = ganhoHora * horas
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
impostoRenda = salarioBruto * 0.11
salarioLiquido = salarioBruto - (inss  + sindicato + impostoRenda)
print('Salário bruto: R$ %.2f' %(salarioBruto))
print('Imposto: R$ %.2f ' %(impostoRenda))
print('INSS: R$ %.2f ' %(inss))
print('Sindicato: R$ %.2f ' %(sindicato))
print('Líquido: R$ %.2f ' %(salarioLiquido))