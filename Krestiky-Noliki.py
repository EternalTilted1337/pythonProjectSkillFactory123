Igrok1 = input("Введите имя игрока играющего х ")
Igrok2 = input("Введите имя игрока играющего о ")
matrix = [
    ['-', '-', '-'],  # 0
    ['-', '-', '-'],  # 1
    ['-', '-', '-'],  # 2
]

win_coord = [[0, 0, 0, 1, 0, 2], [1, 0, 1, 1, 1, 2], [2, 0, 2, 1, 2, 2], [0, 0, 1, 1, 2, 2], [0, 2, 1, 1, 2, 0],[0, 0, 1, 0, 2, 0], [0, 1, 1, 1, 2, 1], [0, 2, 1, 2, 2, 2]]
def checkY():
    checkedY = False
    for el in win_coord:
        if matrix[int(el[0])][int(el[1])] == 'o' and matrix[int(el[2])][int(el[3])] == 'o' and matrix[int(el[4])][int(el[5])] == 'o':
            checkedY = True
            break
    return checkedY

def checkX():
    checkedX = False
    for el in win_coord:
        if matrix[int(el[0])][int(el[1])] == 'x' and matrix[int(el[2])][int(el[3])] == 'x' and matrix[int(el[4])][int(el[5])] == 'x':
            checkedX = True
            break
    return checkedX
def nich():
    count = 0
    for el in matrix:
        for item in el:
            if item == '-':
                count += 1
    return count
while True:
    print('  0 1 2 ')
    print('0', *matrix[0])
    print('1', *matrix[1])
    print('2', *matrix[2])
    print(Igrok1, 'Ваш ход')


    def fhod1v():  # начало ходов
        hod1v = int(input("Цифра по вертикали"))
        return hod1v


    def fhod1g():
        hod1g = int(input("Цифра по горизонтали"))
        return hod1g


    matrix[fhod1v()][fhod1g()] = 'x'

    print('+ 0 1 2 ')
    print('0', *matrix[0])
    print('1', *matrix[1])
    print('2', *matrix[2])

    if checkX():
        print(Igrok1, "ПОБЕДА!!!")
        break
    if checkY():
        print(Igrok2, "ПОБЕДА!!!")
        break
    if nich() == 0:
        print('Ничья')
        break

    print(Igrok2, 'Ваш ход')


    def fhod2v():
        hod2v = int(input("Цифра по вертикали"))
        return hod2v


    def fhod2g():
        hod2g = int(input("Цифра по горизонтали"))
        return hod2g


    while True:
        matrix[fhod2v()][fhod2g()] = 'o'
        break
    print('+ 0 1 2 ')
    print('0', *matrix[0])
    print('1', *matrix[1])
    print('2', *matrix[2])
    print(Igrok1, 'Ваш ход')


    if checkX():
        print(Igrok1, "ПОБЕДА!!!")
        break
    if checkY():
        print(Igrok2, "ПОБЕДА!!!")
        break
    if nich() == 0:
        print('Ничья')
        break