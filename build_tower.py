def tower_builder(n_floors):
    array = []
    for n in range(n_floors):
        x = '*' * (2 * n + 1)
        array.append(x.center((n_floors*2)-1,' '))
    return array

print(tower_builder(3))