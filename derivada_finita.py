import math

print("ATENÇÃO: escreva a função usando 'math.' para funções matemáticas.")
print("Exemplos válidos:")
print("  math.sin(x)")
print("  math.log(x)")
print("  math.sqrt(x)")
print("  math.exp(x) + math.cos(x)")
print("-" * 40)

# Entrada da função e valores
funcao = input("Digite a função f(x): ")
x = float(input("Digite o valor de x: "))
h = float(input("Digite o valor de h: "))

# Verifica se h é zero
if h == 0:
    print("h não pode ser zero.")
else:
    def f(valor):
        try:
            return eval(funcao, {"_builtins_": None, "math": math, "x": valor})
        except Exception as erro:
            print(f"Erro ao calcular f({valor}): {erro}")
            return None

    # Calcula os valores de f
    f1 = f(x + h)
    f0 = f(x)
    f_1 = f(x - h)

    if None in [f1, f0, f_1]:
        print("Erro ao calcular as derivadas.")
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
