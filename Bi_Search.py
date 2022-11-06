def binary_search_recursive(array, element, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if element == array[mid]:
        return mid

    if element < array[mid]:
        return binary_search_recursive(array, element, start, mid - 1)
    else:
        return binary_search_recursive(array, element, mid + 1, end)


def solve(L, x):
    if x >= 0:
        x = x + 0.000005
        x = round(round(x, 5) - 0.00001, 5)
    else:
        x = x - 0.000005
        x = round(round(x, 5) + 0.00001, 5)
    for i in range(len(L)):
        if L[i] >= 0:
            L[i] = L[i] + 0.000005
            L[i] = round(round(L[i], 5) - 0.00001, 5)
        else:
            L[i] = L[i] - 0.000005
            L[i] = round(round(L[i], 5) + 0.00001, 5)
    return binary_search_recursive(L, x, 0, len(L) - 1)
    # print(binary_search_recursive(L, x, 0, len(L) - 1))


def main():
    L = [-1.000001, 7.29291111, 10.222, 15.82929, 20.2727]
    solve(L, -1)


main()
