import math
import time
from typing import Callable

from methods import bisseccao, falsa_posicao, newton_raphson

M = 1000


def funcao_hash(n: float) -> float:
    return 1 - math.exp(-(n**2) / (2 * M)) - 0.05


def derivada_funcao_hash(n: float) -> float:
    return (n / M) * math.exp(-(n**2) / (2 * M))


def coletar_estatisticas(
    nome_metodo: str, metodo: Callable, raiz_real: float, *args
) -> None:
    inicio = time.perf_counter()
    raiz, iteracoes, erro = metodo(*args)
    tempo = (time.perf_counter() - inicio) * 1000

    distancia_raiz_real = abs(raiz - raiz_real)

    print(f"{'=' * 40}")
    print(f"Método:            {nome_metodo}")
    print(f"Raiz encontrada:   {raiz:.8f}")
    print(f"Iterações:         {iteracoes}")
    print(f"Erro:              {erro:.2e}")
    print(f"Distância da raiz: {distancia_raiz_real:.2e}")
    print(f"Tempo (ms):         {tempo:.4f}")


raiz_real = math.sqrt(-2 * M * math.log(0.95))

coletar_estatisticas("Bissecção", bisseccao, raiz_real, funcao_hash, 1.0, 500.0)

coletar_estatisticas("Falsa Posição", falsa_posicao, raiz_real, funcao_hash, 1.0, 500.0)

coletar_estatisticas(
    "Newton-Raphson",
    newton_raphson,
    raiz_real,
    funcao_hash,
    derivada_funcao_hash,
    raiz_real * 0.5,
)
