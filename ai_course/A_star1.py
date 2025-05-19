import math
import random
start=['7', '2', '4', '5', '0', '6', '8', '3', '1']
goal=['0', '1', '2', '3', '4', '5', '6', '7', '8']
def value(now,goal=['0', '1', '2', '3', '4', '5', '6', '7', '8']):
    same=0
    for i in range(9):
        if now[i]==goal:
            same+=1

    # for i in range(3):
    #     sum+=int(now[i])
    # same-=abs(3-sum)
    # sum=0
    # for i in range(3,6):
    #     sum+=int(now[i])
    # same-=abs(12-sum)
    # sum=0
    # for i in range(6,9):
    #     sum+=int(now[i])
    # same-=abs(21-sum)

    s_now=''.join(now)
    step1=0
    for i in range(9):
        idx=s_now.index(f'{i}')
        x=idx//3
        y=idx%3
        ix=i//3
        iy=i%3
        step1+=abs(x-ix)+abs(y-iy)
    dp=[1 for i in range(9)]
    for i in range(9):
        for j in range(i,-1,-1):
            if now[i]>now[j]:
                dp[i]=max(dp[j]+1,dp[i])
    step2=0
    for i in range(9):
        idx=s_now.index(f'{i}')
        x=idx//3
        y=idx%3
        ix=i//3
        iy=i%3
        step2+=(x==ix)+(y==iy)
    return step2
    return max(dp)
    return step2**9+max(dp)**8
    return max(dp)**2.6+step2**1.7
def find_fa(now,past,visited,start):
    while(now!=start and past!=start):
        now=visited[now][0]
        past=visited[past][0]
    if past!=start:
        return 1
    return 0

def append_states(idx,visited:dict,s,choices:dict,start):
    x=idx//3
    y=idx%3
    puzzle=[]
    for c in s:
        puzzle.append(c)
    if x>0:
        tp=list(puzzle)
        tp[idx],tp[idx-3]=tp[idx-3],tp[idx]
        ts=''.join(tp)
        v=value(tp)
        if  not visited.get(ts,False):
            choices[ts]=(s,idx-3,v)
        elif find_fa(s,visited[ts][0],visited,start):
            visited[ts]=(s,idx-3)     
    if x<2:
        tp=list(puzzle)
        tp[idx],tp[idx+3]=tp[idx+3],tp[idx]
        ts=''.join(tp)
        v=value(tp)
        if  not visited.get(ts,False):
            choices[ts]=(s,idx+3,v)
        elif find_fa(s,visited[ts][0],visited,start):
            visited[ts]=(s,idx+3)
    if y>0:
        tp=list(puzzle)
        tp[idx],tp[idx-1]=tp[idx-1],tp[idx]
        ts=''.join(tp)
        v=value(tp)
        if not visited.get(ts,False):
            choices[ts]=(s,idx-1,v)
        elif find_fa(s,visited[ts][0],visited,start):
            visited[ts]=(s,idx-1)
    if y<2:
        tp=list(puzzle)
        tp[idx],tp[idx+1]=tp[idx+1],tp[idx]
        ts=''.join(tp)
        v=value(tp)
        if not visited.get(ts,False):
            choices[ts]=(s,idx+1,v)
        elif find_fa(s,visited[ts][0],visited,start):
            visited[ts]=(s,idx+1)
def display(now):
    k=0
    for i in range(3):
        for j in range(3):
            print(now[k],end=' ')
            k+=1
        print("\n")
    print("------------")

def path(visited,choice):
    step=0
    while(visited[choice][0]!=choice):
        display(choice)
        choice=visited[choice][0]
        step+=1
    display(choice)
    print("The path lenth",step)

def A_star(idx,start,goal):
    g=''.join(goal)
    step=0
    visited={}
    s=''.join(start)
    visited[s]=(s,idx)
    choices={}
    append_states(idx,visited,s,choices,s)
    choice=max(choices.keys(),key=lambda x:choices[x][2])
    w=0
    while(choices):
        choice=max(choices.keys(),key=lambda x:choices[x][2])
        visited[choice]=(choices[choice][0],choices[choice][1])
        if choice==g:
            path(visited,choice)
            append_states(choices[choice][1],visited,choice,choices,s)
        else:
            append_states(choices[choice][1],visited,choice,choices,s)
        step+=1
        choices.pop(choice)
        w+=1
        if w==2000:
            #path(visited,g)
            break
    print("total_step",step)
    return step
A_star(4,start,goal)
# n=A_star(4,start)
# print(n)