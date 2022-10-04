##https://www.beecrowd.com.br/judge/pt/custom-problems/view/1761

Compras = 0
troco = 0
while True:
    n = float(input(''))
    if n == 0:
        n1 = float(input(''))
        troco = n1 - Compras
        break
    else:
        Compras = Compras + n
print("Total da compra: R$%.2f"%(Compras))
print("Valor pago: R$%.2f"%(n1))
print("Troco: R$%.2f"%(troco))