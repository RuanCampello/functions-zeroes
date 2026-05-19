from typing import Tuple


def bisseccao(
    f,
    a: float,
    b: float,
    tolerancia: float = 1e-6,
    max: int = 1000,
) -> Tuple[float, int, float]:
    """
    bisseccao para as raizes de f em [a, b]
    retorna (raiz, iterações, erro)
    """

    if f(a) * f(b) >= 0:
        raise ValueError("f(a) e f(b) devem ter sinais opostos")

    iteracoes = 0

    while (a - b) / 2 > tolerancia and iteracoes < max:
        ponto_medio = (a + b) / 2
        valor_no_ponto_medio = f(ponto_medio)

        if valor_no_ponto_medio == 0:
            break
        elif f(a) * valor_no_ponto_medio < 0:
            b = ponto_medio
        else:
            a = ponto_medio

        iteracoes += 1

    raiz = (a + b) / 2
    erro_final = (a - b) / 2

    return raiz, iteracoes, erro_final


def falsa_posicao(
    f, a: float, b: float, tolerancia: float = 1e-6, max: int = 1000
) -> Tuple[float, int, float]:
    """
    falsa posicao para as raizes de f em [a, b]
    retorna (raiz, iterações, erro)
    """

    if f(a) * f(b) >= 0:
        raise ValueError("f(a) e f(b) devem ter sinais opostos")

    iteracoes = 0
    ponto = a
    ponto_anterior = None

    while iteracoes < max:
        valor_a = f(a)
        valor_b = f(b)
        ponto = (a * valor_b - b * valor_a) / (valor_b - valor_a)
        valor_no_ponto = f(ponto)

        if ponto_anterior is not None and abs(ponto - ponto_anterior) < tolerancia:
            break
        if valor_no_ponto == 0:
            break
        elif valor_a * valor_no_ponto < 0:
            b = ponto
        else:
            a = ponto

        ponto_anterior = ponto
        iteracoes += 1

    erro_final = abs(f(ponto))
    return ponto, iteracoes, erro_final

def newton_raphson(
    f, derivada_f, chute_inicial: float, tolerancia: float = 1e-5, max_iteracoes: int = 20
) -> list:
    """
    Método de Newton-Raphson para encontrar raízes.
    Retorna uma lista de tuplas com o histórico: [(t_novo, erro), ...]
    """
    t = chute_inicial
    historico = []
    
    for i in range(max_iteracoes):
        t_novo = t - (f(t) / derivada_f(t))
        erro = abs(f(t_novo))
        
        # Guardamos o passo atual no histórico
        historico.append((t_novo, erro))
        
        if erro < tolerancia:
            break
            
        t = t_novo
        
    return historico