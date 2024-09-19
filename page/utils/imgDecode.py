from PIL import Image
offset_x = 1372
offset_y = 1372
def extract_number_from_image(overlay_image, offset_x, offset_y):
    # 打开叠加后的图像
    overlay_image = Image.open(overlay_image)
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