from PIL import Image, ImageDraw, ImageFont
import numpy as np

# 原始数据
alpha_beta = [
    [[8]],
    [[4, 6, 4, 6, 8, 4, 4, 4, 4]],
    [[10, 10, 10, 4, 10, 10, 10, 10], 
     [10, 10, 10, 6, 10, 10, 10, 10],
     [10, 10, 10, 4, 10, 10, 10, 10],
     [10, 10, 10, 6, 10, 10, 10, 10],
     [10, 10, 10, 10, 10, 10, 10, 8],
     [10, 10, 10, 10, 4, 10, 10, 8],
     [10, 10, 10, 10, 4, 10, 10, 10],
     [10, 10, 10, 10, 4, 10, 10, 8],
     [10, 10, 10, 10, 4, 10, 10, 10]]
]
alpha_beta=[[[8]],[[4, 6, 8],],[[10, 4], [10, 6], [10, 8]]]
# 动态样式配置
WIDTH, HEIGHT = 1000, 500  # 增大画布尺寸
BASE_NODE_RADIUS = 30
LEVEL_SPACING = 150
SIDE_MARGIN = 200

def calculate_positions(data):
    positions = {}
    connections = []
    
    # 计算每层节点数
    layer_counts = [sum(len(group) for group in layer) for layer in data]
    
    # 根节点
    root_x = WIDTH // 2
    root_y = 100
    positions[('node', 0, 0)] = (root_x, root_y)
    
    # 逐层计算位置
    for level in range(1, len(data)):
        # 获取当前层所有节点
        current_nodes = [num for group in data[level] for num in group]
        node_count = len(current_nodes)
        
        # 动态调整参数
        node_radius = BASE_NODE_RADIUS * (0.7 if level==len(data)-1 else 1)  # 末层缩小
        x_positions = np.linspace(SIDE_MARGIN, WIDTH-SIDE_MARGIN, node_count)
        
        # 记录节点位置
        for idx, x in enumerate(x_positions):
            positions[('node', level, idx)] = (x, root_y + level*LEVEL_SPACING)
            
        # 建立连接关系
        parent_nodes = [num for group in data[level-1] for num in group]
        children_per_parent = node_count // len(parent_nodes)
        
        for parent_idx in range(len(parent_nodes)):
            parent_x, parent_y = positions[('node', level-1, parent_idx)]
            child_start = parent_idx * children_per_parent
            child_end = (parent_idx + 1) * children_per_parent
            
            for child_idx in range(child_start, child_end):
                child_pos = positions[('node', level, child_idx)]
                connections.append(((parent_x, parent_y), child_pos))
    
    return positions, connections

def draw_tree():
    img = Image.new('RGB', (WIDTH, HEIGHT), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 18)  # 使用标准字体
    
    positions, connections = calculate_positions(alpha_beta)
    
    # 绘制连接线
    for (start, end) in connections:
        draw.line([start, end], fill=(0,0,0), width=2)
    
    # 绘制节点
    for key in positions:
        if key[0] != 'node':
            continue
            
        level = key[1]
        x, y = positions[key]
        value = alpha_beta[level][key[2]//len(alpha_beta[level][0])][key[2]%len(alpha_beta[level][0])]
        
        # 动态节点大小
        radius = BASE_NODE_RADIUS * (1 if level==len(alpha_beta)-1 else 1)
        
        # 绘制圆形
        draw.ellipse((x-radius, y-radius, x+radius, y+radius),
                    fill=(173, 216, 230), outline=(0,0,0))
        
        # 文字定位
        text_bbox = font.getbbox(str(value))
        text_w = text_bbox[2] - text_bbox[0]
        text_h = text_bbox[3] - text_bbox[1]
        draw.text((x - text_w//2, y - text_h//2), str(value),
                 fill=(0,0,0), font=font)
    
    img.show()
    img.save('organized_tree.png')

draw_tree()