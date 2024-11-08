def clean_string(s):
    cleanedstr = ''
    for x in s:
        if x == '#':
            cleanedstr = cleanedstr [:-1]
        else:
            cleanedstr = cleanedstr + x
    return cleanedstr

print(clean_string('abc#d##c'))