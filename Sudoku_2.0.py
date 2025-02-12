
def find_empty_grid(x): # Encontra os espaços vazios (iguais a zero).
    for i in range(len(x)):
        for j in range(len(x[0])):
            if x[i][j] == 0:
                return (i, j)  #retorna linha e coluna
    return None

#Soluciona o array
def solve_array(x):
    find = find_empty_grid(x) #Encontra os espaços vazios (iguais a zero)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(x, i, (row, col)): #Valida as posições
            x[row][col] = i

            if solve_array(x):
                return True

            x[row][col] = 0

    return False

#valida as posições
def valid(x, num, pos): 
    # Checa linha
    for i in range(len(x[0])):
        if x[pos[0]][i] == num and pos[1] != i:
            return False

    # Checa coluna
    for i in range(len(x)):
        if x[i][pos[1]] == num and pos[0] != i:
            return False

    # Checa a célula
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if x[i][j] == num and (i,j) != pos:
                return False

    return True

# printa o tabuleiro com o layout parecido com o de sudoku
def print_board(x): 
    for i in range(len(x)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(x[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                k = '.' if x[i][j]==0 else str(x[i][j])
                print(k)
            else:
                k = '.' if x[i][j]==0 else str(x[i][j])
                print(k + " ", end="")


# board = []
# for i in range(1,10):
#     board.append(list(map(int, input().split())))
# solve_array(board)
# print('\n')
# print_board(board)

x = [
[8,0,0,0,0,0,0,0,0],
[0,0,3,6,0,0,0,0,0],
[0,7,0,0,9,0,2,0,0],
[0,5,0,0,0,7,0,0,0],
[0,0,0,0,4,5,7,0,0],
[0,0,0,1,0,0,0,3,0],
[0,0,1,0,0,0,0,6,8],
[0,0,8,5,0,0,0,1,0],
[0,9,0,0,0,0,4,0,0]
]
solve_array(x)
print_board(x)