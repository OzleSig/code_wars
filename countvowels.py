def get_count(sentence):
    vowels = ('a', 'e', 'i', 'o', 'u')
    n_vowel = 0
    for x in sentence.lower():
        if x in vowels:
            n_vowel +=1
    return n_vowel

print(get_count(input("Comment: ")))