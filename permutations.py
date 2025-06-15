input = 'augggjhjjkw'
outdict = dict()

def permutations(input):
    output = []
    if input in outdict:
        return(outdict[input])
    if len(input) == 1:
        return(input)
    elif len(input) == 2:
            output.append(input)
            input = input[1]+input[0]
            output.append(input)
            return(output)
    else:
        for i,x in enumerate(input):
                ansr = []
                for y in permutations(input[:i] + input[i+1:]):
                    output.append(x+y)
                    ansr.append(y)
                outdict[input[:i] + input[i+1:]]=ansr 
    return(output)
    
permutations(input)