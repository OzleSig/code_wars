def is_isogram(string):
    string = ''.join(sorted(string.lower()))
    n = len(string)
    for x in range(n):
        if string[x]==string[x-1]:
            return False
    else:
        return True

print(is_isogram(input("String: ")))