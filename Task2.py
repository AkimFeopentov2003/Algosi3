def solve(mas, index, rez):
    while index > 0:
        if index % 2 == 1:
            if mas[index] < mas[(index - 1) // 2]:
                rez.append([(index - 1) // 2, index])
                mas[index], mas[(index - 1) // 2] = mas[(index - 1) // 2], mas[index]
            index -= 1
        else:
            min_Local = min(mas[index], mas[index - 1])
            if min_Local < mas[(index - 2) // 2]:
                if min_Local == mas[index]:
                    min_Local = index
                else:
                    min_Local = index - 1
                rez.append([(index - 1) // 2, min_Local])
                mas[min_Local], mas[(index - 2) // 2] = mas[(index - 2) // 2], mas[min_Local]
                index_down = min_Local
                N = 0
                if len(mas) % 2 == 1:
                    N = (len(mas) - 2) // 2
                else:
                    N = (len(mas) - 1) // 2
                while index_down <= N:
                    if index_down * 2 + 2 < len(mas):
                        min_Local = min(mas[index_down * 2 + 1], mas[index_down * 2 + 2])
                    else:
                        min_Local = mas[index_down * 2 + 1]
                    if min_Local < mas[index_down]:
                        if min_Local == mas[index_down * 2 + 1]:
                            min_Local = index_down * 2 + 1
                        else:
                            min_Local = index_down * 2 + 2
                        rez.append([index_down, min_Local])
                        mas[min_Local], mas[index_down] = mas[index_down], mas[min_Local]
                    else:
                        break;
                    index_down = min_Local;
            index -= 2


def main():
    rez = []
    N = int(input())
    mas = [int(i) for i in input().split()]
    N -= 1
    solve(mas, N, rez)
    print(len(rez))
    for i in range(len(rez)):
        print(rez[i][0], rez[i][1])


main()
