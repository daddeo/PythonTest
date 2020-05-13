def selectionSort(list, showProgress):
    for i in range(len(list) - 1):
        minpos = i
        for j in range(i, len(list)):
            if list[j] < list[minpos]:
                minpos = j

        temporary = list[i]
        list[i] = list[minpos]
        list[minpos] = temporary

        if showProgress:
            if minpos == i:
                print(list, " -- no change")
            else:
                print(list, " -- swapped {} and {}".format(list[i], list[minpos]))


numbers = [5, 3, 8, 7, 6, 2]
selectionSort(numbers, True)

print(numbers)
