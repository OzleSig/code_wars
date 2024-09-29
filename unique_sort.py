def unique_in_order(sequence):
    result =[]
    for i, x in enumerate(sequence):
        if i == 0 or sequence[i-1] != x:
            result.append(x)
    return result