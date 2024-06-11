
const N = 8;

function printarTabuleiro(tab) {
    for (var lin of tab) {
        console.log(lin.join(" "));
    }
    console.log("\n");
}

function eSeguro(tab, lin, col, N) {
    // Verifica a coluna acima da posição atual
    for (var i = 0; i < lin; i++) {
        if (tab[i][col] === 'D') {
            return false;
        }
    }

    // Verifica a diagonal superior esquerda
    for (var i = lin, j = col; i >= 0 && j >= 0; i--, j--) {
        if (tab[i][j] === 'D') {
            return false;
        }
    }

    // Verifica a diagonal superior direita
    for (var i = lin, j = col; i >= 0 && j < N; i--, j++) {
        if (tab[i][j] === 'D') {
            return false;
        }
    }

    return true;
}


    var tab = [];
    for (var i = 0; i < N; i++) {
        var lin = [];
        for (var j = 0; j < N; j++) {
            lin.push('-');
        }
        tab.push(lin);
    } 
    var stack = [];
    var lin = 0, col = 0;

    while (lin < N) {
        while (col < N) {
            if (eSeguro(tab, lin, col, N)) {
                tab[lin][col] = 'D';
                stack.push({ lin, col });
                printarTabuleiro(tab); 
                lin++;
                col = 0;
                break;
            } else {
                col++;
            }
        }

        if (col === N || stack.length === 0) {
            if (stack.length === 0) {
                break;
            }
            var prev = stack.pop();
            lin = prev.lin;
            col = prev.col;
            tab[lin][col] = '-';
            col++;
        }
    }

    if (stack.length === N) {
        console.log("Solução: ");
        printarTabuleiro(tab);
    
    } else {
        console.log("Não encontrou a solução");
        
    }







