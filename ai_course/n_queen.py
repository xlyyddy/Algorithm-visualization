n=5
arr=[[0 for i in range(n)] for j in range(n)]
state=[]
res=[]
visited=[False for i in range(n)]
diags1=[0 for i in range(2*n-1)]
diags2=[0 for i in range(2*n-1)]
def n_queen(m,res:list,state:list,visited,diags1,diags2):
    if len(state)==n:
        res.append(list(state))
        return 
    for i in range(n):
        diag1=i+m
        diag2=m-i+n-1
        if not visited[i] and not diags1[diag1] and not diags2[diag2]:
            diags1[diag1]=1
            diags2[diag2]=1
            visited[i]=True
            state.append((i,m))
            n_queen(m+1,res,state,visited,diags1,diags2)
            state.pop()
            visited[i]=False
            diags1[diag1]=0
            diags2[diag2]=0
n_queen(0,res,state,visited,diags1,diags2)
for i in range(len(res)):
    arr=[[0 for i in range(n)] for j in range(n)]
    for x,y in res[i]:
        arr[x][y]=1
    for i in range(n):
        print(arr[i])
    print("————")
print(len(res))