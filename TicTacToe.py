# returned values: 
# x - X won
# o - O won
# d - draw
# i - impossible
# c - continue

def main():
    matrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    print("---------")
    print("| " + matrix[0][0] + " " + matrix[0][1] + " " + matrix[0][2] + " |")
    print("| " + matrix[1][0] + " " + matrix[1][1] + " " + matrix[1][2] + " |")
    print("| " + matrix[2][0] + " " + matrix[2][1] + " " + matrix[2][2] + " |")
    print("---------")
    
    provided_coordinates = []
    queue_turn = 'X'
    winner = False

    while winner != True:

        while len(provided_coordinates) != 2:
            provided_coordinates = input("Enter the coordinates: ").split()
            provided_coordinates[0] = int(provided_coordinates[0])
            provided_coordinates[1] = int(provided_coordinates[1])
            if len(provided_coordinates) != 2:
                provided_coordinates = []
                print("Coordinates should be from 1 to 3!")

            elif not isinstance(provided_coordinates[0], int) or not isinstance(provided_coordinates[1], int):
                provided_coordinates = []
                print("You should enter numbers!")
            elif provided_coordinates[0] not in (1,2,3) or provided_coordinates[1] not in (1,2,3):
                provided_coordinates = []
                print("Coordinates should be from 1 to 3!")
                
        provided_coordinates[0] = abs(provided_coordinates[0] - 1)
        provided_coordinates[1] = abs(provided_coordinates[1] - 1)

        if matrix[provided_coordinates[0]][provided_coordinates[1]] == ' ' and queue_turn == 'X':
            matrix[provided_coordinates[0]][provided_coordinates[1]] = 'X'
            queue_turn = 'O'
        elif matrix[provided_coordinates[0]][provided_coordinates[1]] == ' ' and queue_turn == 'O':
            matrix[provided_coordinates[0]][provided_coordinates[1]] = 'O'
            queue_turn = 'X'
        else:
            print("This cell is occupied! Choose another one!")
            provided_coordinates = []

        print("---------")
        print("| " + matrix[0][0] + " " + matrix[0][1] + " " + matrix[0][2] + " |")
        print("| " + matrix[1][0] + " " + matrix[1][1] + " " + matrix[1][2] + " |")
        print("| " + matrix[2][0] + " " + matrix[2][1] + " " + matrix[2][2] + " |")
        print("---------")

        result = check_win(matrix)
        provided_coordinates = []

        if result == 'X':
            print("X wins")
            break
        elif result == 'O':
            print("O wins")
            break
        elif result == 'd':
            print("Draw")
            break

def check_win(matrix):

    divided_cells = matrix

    #counter for checking if cells has empty cells
    counter = 0
    counterX = 0
    counterO = 0
    winner = "" #if winner non empty it's impossible case

    for line in matrix:
        for x in line:
            if x == '_' or x == ' ':
                counter += 1
            elif x == 'X':
                counterX += 1
            elif x == 'O':
                counterO += 1

    # X or O wins
    if divided_cells[0][0] == divided_cells[0][1] == divided_cells[0][2] and (divided_cells[0][0] != '_' and divided_cells[0][0] != ' ') or \
    divided_cells[0][0] == divided_cells[1][1] == divided_cells[2][2] and (divided_cells[0][0] != '_' and divided_cells[0][0] != ' ') or \
    divided_cells[0][0] == divided_cells[1][0] == divided_cells[2][0] and (divided_cells[0][0] != '_' and divided_cells[0][0] != ' '):
        if divided_cells[0][0] == 'X':
            winner += "X"
        elif divided_cells[0][0] == 'O':
            winner += "O"
    if divided_cells[0][1] == divided_cells[1][1] == divided_cells[2][1] and (divided_cells[1][1] != '_' and divided_cells[1][1] != ' ') or \
    divided_cells[1][0] == divided_cells[1][1] == divided_cells[1][2] and (divided_cells[1][1] != '_' and divided_cells[1][1] != ' ') or \
    divided_cells[0][2] == divided_cells[1][1] == divided_cells[2][0] and (divided_cells[1][1] != '_' and divided_cells[1][1] != ' '):
        if divided_cells[1][1] == 'X':
            winner += "X"
        elif divided_cells[1][1] == 'O':
            winner += "O"
    if divided_cells[0][2] == divided_cells[1][2] == divided_cells[2][2] and (divided_cells[2][2] != '_' and divided_cells[2][2] != ' ') or \
    divided_cells[2][0] == divided_cells[2][1] == divided_cells[2][2] and (divided_cells[2][2] != '_' and divided_cells[2][2] != ' '):
        if divided_cells[2][2] == 'X':
            winner += "X"
        else:
            winner += "O"

    if len(winner) == 1:
        return winner
        
    elif len(winner) > 1:
        return 'i'
        
    elif counter > 0:
        if abs(counterX-counterO) >= 2:
                print("Impossible")
        elif not winner:
            return 'c'
                                
    elif counter == 0 and not winner:
            return 'd'          

if __name__ == "__main__":
    main()