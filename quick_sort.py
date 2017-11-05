def quicksort(seq):
    wall = 0
    pivot = seq[-1]
    for index, num in enumerate(seq):
        if num < pivot:
            seq[wall], seq[index] = seq[index], seq[wall]
            wall += 1
    seq[wall], seq[-1] = seq[-1], seq[wall]
    left = seq[:wall]
    if len(left) > 0:
        left = quicksort(left)
    right = seq[(wall + 1):]
    if len(right) > 0:
        right = quicksort(right)
    return left + [pivot] + right