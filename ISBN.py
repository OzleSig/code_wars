def valid_ISBN10(isbn): 
    isbn_sum = 0
    if len(isbn) != 10:
        return False
    for i, x in enumerate(isbn):
        i += 1
        if x.isalpha():
            if x.upper() == 'X' and i != 1:
                x = 10
            else: 
                return False
        x = int(x)
        x_i = x*i
        isbn_sum += x_i
    return isbn_sum % 11 == 0