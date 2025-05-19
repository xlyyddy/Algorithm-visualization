import copy
from queen_picture import draw_chessboard_with_icon
def any(x,Y):
    x0,x1=x[0],x[1]
    for y in Y:
        y0,y1=y[0],y[1]
        if x0!=y0 and x1!=y1 and x0+x1!=y0+y1 and x0-x1!=y0-y1:
            return True
    return False
def ac3(arr,x1,x2):
    dx1=arr[x1]
    dx2=arr[x2]
    rm=[]
    for x in range(len(dx2)):
        if any(dx2[x],dx1):
           continue
        rm.append(dx2[x])
    for x in rm:
        dx2.remove(x) 
def check(arr1):
    for i in range(len(arr1)):
        for j in range(i+1,len(arr1)):
            ac3(arr1,i,j)
icon_path=r"C:\Users\pingf\Downloads\ww.png"
wes=1
def queen(arr,i,res,state,n):
    global wes
    if i==n:
        res.append(list(state))
        return 
    if not arr[i]:
        return 
    for k in range(len(arr[i])):
        arr1=copy.deepcopy(arr)
        state.append(arr[i][k])
        wes+=1
        arr1[i]=[arr[i][k]]
        check(arr1)
        #draw_chessboard_with_icon(arr1,wes,icon_path)
        queen(arr1,i+1,res,state,n)
        state.pop()
def display(res,n):
    for r in res:
        arr=[[0 for i in range(n)] for j in range(n)]
        for i in range(len(r)):
            arr[r[i][0]][r[i][1]]=1
            print(arr[i])
        print("--------")
res=[]
arr=[]
n=4
for i in range(n):
    arr.append([(i,j) for j in range(n)])
state=[]
#draw_chessboard_with_icon(arr,wes,icon_path)
queen(arr,0,res,state,n)
display(res,n)
icon_path=r"ai_course\Queen_Black.png"
for i in range(len(res)):
    draw_chessboard_with_icon(res[i],99+i,icon_path)
print(len(res))