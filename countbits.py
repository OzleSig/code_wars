def count_bits(n):
    bincount = 0
    bin_n = bin(n)
    for x in bin_n[2:]:
        bincount += int(x)
    return bincount

print(count_bits(int(input("Number: "))))