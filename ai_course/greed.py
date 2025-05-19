import math
import random
from test2 import draw_puzzle
start=['7', '2', '4', '5', '0', '6', '8', '3', '1']
goal=['0', '1', '2', '3', '4', '5', '6', '7', '8']
def value(now,goal=['0', '1', '2', '3', '4', '5', '6', '7', '8']):
    same=0
    for i in range(9):
        if now[i]==goal:
            same+=1
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

def append_states(idx,visited:dict,s,choices:dict):
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
    if x<2:
        tp=list(puzzle)
        tp[idx],tp[idx+3]=tp[idx+3],tp[idx]
        ts=''.join(tp)
        v=value(tp)
        if  not visited.get(ts,False):
            choices[ts]=(s,idx+3,v)
    if y>0:
        tp=list(puzzle)
        tp[idx],tp[idx-1]=tp[idx-1],tp[idx]
        ts=''.join(tp)
        v=value(tp)
        if not visited.get(ts,False):
            choices[ts]=(s,idx-1,v)
    if y<2:
        tp=list(puzzle)
        tp[idx],tp[idx+1]=tp[idx+1],tp[idx]
        ts=''.join(tp)
        v=value(tp)
        if not visited.get(ts,False):
            choices[ts]=(s,idx+1,v)

def display(now):
    k=0
    for i in range(3):
        for j in range(3):
            print(now[k],end=' ')
            k+=1
        print("\n")
    print("------------")
wes=0
def path(visited,choice):
    global wes
    step=0
    while(visited[choice][0]!=choice):
        draw_puzzle(list(map(int,list(choice))),number=wes+1)
        wes+=1
        display(choice)
        choice=visited[choice][0]
        step+=1
    draw_puzzle(list(map(int,list(choice))),number=wes+1)
    #display(choice)
    print("The path lenth",step)

def greedy(idx,start,goal):
    g=''.join(goal)
    step=0
    visited={}
    s=''.join(start)
    visited[s]=(s,idx)
    fa={}
    fa[s]=(s,idx)
    choices={}
    append_states(idx,visited,s,choices)
    choice=max(choices.keys(),key=lambda x:choices[x][2])
    w=0
    while(choices):
        choice=max(choices.keys(),key=lambda x:choices[x][2])
        idx=choices[choice][1]
        fa[choice]=(choices[choice][0],visited[choices[choice][0]][1])
        visited[choice]=(choices[choice][0],idx)
        choices={}
        if choice==g:
            path(fa,choice)
            return
        append_states(idx,visited,choice,choices)
        while(not choices):
            past=fa[choice]
            append_states(past[1],visited,past[0],choices)
            choice=past[0]
        step+=1
        w+=1
    print("total_step",step)
    return step
greedy(4,start,goal)
