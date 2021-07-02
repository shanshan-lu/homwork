'''将你的 QQ 头像右上角加上红色的数字'''
from PIL import Image,ImageDraw,ImageFont,ImageColor

def add_num_to_pic(picture,number,color='red'):
    num_font = ImageFont.truetype('arial.ttf',100)
    num_fontcolor = ImageColor.colormap.get(color)  #设置字体和颜色

    canvas = ImageDraw.Draw(picture)
    width,height = picture.size
    pos = (width-60,30)  #不要用绝对的阿拉伯数字，需改动
    canvas.text(pos,number, font=num_font,fill=num_fontcolor)
    
    return pic 

if __name__ == "__main__":
    pic_path = "../doc/qq.jpg"
    pic =Image.open(pic_path) 
    text = "4"
    canvas = add_num_to_pic(pic,text)
    canvas.save('../doc/image.png') 
