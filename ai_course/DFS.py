# nodes = [
#     "Oradea", "Zerind", "Arad", "Sibiu", "Timisoara", "Lugoj", "Mehadia", 
#     "Drobeta", "Craiova", "Neamt", "Iasi", "Fagaras", "Vaslui", "Hirsova", 
#     "Urziceni", "Bucharest", "Pitesti", "Giurgiu", "Rimnicu Vilcea", "Eforie"
# ]
# arr=[[0, 71, 0, 151, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [71, 0, 75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 75, 0, 140, 118, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [151, 0, 140, 0, 0, 0, 0, 0, 0, 0, 0, 99, 0, 0, 0, 0, 0, 0, 80, 0],
# [0, 0, 118, 0, 0, 111, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 111, 0, 70, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 70, 0, 75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 75, 0, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 120, 0, 0, 0, 0, 0, 0, 0, 0, 138, 0, 146, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 87, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 87, 0, 0, 92, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 99, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 211, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 92, 0, 0, 0, 142, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 98, 0, 0, 0, 0, 86],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 142, 98, 0, 85, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 211, 0, 0, 85, 0, 101, 90, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 138, 0, 0, 0, 0, 0, 0, 101, 0, 0, 97, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0],
# [0, 0, 0, 80, 0, 0, 0, 0, 146, 0, 0, 0, 0, 0, 0, 0, 97, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 86, 0, 0, 0, 0, 0, 0]]
# # for i in range(len(nodes)):
# #     for j in range(len(nodes)):
# #         print(f"{}")
# res=[]
# visited=[False for i in range(len(arr))]
# def dfs(arr,s,t,stack):
#     stack.append(s)
#     # print(nodes[s])
#     if s==t:
#         res.append(list(stack))
#         stack.pop()
#         return stack
#     visited[s]=True
#     for i in range(len(arr)):
#         if arr[s][i]!=0 and not visited[i]:
#             dfs(arr,i,t,stack)
#             visited[i]=False
#     stack.pop()
# stack=[]
# dfs(arr,2,15,stack)
# for i in range(len(res)):
#     print(nodes[res[i][0]],end="")
#     for j in res[i][1:]:
#         print(f"->{nodes[j]}",end="")
#     print("")

