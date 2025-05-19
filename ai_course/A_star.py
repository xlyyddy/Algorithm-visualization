# 在A_star.py中使用
import sys
from pathlib import Path
import heapq
ROOT_DIR = Path(__file__).parent  # 获取A_star.py所在目录（即ai_course）
sys.path.append(str(ROOT_DIR))
from test2 import draw_puzzle  # 开头的点号表示"当前目录"
start=['7', '2', '4', '5', '0', '6', '8', '3', '1']
goal=['0', '1', '2', '3', '4', '5', '6', '7', '8']


def value(now,goal=['0', '1', '2', '3', '4', '5', '6', '7', '8']):
    s_now=list(now)
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
    return step1
def append_states(s):
    puzzle=list(s)
    idx=puzzle.index("0")
    x=idx//3
    y=idx%3
    moves=[]
    if x>0:
        tp=puzzle.copy()
        tp[idx],tp[idx-3]=tp[idx-3],tp[idx]
        ts=''.join(tp)
        moves.append(ts)
    if x<2:
        tp=puzzle.copy()
        tp[idx],tp[idx+3]=tp[idx+3],tp[idx]
        ts=''.join(tp)
        moves.append(ts)
    if y>0:
        tp=puzzle.copy()
        tp[idx],tp[idx-1]=tp[idx-1],tp[idx]
        ts=''.join(tp)
        moves.append(ts)
    if y<2:
        tp=puzzle.copy()
        tp[idx],tp[idx+1]=tp[idx+1],tp[idx]
        ts=''.join(tp)
        moves.append(ts)
    return moves

def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path
def A_star(start,goal):
    heap=[]
    g=''.join(goal)
    s=''.join(start)

    fa={}
    states_g={s:0}
    heapq.heappush(heap,(0,0,s))
    while(heap):
        current_f,current_g,current_state=heapq.heappop(heap)
        next_state_g=current_g+1
        if current_state == g:
            return reconstruct_path(fa, current_state)
        for next_state in append_states(current_state):
            next_state_g=current_g+1
            if next_state not in states_g or next_state_g<states_g[next_state]:#有个想法，如果第一个没有加进来，那么遍历到其他的的时候
                fa[next_state]=current_state                                   #就会一直重复更新g值，因为s的均值是给了的，所以为0
                states_g[next_state]=next_state_g
                h=value(next_state)
                heapq.heappush(heap,(h+next_state_g,next_state_g,next_state))

    return None
path = A_star(start, goal)
if path:
    print(f"Found path with {len(path)} steps:")
    for state in path:
        print('\n'.join(' '.join(state[i*3:(i+1)*3]) for i in range(3)))
        print()
else:
    print("No solution found")

for i in range(len(path)):
    draw_puzzle(list(map(int,list(path[i]))),number=i+1)
