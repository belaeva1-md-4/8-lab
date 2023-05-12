from PIL import Image, ImageDraw, ImageFont

def s():
    image=Image.open("ирина.jpg")
    image.show()
    im=image.crop((150, 75, 500, 150))
    im.show()
    im.save("обрез.jpg")

def s1():
    n = Image.open("новый год.jpg")
    d = Image.open("день рож.jpg")
    i = Image.open("ирина.jpg")
    p = Image.open("пасха.jpg")
    a={"Новый год":n, "Пасха":p, "День рождения":d, "8 марта":i}

    s=str(input("Введите праздник "))
    nov=a[s]
    '''nov.show()'''

    ss=str(input('КОго вы хотите поздравить? '))
    font=ImageFont.truetype("arial.ttf", 40)
    draw=ImageDraw.Draw(nov)
    draw.text((100, 400), 'Поздравляю, '+ ss, font=font,  fill=('#ffffff'), stroke_width=2)
    nov.show()

s1()