import networkx as nx
import matplotlib.pyplot as plt
m=1
nodes = [
    "Oradea", "Zerind", "Arad", "Sibiu", "Timisoara", "Lugoj", "Mehadia", 
    "Drobeta", "Craiova", "Neamt", "Iasi", "Fagaras", "Vaslui", "Hirsova", 
    "Urziceni", "Bucharest", "Pitesti", "Giurgiu", "Rimnicu Vilcea", "Eforie"
]
arr=[[0, 71, 0, 151, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[71, 0, 75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 75, 0, 140, 118, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[151, 0, 140, 0, 0, 0, 0, 0, 0, 0, 0, 99, 0, 0, 0, 0, 0, 0, 80, 0],
[0, 0, 118, 0, 0, 111, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 111, 0, 70, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 70, 0, 75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 75, 0, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 120, 0, 0, 0, 0, 0, 0, 0, 0, 138, 0, 146, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 87, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 87, 0, 0, 92, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 99, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 211, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 92, 0, 0, 0, 142, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 98, 0, 0, 0, 0, 86],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 142, 98, 0, 85, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 211, 0, 0, 85, 0, 101, 90, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 138, 0, 0, 0, 0, 0, 0, 101, 0, 0, 97, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0],
[0, 0, 0, 80, 0, 0, 0, 0, 146, 0, 0, 0, 0, 0, 0, 0, 97, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 86, 0, 0, 0, 0, 0, 0]]

res=[]
visited=[False for i in range(len(arr))]

G = nx.Graph()
edges = [
    # 根据图片中的连接关系构建完整边集
    ("Oradea", "Zerind", 71), ("Oradea", "Sibiu", 151),
    ("Zerind", "Arad", 75), ("Arad", "Sibiu", 140),
    ("Arad", "Timisoara", 118), ("Sibiu", "Fagaras", 99),
    ("Sibiu", "Rimnicu Vilcea", 80), ("Timisoara", "Lugoj", 111),
    ("Lugoj", "Mehadia", 70), ("Mehadia", "Drobeta", 75),
    ("Drobeta", "Craiova", 120), ("Craiova", "Rimnicu Vilcea", 146),
    ("Craiova", "Pitesti", 138), ("Rimnicu Vilcea", "Pitesti", 97),
    ("Fagaras", "Bucharest", 211), ("Pitesti", "Bucharest", 101),
    ("Bucharest", "Giurgiu", 90), ("Bucharest", "Urziceni", 85),
    ("Urziceni", "Hirsova", 98), ("Hirsova", "Eforie", 86),
    ("Urziceni", "Vaslui", 142), ("Vaslui", "Iasi", 92),
    ("Iasi", "Neamt", 87)
]
G.add_weighted_edges_from(edges)
pos={'Oradea': (28.350137983133678, 197.14269563027716), 'Zerind': (16.79308696791699, 167.0631433431489), 'Arad': (8.51731084490901, 136.35251735709625), 'Sibiu': (66.40984331077296, 110.57459568629267), 'Timisoara': (10.001207673609505, 74.28169115417623), 'Lugoj': (45.95968939662571, 50.41215073822261), 'Mehadia': (47.311256031944254, 20.629891720498108), 'Drobeta': (45.80037926090375, -10.716176145619727), 'Craiova': (89.4802635297987, -18.607937755988246), 'Neamt': (163.90957351134958, 170.6404267456023), 'Iasi': (198.01992918407515, 147.7136426005581), 'Fagaras': (114.79901227715852, 103.61736788821568), 'Vaslui': (215.83439968343535, 100.98284075667178), 'Hirsova': (228.22268987455612, 28.24003412320326), 'Urziceni': (189.4878436088371, 29.542522958646174), 'Bucharest': (161.69079444367358, 12.022519258539802), 'Pitesti': (123.25401230285371, 40.59736161859098), 'Giurgiu': (149.37059648798237, -31.849179552801047), 'Rimnicu Vilcea': (79.26514345620771, 73.88136020021688), 'Eforie': (241.92464630580352, -15.037335101161915)}
# 高级绘图配置
def update(stack):
    global m
    if not stack:return
    plt.figure(figsize=(25, 20))
    node_colors = ["#FF9999"] * len(G.nodes())
    node_colors[list(G.nodes()).index(nodes[stack[-1]])]="#FFA500"#橙色
    node_idx=[list(G.nodes()).index(nodes[i]) for i in stack[:-1]]
    for idx in node_idx:
        node_colors[idx] = "#0000FF"#蓝色
    # 边标签特殊处理（防止重叠）
    nx.draw(G, pos, 
    with_labels=True,
    node_color=node_colors,    # 浅红色节点（匹配图片）
    node_shape='s',         # 方形节点
    node_size=500,
    edge_color='gray',      # 灰色边线
    width=2,
    font_size=9,
    font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, 
                                edge_labels=edge_labels,
                                label_pos=0.6,  # 标签位置优化
                                font_size=8,
                                bbox=dict(alpha=0))
    plt.axis('off')
    plt.gca().set_facecolor('white')  # 白色背景
    plt.tight_layout()
    file_name = f"C:\\Users\\pingf\\Desktop\\可视化图片\\{m}.png"
    m+=1
    plt.savefig(file_name)  # 保存为文件
    # 获取当前时间戳作为文件名
def dfs(arr,s,t,stack):
    stack.append(s)
    #update(stack)
    # print(nodes[s])
    if s==t:
        res.append(list(stack))
        stack.pop()
        return stack
    visited[s]=True
    for i in range(len(arr)):
        if arr[s][i]!=0 and not visited[i]:
            dfs(arr,i,t,stack)
            visited[i]=False
    stack.pop()
    #update(stack)
stack=[]
mmm=dfs(arr,2,15,stack)