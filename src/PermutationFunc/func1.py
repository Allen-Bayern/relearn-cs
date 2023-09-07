array = list()

def permutations(arr, position, end):
    if position == end:
        global array
        array.append(arr)
    else:
        for i in range(position, end):
            arr[i], arr[end] = arr[end], arr[i]
            permutations(arr = arr, position = position + 1, end = end)
            arr[i], arr[end] = arr[end], arr[i]