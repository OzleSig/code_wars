def to_jaden_case(string):
    eachword = string.split()
    tweet = '' 
    for x in eachword:
        x = x.lower()
        x = x[0].capitalize()+x[1:]+' '
        tweet += x
    tweet = tweet[:-1]
    return tweet

print(to_jaden_case(input("Tweet: ")))