import itertools

def distancia_total(caminho, distancias):
     total = 0
     for i in range(len(caminho) - 1):
        total += distancias[caminho[i]][caminho[i + 1]]
     total += distancias[caminho[-1]][caminho[0]]
     return total

def caixeiro_viajante(distancias):
     cidades = list(distancias.keys())
     menor_distancia = 1000000
     melhor_caminho = None
    
    

     for permutacao in itertools.permutations(cidades):
         d = distancia_total(permutacao, distancias)
         if d < menor_distancia:
             menor_distancia = d
             melhor_caminho = permutacao

     return melhor_caminho, menor_distancia
       
distancias = {
     'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
     'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
     'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
     'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
     }

caminho, distancia = caixeiro_viajante(distancias)
print(f"Melhor caminho: {caminho} com distância total de: {distancia}")


#guloso
def distancia_total(caminho, distancias):
    total = 0  # O(1)
    for i in range(len(caminho) - 1):  # O(n)
        total += distancias[caminho[i]][caminho[i + 1]]  # O(1)
    total += distancias[caminho[-1]][caminho[0]]  # O(1)
    return total  # O(1)

def caixeiro_viajante_guloso(distancias):
    cidades = list(distancias.keys())  # O(n)
    cidade_atual = cidades[0]  # O(1)
    caminho = [cidade_atual]  # O(1)
    visitadas = {cidade_atual}  # O(1)
    
    while len(visitadas) < len(cidades):  # O(n)
        cidade_mais_proxima = None  # O(1)
        menor_distancia = float('inf')  # O(1)
        for cidade in cidades:  # O(n)
            if cidade not in visitadas and distancias[cidade_atual][cidade] < menor_distancia:  # O(1)
                cidade_mais_proxima = cidade  # O(1)
                menor_distancia = distancias[cidade_atual][cidade]  # O(1)
        caminho.append(cidade_mais_proxima)  # O(1)
        visitadas.add(cidade_mais_proxima)  # O(1)
        cidade_atual = cidade_mais_proxima  # O(1)
    
    return caminho, distancia_total(caminho, distancias)  # O(n)

distancias = {  # O(1)
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},  # O(1)
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},  # O(1)
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},  # O(1)
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}  # O(1)
}

caminho, distancia = caixeiro_viajante_guloso(distancias)  # O(n^2)
print(f"Melhor caminho: {caminho} com distância total de: {distancia}")  # O(n)