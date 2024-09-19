# gen-colored-ascii-image.py

import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import PIL.ImageFont as ImageFont

# 定义输出宽度和高度（行/像素）
output_width = 50
output_height = 50

# 定义彩色 ASCII 字符画绘图字体和字体大小
colored_ascii_image_font = "fonts/DejaVuSans-Bold.ttf"
colored_ascii_image_font_size = 30

# 定义彩色 ASCII 字符画替换像素的 ASCII 字符
colored_ascii_chars = [" ", "o", "0", "@", "8", "#", "$", "S", "X"]

# 将图像调整为指定大小
def resize_image(image_file, output_width, output_height):
    image = Image.open(image_file)
    image = image.resize((output_width, output_height))
    return image


# 将图像转换为灰度图像
def convert_to_gray(image):    
    return image.convert('L')


# 将图像转换为彩色 ASCII 字符画
def image_to_colored_ascii(image, output_width, output_height):
    resized_image = resize_image(image, output_width, output_height)

    ascii_image = []
    ascii_image_chars = []
    ascii_image_colors=[]
    for y in range(output_height):
        row = ""
        for x in range(output_width):
            color = resized_image.getpixel((x, y))

            gray_value = sum(color) // 3
            char_index = int(gray_value / 255 * (len(colored_ascii_chars) - 1))
            if char_index >= len(colored_ascii_chars):
                char_index = len(colored_ascii_chars) - 1

            row += f"\033[38;2;{color[0]};{color[1]};{color[2]}m{colored_ascii_chars[char_index]}"

            ascii_image_chars.append(colored_ascii_chars[char_index])
            ascii_image_colors.append((color[0], color[1], color[2]))

        ascii_image.append(row)

    return "\n".join(ascii_image), ascii_image_chars, ascii_image_colors


# 将彩色 ASCII 艺术图像存储为图片
def save_colored_ascii_image_as_picture(ascii_image_chars, ascii_image_colors, font_path, font_size, output_path):
    image = Image.new('RGB', ((output_width * font_size), (output_height * font_size)), color='white')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)

    for i in range(output_height):
        for j in range(output_width):
            draw.text((j * font_size, i * font_size), ascii_image_chars[i*output_width+j], font=font, fill=ascii_image_colors[i*output_width+j])

    image.save(output_path)

def colored_ascii_image_as_picture(ascii_image_chars, ascii_image_colors, font_path, font_size):
    image = Image.new('RGB', ((output_width * font_size), (output_height * font_size)), color='white')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)

    for i in range(output_height):
        for j in range(output_width):
            draw.text((j * font_size, i * font_size), ascii_image_chars[i*output_width+j], font=font, fill=ascii_image_colors[i*output_width+j])

    return image

if __name__ == "__main__":
    image_path = "assets/mol1.png"

    # 将图像转换为彩色 ASCII 字符画
    colored_ascii_image, colored_ascii_image_chars, colored_ascii_image_colors = image_to_colored_ascii(image_path, output_width, output_height)

    # 存储彩色 ASCII 字符画到图片文件
    save_colored_ascii_image_as_picture(colored_ascii_image_chars, colored_ascii_image_colors, colored_ascii_image_font, colored_ascii_image_font_size, "colored_ascii_image.png")

    # 在终端窗口打印彩色 ASCII 字符画
    #print(colored_ascii_image)