from funcs import *


def main():
    matrix = create_board()
    layout = []
    for i in range(3):
        row = []
        for j in range(3):
            button = sg.Button('-', size=(8, 4), key=(i, j), button_color='black')
            row.append(button)
        layout.append(row)
    window = (sg.Window('крестики нолики', layout, background_color='gray'))
    turn = 0
    while True:
        if check_for_end(matrix):
            break
        event, values = window.Read()
        if event is None:
            break
        else:
            x, y = event
        if matrix[x][y] == '-':
            if turn % 2 == 0:
                matrix[x][y] = 'x'
                window[event].Update('X')
                turn += 1
            else:
                window[event].Update('O')
                matrix[x][y] = 'O'
                turn += 1
        else:
            print('Эта клетка уже занята')
    end(matrix)
    window.Close()
