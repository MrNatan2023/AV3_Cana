import pandas as pd
import json
from collections import deque

class NumeroDeBacon:
    def init(self, arquivo):
        # Inicializa dicionários para mapear actores a movies e a outros actores
        self.movies_by_actor = {}
        self.actors_connected = {}
        self.load_data(arquivo)

    def load_data(self, arquivo):
        dados = pd.read_csv(arquivo)
        # Itera por cada linha dos dados
        for _, row in dados.iterrows():
            # Converte a string JSON da coluna 'cast' em lista de dicionários
            cast = json.loads(row['cast'])
            # Armazena o título do movie da linha atual
            movie = row['title']
            # Lista para guardar todos os actores do movie atual
            actors_InMovie = []

            # Itera sobre cada actor no cast
            for actor in cast:
                name_of_actor = actor['name']
                actors_InMovie.append(name_of_actor)
                # Se o actor não estiver no dicionário, adiciona com um conjunto vazio
                if name_of_actor not in self.movies_by_actor:
                    self.movies_by_actor[name_of_actor] = set()
                # Adiciona o movie ao conjunto de movies do actor
                self.movies_by_actor[name_of_actor].add(movie)

            # Conecta todos os actores que coestrelaram o mesmo movie
            for actor in actors_InMovie:
                if actor not in self.actors_connected:
                    self.actors_connected[actor] = set()
                self.actors_connected[actor].update(actors_InMovie)
                # Remove o próprio actor para evitar auto-referência
                self.actors_connected[actor].discard(actor)

    def calcular_numero_de_bacon(self, actor_inicial, actor_final):
        # Retorna 0 se o actor inicial e final forem o mesmo
        if actor_inicial == actor_final:
            return 0

        # Conjunto para manter registro dos actores visitados
        visitados = set()
        # largura bfs pra esquerda
        fila = deque([(actor_inicial, [], 0)])

        # Processa a fila até estar vazia
        while fila:
            # Desempacota a tupla na frente da fila
            actor_available, caminho, distancia = fila.popleft()
            # Adiciona o actor atual aos visitados
            visitados.add(actor_available)

            # Itera sobre cada movie do actor atual
            for movie in self.movies_by_actor.get(actor_available, []):
                # Itera sobre cada coactor que trabalhou com o actor atual
                for coactor in self.actors_connected.get(actor_available, []):
                    # Se o coactor for o actor final
                    if coactor == actor_final:
                        caminho_completo = caminho + [(actor_available, movie)]
                        self.print_caminho(caminho_completo, actor_final)
                        return distancia + 1
                    if coactor not in visitados:
                        visitados.add(coactor)
                        fila.append((coactor, caminho + [(actor_available, movie)], distancia + 1))

        return -1

    def print_caminho(self, caminho, actor_final):
        for actor, movie in caminho:
            print(f"{actor} atuou em '{movie}'")
        print(f"{actor_final}")

# Uso da classe
caminho_arquivo = 'tmdb_5000_credits.csv'
jogo = NumeroDeBacon(caminho_arquivo)
print(jogo.calcular_numero_de_bacon('Judi Dench', 'Johnny Depp'))