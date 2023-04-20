# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество
# элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
N = abs(int(input('Введите кол-во элементов: ')))
A = input("Введите элементы через пробел: ").split()
B = list(map(int, A))
if len(B) != N or N == 0:
    print('Введено не то кол-во элементов')
else:
    X = int(input('К какому числу искать ближайшее?: '))
    min = abs(X - B[0])
    index = 0
    for i in range(1, N):
        count = abs(X - B[i])
        if count < min:
            min = count
            index = i
    print(f'Число {B[index]} в списке  наиболее близко по величине к числу {X}, их разница составляет {abs(X - B[index])}')