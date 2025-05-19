from PIL import Image, ImageDraw
import os

def draw_chessboard_with_icon(state,number,icon_path, cell_size=200):
    """整合绘图功能的完整实现"""
    # 创建画布
    output_path=os.path.join('output', f'{number}.png')
    img = Image.new("RGB", (cell_size*4, cell_size*4), "white")
    draw = ImageDraw.Draw(img)
    
    # 棋盘颜色配置
    colors = [(235, 235, 235), (80, 110, 150)]
    # 修复1：正确的路径处理
    try:
        # 统一使用下划线命名规范
        icon_path = os.path.normpath(icon_path)  # 自动转换路径分隔符
        print(f"尝试加载图标：{icon_path}")
        
        # 修复2：移除错误的replace操作
        icon = Image.open(icon_path).convert("RGBA")
        
        # 修复3：正确的resize方法和尺寸计算
        icon_size = int(cell_size * 0.8)
        icon = icon.resize((icon_size, icon_size))  # 保持宽高比
    except Exception as e:
        print(f"图标加载失败：{str(e)}，使用备用方案")
        # 生成备用图标
        icon = Image.new("RGBA", (cell_size, cell_size), (0,0,0,0))
        draw_icon = ImageDraw.Draw(icon)
        # 修复4：正确的椭圆绘制坐标
        draw_icon.ellipse([10, 10, cell_size-10, cell_size-10], fill=(255,0,0,255))


    # 绘制棋盘
    lenth=len(state)
    for i in range(lenth):
        for j in range(lenth):
            # 计算坐标
            x0 = j * cell_size
            y0 = i * cell_size
            
            # 绘制格子
            color_index = (i + j) % 2
            draw.rectangle([x0, y0, x0+cell_size, y0+cell_size], fill=colors[color_index])
            
            # 绘制棋子（在奇数格）
            if (i,j) in state:
                position = (
                    x0 + (cell_size - icon.width)//2,
                    y0 + (cell_size - icon.height)//2
                )
                img.paste(icon, position, icon)  # 保持透明度

            
    # 添加棋盘边框
    draw.rectangle([0, 0, cell_size*4-1, cell_size*4-1], outline="black", width=3)
    
    # 保存结果
    img.save(output_path)
    print(f"棋盘已生成：{output_path}")

# 使用示例（包含两种路径格式测试）
if __name__ == "__main__":
    # 测试路径1：原始字符串路径
    draw_chessboard_with_icon(
        [1],
        1,
        icon_path=r"ai_course\Queen_Black.png",
        cell_size=200
    )
