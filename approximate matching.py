


def approximate_matching(x, y):
    minn =1000
    D =[]
    for i in range (len(x)+1): #+1 for Empty row
        D.append([0]*(len(y)+1))# table with rows =len(y) and column = len(x)
    for i in range (len(x)+1):
        D[i][0]=0    #initialize first column with incremental
      
    for i in range (len(y)+1):
        D[0][i]=i    #initialize first row with incremental
        
        
    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            dist1 = D[i][j-1]+1
            dist2 = D[i-1][j]+1
            if x[i-1] == y[j-1]:
                dist3 = D[i-1][j-1]
            else:
                dist3 = D[i-1][j-1]+1
            D[i][j] = min (dist1,dist2,dist3)
        if D[i][j] < minn:
            minn = D[i][j]
            mini = i
            minj = j
            
  
            
    return mini, minj ,D



def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;0;0;0m".format(r, g, b, text)
def trace_back (T,P):
    ResultT =[]
    ResultP =[]
    i,j,D =approximate_matching(T, P) 
    i=i-1
    j=j-1
    for x in range (len(P)+1):
        if T[i]==P[j]:
            colored_char = colored(0, 255, 0, T[i])
            ResultT.append(colored_char)
            colored_char = colored(0, 255, 0, P[j])
            ResultP.append(colored_char)
            i=i-1
            j=j-1
        else:
            minn= min(D[i-1][j-1] ,D[i-1][j], D[i][j-1] )
            if minn == D[i-1][j]:
                colored_char = colored(255, 0, 255, '-')
                ResultT.append(colored_char)
                colored_char = colored(255, 0, 255, T[i])
                ResultP.append(colored_char)
                i=i-1
            elif  minn == D[i][j-1]:
                colored_char = colored(255, 0, 255, '-')
                ResultT.append(colored_char)
                colored_char = colored(255, 0, 255, P[j])
                ResultP.append(colored_char)
                j=j-1
            else:
                colored_char = colored(255, 0, 0, T[i])
                ResultT.append(colored_char)
                colored_char = colored(255, 0, 0, P[j])
                ResultP.append(colored_char)
                i=i-1
                j=j-1           
    D = list(map(list, zip(*D)))      
    return ResultT[::-1] ,ResultP[::-1] ,D



#TESET 
T= 'TTGGGATACAGTACGGAACCT'
P= 'ATGCAGTCG'
R1 , R2 , D =trace_back(T,P)
S1 = ''
for i in range(len(R1)):
    S1 =  S1 + R1[i] + ' '
S2 = ''
for i in range(len(R2)):
    S2 =  S2 + R2[i] + ' '
New = '      '
for x in range (len(T)):
    New = New +T[x]+'  '    
print(New)
for i in range(len(D)):
    print(P[i-1],D[i])
i,j,D =approximate_matching(T, P)
S1 = T[: i - j] +' '+ S1 + T[i:] 
print(S1 )
spaces = len(T[: i-j])
spacesvar = ' '
for i in range(spaces):
    spacesvar += ' '
S2 =  spacesvar + S2 
print(S2)

