array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

def snail(snail_map):
    snailed=[]
    if len(snail_map)==1:
        if len(snail_map[0])==1:
            snailed.append(snail_map[0][0])
        else:
            snailed.append(snail_map[0])
    max = len(snail_map)-1
    count=0
    dir_count=0
    tot_count=0
    xincrement=1
    yincrement=0
    x=0
    y=0
    while max>0:
        snailed.append(snail_map[y][x])
        if count==max:
            count=0
            temp=yincrement
            yincrement=xincrement
            xincrement=temp
            dir_count+=1
            tot_count+=1
            if dir_count==2:
                dir_count=0
                xincrement*=-1
                yincrement*=-1
            if tot_count==3 or (tot_count>3 and tot_count%2==1):
                max-=1
        y+=yincrement
        x+=xincrement
        count+=1
    return(snailed)

print(snail(array))