def disemvowel(string_):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    cleaned = ''
    for x in string_:
        if x not in vowels: 
            cleaned += x
    return cleaned

print(disemvowel(input("Comment: ")))