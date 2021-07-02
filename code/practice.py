'''将你的 QQ 头像右上角加上红色的数字'''
from PIL import Image,ImageDraw,ImageFont,ImageColor

def add_num_to_pic(picture,number,color='red'):
    pic =Image.open(picture)  #移出
    num_font = ImageFont.truetype('arial.ttf',100)
    num_fontcolor = ImageColor.colormap.get('red')

    canvas = ImageDraw.Draw(pic)
    width,height = picture.size
    pos = (width-60,30)
    pic.text(pos,number, font=num_font,fill=num_fontcolor)
    
    canvas.save('E:\\LSS\\practice\\image.png') #移出
    return pic 

if __name__ == "__main__":
    pic_path = "E:\\LSS\\practice\\qq.jpg"
    text = "4"
    add_num_to_pic(pic_path,text)
