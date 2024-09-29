def find_outlier(integers):
    evens = sum(1 for x in integers if x%2==0)
    if evens == 1:
        for x in integers:
            if x%2==0:
                return x
    else:
        for x in integers:
            if x%2!=0:
                return x