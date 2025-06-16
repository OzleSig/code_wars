input = 'aaw'
outdict = dict()

def permutations(input):
    output = []
    outset = set('')
    if input in outdict:
        return(outdict[input])
    if len(input) == 1:
        return(input)
    else:
        for i,x in enumerate(input):
                ansr = []
                for y in permutations(input[:i] + input[i+1:]):
                    output.append(x+y)
                    ansr.append(y)
                outdict[input[:i] + input[i+1:]]=ansr 
    outset.update(output)
    return(outset)
    
print(permutations(input))