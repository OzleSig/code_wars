def reverse_words(text):
    rev_text = ''
    words = text.split()
    count = 0
    for l, word in enumerate(words):
        for y in range(len(word)):
            rev_text += word[len(word)-y-1]
            count += 1 
        rev_text += text[count::]
    return rev_text

print(reverse_words(input("Words: ")))
