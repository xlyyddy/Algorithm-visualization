import os
from PIL import Image, ImageDraw, ImageFont

image_folder = r"C:\Users\pingf\Desktop\code\python2.py\output"
output_gif = "67.gif"

# 获取并排序图片
images = [f for f in os.listdir(image_folder) if f.endswith('.png')]
images.sort(key=lambda f: int(f.split('.')[0]))

processed_images = []

#字体设置（Windows系统路径）
FONT_SIZE = 40
TEXT_COLOR = "Black"
BOTTOM_MARGIN = 20

for img_file in images:
    img = Image.open(os.path.join(image_folder, img_file))
    draw = ImageDraw.Draw(img)
    number = os.path.splitext(img_file)[0]

    try:
        font = ImageFont.truetype("arial.ttf", FONT_SIZE)
    except:
        font = ImageFont.load_default()

    # 使用textbbox替代textsize（新版本Pillow的写法）
    bbox = draw.textbbox((0, 0), number, font=font)
    text_width = bbox[2] - bbox[0]  # 右边界 - 左边界
    text_height = bbox[3] - bbox[1] # 下边界 - 上边界

    x = (img.width - text_width) // 2
    y = img.height - text_height - BOTTOM_MARGIN
    
    draw.text((x, y), number, fill=TEXT_COLOR, font=font)
    processed_images.append(img)

# 生成GIF
processed_images[0].save(
    output_gif,
    save_all=True,
    append_images=processed_images[1:],
    duration=700,
    loop=0,
    optimize=True
)

print(f"GIF已生成：{output_gif}")