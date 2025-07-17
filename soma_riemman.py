from math import *

expressao = input("Digite a função f(x): ")

def f(x):
    return eval(expressao, {"_builtins_": None}, {
        "x": x, "sin": sin, "cos": cos, "tan": tan,
        "exp": exp, "log": log, "sqrt": sqrt,
        "pi": pi, "e": e
    })

a = float(input("Limite inferior a: "))
b = float(input("Limite superior b: "))
n = int(input("Número de subintervalos n: "))

dx = (b - a) / n
soma = 0

for i in range(n):
    xi = a + (i + 0.5) * dx  # ponto médio do subintervalo
    soma += f(xi) * dx

print(f"Soma de Riemann (ponto médio): {soma}")