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

def minimax(arr,player,num):
    states=[]
    get_states(states,arr,player)
    if player=='O':
        val=float("-inf")
        for state in states:
            if win(state[1]):return 10
            if num==8:return state[0]
            val=max(val,minimax(state[1],'X',num+1))
        return val
    else:
        val=float("inf")
        for state in states:
            if win(state[1]):return -10
            if num==8:return state[0]
            val=min(val,minimax(state[1],'O',num+1))
        return val

arr=[['0' for i in range(3)] for j in range(3)]
a=minimax(arr,'O',0)
print(a)


def minimax_alpha_beta(arr,player,num,alpha,beta):
    states=[]
    get_states(states,arr,player)
    if player=='O':
        val=float("-inf")
        alpha=float("-inf")
        for state in states:
            if win(state[1]):return 10
            if num==8:return state[0]
            tmp=minimax(state[1],'X',num+1)
            if tmp>beta:
                return None
            val=max(val,tmp)
        return val
    else:
        val=float("inf")
        for state in states:
            if win(state[1]):return -10
            if num==8:return state[0]
            tmp=minimax(state[1],'O',num+1)
            if tmp<alpha:
                return None
            val=min(val,tmp)
        return val
    
