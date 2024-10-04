def sq_in_rect(lng, wdth):
    squares = None
    if lng != wdth:
        squares = []
        while lng > 0 and wdth > 0:
            squares.append(min(lng, wdth))
            if lng > wdth:
                lng -= wdth
            else:
                wdth -= lng
    return squares

print(sq_in_rect(5,5))