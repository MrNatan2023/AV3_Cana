def pos_valida(x, y, tabuleiro): #verificar
    return 0 <= x < 8 and 0 <= y < 8 and tabuleiro[x][y] == -1

def print_tabuleiro(tabuleiro): #imprime o tabuleiro, mostrando o estado atual das pos visitadas
    for row in tabuleiro:
        for col in row:
            print(f"{col:2}", end=' ')
        print()

def passeio_cavalo(): #inicializa o tabuleiro
    tabuleiro = [[-1 for _ in range(8)] for _ in range(8)] 
    
    mov_x = [2, 1, -1, -2, -2, -1, 1, 2]
    mov_y = [1, 2, 2, 1, -1, -2, -2, -1]
    
    tabuleiro[0][0] = 0
    
    def solucao(x, y, contar_mov):  #funçao recursiva
        if contar_mov == 64: #condiçao de parada
            return True
        
        #tentativa de movimento
        for i in range(8):
            prox_x = x + mov_x[i] #calcula a nova posiçao
            prox_y = y + mov_y[i]
            
            if pos_valida(prox_x, prox_y, tabuleiro): 
                tabuleiro[prox_x][prox_y] = contar_mov #marca a pos com o numero de mov atuais
                if solucao(prox_x, prox_y, contar_mov + 1): #continuar a partir da nova posiçao
                    return True
                tabuleiro[prox_x][prox_y] = -1 #se nao encontrou soluçao desfaz
                
        return False
    
    if not solucao(0, 0, 1):
        print("Não existe solução!")
    else:
        print_tabuleiro(tabuleiro)

passeio_cavalo()