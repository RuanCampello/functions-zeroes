import numpy as np
import matplotlib.pyplot as plt
from methods import newton_raphson  

# 1. DEFINIÇÃO DO PROBLEMA
def f(t):
    return -4.9 * t**2 + 50 * t + 10

def derivada_f(t):
    return -9.8 * t + 50

if __name__ == "__main__":
    print("SEMINÁRIO: CÁLCULO NUMÉRICO")
    print("Problema: Tempo de queda de um objeto.")
    print("Equação: -4.9t² + 50t + 10 = 0")
    
    input("\nPressione Enter para dar o chute inicial de 8 segundos...")
    
    print("\n--- INICIANDO MÉTODO DE NEWTON-RAPHSON ---")
    print("Chute inicial (t0) = 8.0 segundos\n")
    
    # 2. Recebemos o histórico completo do methods.py
    historico = newton_raphson(f, derivada_f, chute_inicial=8.0)

    # 3. Fazemos um loop pelo histórico recriando as pausas
    for i, (t_novo, erro) in enumerate(historico):
        input(f"Pressione Enter para rodar a iteração {i+1}...")
        print(f"Iteração {i+1}: t = {t_novo:.6f} | Erro (Altura) = {erro:.6f}m")

    # 4. Pegamos o valor da raiz (último tempo calculado no histórico) e o total de iterações
    raiz = historico[-1][0]
    total_iteracoes = len(historico)

    print("\n" + "="*50)
    print(f"✓ RAIZ ENCONTRADA!")
    print(f"O objeto atinge o solo exatamente em {raiz:.4f} segundos.")
    print(f"Total de iterações: {total_iteracoes}")
    print("="*50 + "\n")

    input("Pressione Enter para gerar o gráfico da trajetória...")
#  Geração do Gráfico 
    tempos = np.linspace(0, raiz + 2, 100)
    alturas = f(tempos)

    plt.figure(figsize=(8, 5))
    plt.plot(tempos, alturas, label='Trajetória f(t)', color='blue', linewidth=2)
    plt.axhline(0, color='black', linewidth=1)
    plt.scatter([raiz], [0], color='red', s=100, zorder=5, label=f'Raiz: {raiz:.2f}s')
    
    plt.title("Método de Newton-Raphson", fontsize=14)
    plt.xlabel("Tempo (segundos)")
    plt.ylabel("Altura (metros)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()