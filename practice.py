'''将你的 QQ 头像右上角加上红色的数字'''
from PIL import Image,ImageDraw,ImageFont,ImageColor

def add_number(picture_name,text):
    picture =Image.open(picture_name)
    font = ImageFont.truetype('arial.ttf',100)
    fontcolor = ImageColor.colormap.get('red')
    draw = ImageDraw.Draw(picture)
    width,height = picture.size
    draw.text((width-60,30),text, font=font,fill=fontcolor)
    picture.save('F:\\LSS\\practice\\image.png')

if __name__ == "__main__":
    picture_name = "E:\\LSS\\practice\\qq.jpg"
    text = "4"
    add_number(picture_name,text)
