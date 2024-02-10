import PySimpleGUI as sg


def check_for_end(matrix):
    if matrix[0][0] == 0 and matrix[1][1] == 0 and matrix[2][2] == 0:
        return True
    if matrix[0][0] == 'x' and matrix[1][1] == 'x' and matrix[2][2] == 'x':
        return True
    if matrix[0][2] == 0 and matrix[1][1] == 0 and matrix[2][0] == 0:
        return True
    if matrix[0][2] == 'x' and matrix[1][1] == 'x' and matrix[2][0] == 'x':
        return True
    if matrix[0][0] == 0 and matrix[0][1] == 0 and matrix[0][2] == 0:
        return True
    if matrix[0][0] == 'x' and matrix[0][1] == 'x' and matrix[0][2] == 'x':
        return True
    if matrix[1][0] == 0 and matrix[1][1] == 0 and matrix[1][2] == 0:
        return True
    if matrix[1][0] == 'x' and matrix[1][1] == 'x' and matrix[1][2] == 'x':
        return True
    if matrix[2][0] == 0 and matrix[2][1] == 0 and matrix[2][2] == 0:
        return True
    if matrix[2][0] == 'x' and matrix[2][1] == 'x' and matrix[2][2] == 'x':
        return True
    if matrix[0][2] == 0 and matrix[1][2] == 0 and matrix[2][2] == 0:
        return True
    if matrix[0][2] == 'x' and matrix[1][2] == 'x' and matrix[2][2] == 'x':
        return True
    if matrix[0][1] == 0 and matrix[1][1] == 0 and matrix[2][1] == 0:
        return True
    if matrix[0][1] == 'x' and matrix[1][1] == 'x' and matrix[2][1] == 'x':
        return True
    if matrix[0][0] == 0 and matrix[1][0] == 0 and matrix[2][0] == 0:
        return True
    if matrix[0][0] == 'x' and matrix[1][0] == 'x' and matrix[2][0] == 'x':
        return True


def create_board():
    matrixx = []
    for a in range(3):
        roww = []
        for j in range(3):
            roww.append('-')
        matrixx.append(roww)
    return matrixx


def end(matrixx):
    print('gameover. результат: ', )

    for i in range(0, 3, 1):
        print()
        for j in range(0, 3, 1):
            print(matrixx[i][j], end=' ')

