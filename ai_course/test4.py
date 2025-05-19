import copy
def cal_value(arr):
    val=0
    k=0
    for i in range(3):
        for j in range(3):
            if arr[i][j]=='O':
                val+=k
            elif arr[i][j]=='X':
                val-=k
            k+=1
    return val
def win(arr):
    for i in range(3):
        s=''.join(arr[i])
        if s=='OOO' or s=='XXX':
            return True
    for j in range(3):
        s=''.join((arr[0][j],arr[1][j],arr[2][j]))
        if s=='OOO' or s=='XXX':
            return True
    if arr[0][0] == arr[1][1] == arr[2][2] and arr[0][0]!='0' :
        return True
    if arr[0][2] == arr[1][1] == arr[2][0] and arr[0][2]!='0':
        return True
    return False
def get_states(states,arr,player):
    for i in range(3):
        for j in range(3):
            if arr[i][j]=='0':
                arr[i][j]=player
                val=cal_value(arr)
                states.append((val,copy.deepcopy(arr)))
                arr[i][j]='0'
ss=[[] for i in range(3)]
def minimax(arr,player,num):
    states=[]
    get_states(states,arr,player)
    if player=='O':
        val=float("-inf")
        s=[]
        for state in states:
            if win(state[1]):return 10
            if num==8:return state[0]
            s.append(minimax(state[1],'X',num+1))
        if num<3:
            ss[num].append(s)
        val=max(val,max(s))
        return val
    else:
        val=float("inf")
        s=[]
        for state in states:
            if win(state[1]):return -10
            if num==8:return state[0]
            s.append(minimax(state[1],'O',num+1))
        if num<3:
            ss[num].append(s)
        val=min(val,min(s))
        return val

def minimax_alpha_beta(arr,player,num,alpha,beta):
    states=[]
    get_states(states,arr,player)
    if player=='O':
        val=float("-inf")
        s=[]
        for state in states:
            if win(state[1]):return 10
            if num==8:return state[0]
            tmp=minimax_alpha_beta(state[1],'X',num+1,alpha,beta)
            if tmp =='cut':
                continue
            elif tmp>=beta:
                return 'cut'
            alpha=max(tmp,alpha)
            val=max(val,tmp)
        return val
    else:
        val=float("inf")
        s=[]
        for state in states:
            if win(state[1]):return -10
            if num==8:return state[0]
            tmp=minimax_alpha_beta(state[1],'O',num+1,alpha,beta)
            if tmp=='cut':
                continue
            elif tmp<=alpha:
                return "cut"
            beta=min(tmp,beta)
            val=min(val,tmp)
        return val
alpha=float("-inf")
beta=float("inf")
arr=[['0' for i in range(3)] for j in range(3)]
#a=minimax_alpha_beta(arr,'O',0,alpha,beta)
minimax(arr,'O',0)
for i in range(2):
    print(ss[i])
    print(",")
#alpha_beta=[[8],[[4, 6, 8],][[10, 4], [10, 6], [10, 8]]]
minimax=[[[8]],[[4, 6, 4, 6, 8, 4, 4, 4, 4]],
[[10, 10, 10, 4, 10, 10, 10, 10], [10, 10, 10, 6, 10, 10, 10, 10], [10, 10, 10, 4, 10, 10, 10, 10], [10, 10, 10, 6, 10, 10, 10, 10], [10, 10, 10, 10, 10, 10, 10, 8], [10, 10, 10, 10, 4, 10, 10, 8], [10, 10, 10, 10, 4, 10, 10, 10], [10, 10, 10, 10, 4, 10, 10, 8], [10, 10, 10, 10, 4, 10, 10, 10]]]