##https://www.beecrowd.com.br/judge/pt/custom-problems/view/1760

cont = 4
qtdacima = 0
idade = 0

while cont > 0:
    idade1 = int(input(""))
    peso = float(input(""))

    if peso > 90:
        qtdacima = qtdacima + 1
        idade = idade + idade1
        cont = cont - 1 

    else:
        idade = idade + idade1
        cont = cont - 1

media = idade / 4
print("Qtd pessoas > 90 Kg: %i" %(qtdacima))
print("Idade média: %.2f" %(media))