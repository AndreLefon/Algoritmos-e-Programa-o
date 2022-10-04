##https://www.beecrowd.com.br/judge/pt/custom-problems/view/1734

def main():
    n = int(input(" "))
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1

    print("%i! =" %n, fat)


main()