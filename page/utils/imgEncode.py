from PIL import Image

def create_square_pattern(number):
    # 将输入整数转换为1024位的二进制字符串，不足部分填充0
    binary_string = f'{number:01024b}'

    # 创建一个128x128像素的RGB图像
    img_size = 128
    block_size = 4
    img = Image.new('RGB', (img_size, img_size), 'white')

    # 定义紫色和绿色
    purple = (254, 254, 254)
    green = (0, 0, 0)

    # 遍历二进制字符串，按位设置4x4方块的颜色
    for i, bit in enumerate(binary_string):
        color = purple if bit == '0' else green
        x = (i % 32) * block_size
        y = (i // 32) * block_size
        for dx in range(block_size):
            for dy in range(block_size):
                img.putpixel((x + dx, y + dy), color)

    return img
def overlay_pattern_on_image(base_image, pattern_image, offset_x, offset_y):
    pattern_image = pattern_image.convert("RGBA")
    # 打开基础图像
    #base_image = Image.open(base_image_path)
    
    # 获取基础图像的尺寸
    base_width, base_height = base_image.size
    
    # 获取图案图像的尺寸
    pattern_width, pattern_height = pattern_image.size
    
    # 计算图案图像粘贴的位置
    paste_x = offset_x
    paste_y = offset_y
    
    # 确保图案图像不会超出基础图像的边界
    if paste_x + pattern_width > base_width or paste_y + pattern_height > base_height:
        raise ValueError("Pattern image exceeds the boundaries of the base image.")
    
    # 创建一个新的图像，将基础图像复制到新图像中
    new_image = base_image.copy()
    
    # 将图案图像粘贴到新图像上
    new_image.paste(pattern_image, (paste_x, paste_y), pattern_image)
    
    return new_image

def extract_number_from_image(overlay_image, offset_x, offset_y):
    # 打开叠加后的图像
    #overlay_image = Image.open(overlay_image_path)
    # 提取128x128像素的区域
    pattern_region = overlay_image.crop((offset_x, offset_y, offset_x + 128, offset_y + 128))
    
    # 定义紫色和绿色的RGB值
    purple = (254, 254, 254)
    green = (0, 0, 0)
    
    binary_string = ""
    
    # 遍历128x128区域中的每个4x4方块
    block_size = 4
    for y in range(0, 128, block_size):
        for x in range(0, 128, block_size):
            # 获取4x4方块的左上角像素的颜色
            color = pattern_region.getpixel((x, y))
            if color == purple:
                binary_string += "0"
            elif color == green:
                binary_string += "1"
            else:
                raise ValueError("Unexpected color found in the pattern region.")
    
    # 将二进制字符串转换为十进制整数
    number = int(binary_string, 2)
    
    return number

# 示例使用
#base_image_path = 'FLL.jpg'  # 基础图像的路径
# 示例使用
#number = 80291670378524564640069487068812981035930848416449863249303777134369802916703785245646400694870688129810359308484164498632493037771343698029167037852456464006948706881298103593084841644986324930377713436980291670378524564662999515313693489885343780490631115314181593435331209712709857825836348345723998675361
#result_image = create_square_pattern(number)
#result_image.show()  # 显示结果图像
#result_image.save('output_pattern.png')  # 保存结果图像
# 设定偏移量
offset_x = 1372#20
offset_y = 1372#20

# 叠加图案图像到基础图像上
#result_image = overlay_pattern_on_image(base_image_path, result_image, offset_x, offset_y)
#result_image.show()  # 显示结果图像
#result_image.save('overlay_output_image.png')  # 保存结果图像

#extracted_number = extract_number_from_image("overlay_output_image.png", offset_x, offset_y)
#print(f'Extracted number: {extracted_number}')