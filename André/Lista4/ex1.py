##https://www.beecrowd.com.br/judge/pt/custom-problems/view/1759

atual = int(input())

valIni = 1015

anos = atual - 2006

valorSomado = 1015

contadorPorcentagem = 0.015 

somaPorcentagem = 0.01

if atual < 2006:
    print("O ano informado deverá ser > 2005!")

elif atual == 2006:
    print("Salário atual: R$%.2f"%(valIni))
    
 

elif atual > 2006:
    porcentagem = (0.015 + 0.01)
    Anterior = valIni

    for i in range(anos):
        calculo = Anterior + (Anterior * porcentagem)
        Anterior = calculo
        porcentagem = porcentagem + 0.01

        
    print("Salário atual: R$%.2f"%(calculo))
