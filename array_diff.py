def array_diff(a, b):
    diff = []
    for x in a:
        if x not in b:
            diff.append(x)
    return diff

print(array_diff([1,2,2], []))