from PIL import Image, ImageDraw, ImageFont
import os

def draw_puzzle(input_array, save_dir='output',number=None):
    # 验证输入有效性（保持不变）
    try:
        nums = [int(num) for num in input_array]
    except ValueError:
        raise ValueError("数组元素必须为数字")
    
    if len(nums) != 9:
        raise ValueError("数组长度必须为9个元素")
    
    if sorted(nums) != list(range(9)):
        raise ValueError("数组必须包含0-8的每个数字，且不重复")

    # 创建图像和绘图对象（保持不变）
    image = Image.new('RGB', (300, 300), '#FFFFE0')
    draw = ImageDraw.Draw(image)
    
    # 修改颜色定义部分（原代码中找到colors字典）
    colors = {
    'background': '#FFFFE0',  # 保持浅黄背景
    'border': '#A52A2A',      # 保持棕色边框
    'empty': '#808080',       # 保持灰色空位
    'number': '#0000FF',      # 保持蓝色数字
    'cell': '#FFA500'         # 新增橙黄色格子 ← 关键修改点
    }   
    
    try:
        font = ImageFont.truetype('arial.ttf', 40)
    except:
        font = ImageFont.load_default()

    # 修改部分：使用textbbox替代textsize
    for i in range(9):
        num = nums[i]
        row, col = divmod(i, 3)
        x0 = col * 100
        y0 = row * 100
        
        # 绘制格子背景（保持不变）
        fill = colors['empty'] if num == 0 else colors['cell']  # 原'white'改为colors['cell']
        draw.rectangle([x0, y0, x0+100, y0+100], fill=fill)
        
        if num != 0:
            text = str(num)
            # 新的文本尺寸获取方式
            text_bbox = draw.textbbox((0, 0), text, font=font)
            w = text_bbox[2] - text_bbox[0]  # 计算实际宽度
            h = text_bbox[3] - text_bbox[1]   # 计算实际高度
            draw.text(
                (x0 + (100 - w)/2, y0 + (100 - h)/2),  # 保持居中计算
                text, 
                fill=colors['number'], 
                font=font
            )

    # 绘制网格线（保持不变）
    for pos in [100, 200]:
        draw.line([(pos, 0), (pos, 300)], fill=colors['border'], width=3)
        draw.line([(0, pos), (300, pos)], fill=colors['border'], width=3)

    # 保存图片（保持不变）
    os.makedirs(save_dir, exist_ok=True)
    image.save(os.path.join(save_dir, f'{number}.png'))
    return os.path.join(save_dir, f'{number}.png')

# 示例用法（保持不变）
if __name__ == "__main__":
    example_input = [7, 2, 4, 5, 0, 6, 8, 3, 1]
    try:
        output_path = draw_puzzle(example_input,number=0)
        print(f"图片已保存至：{output_path}")
    except Exception as e:
        print(f"发生错误：{str(e)}")