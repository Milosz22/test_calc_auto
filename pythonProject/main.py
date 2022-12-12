


def calc():
    print("wypisz dwie liczby")
    x = input()
    y = input()
    while True:

        try:
            x=int(x)
            y=int(y)
        except:
            print("Zle dane, podaj poprawne (integery):")

            x = input()
            y = input()
        else:
            break


    print("wybierz operacje +, - , * ,/ : ")
    operacje = ['+', '-', '*', '/']


    while True:
        op = str(input())
        if op in operacje:
            break
        print("Podales niepoprawna operacje, podaj poprawna:")


    w=wynik(x, y, op)
    print("wynik to: "+str(w))

    return w



def wynik(x, y, op):
    operacje = ['+', '-', '*', '/']
    if op == '+':
        return x + y
    if op == '-':
        return x - y
    if op == '*':
        return x * y
    if op == '/':
        return x / y

    raise Exception("Podales zla operacje")
    return "Something wrong"


#calc()








