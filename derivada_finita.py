funcao = input("Digite a função f(x): ")
x = float(input("Digite o valor de x: "))
h = float(input("Digite o valor de h: "))

if h == 0:
    print("h não pode ser zero.")
else:
    def f(x):
        try:
            return eval(funcao)
        except:
            print(f"Erro ao calcular f({x})")
            return None

    f1 = f(x + h)
    f0 = f(x)
    f_1 = f(x - h)

    if None in [f1, f0, f_1]:
        print("Não foi possível calcular as derivadas.")
    else:
        prog = (f1 - f0) / h
        retr = (f0 - f_1) / h
        cent = (f1 - f_1) / (2 * h)
        segunda = (f1 - 2*f0 + f_1) / (h**2)

        print("\nDerivadas aproximadas:")
        print("Progressiva:", prog)
        print("Retrogada  :", retr)
        print("Central    :", cent)
        print("2ª derivada:", segunda)
