from PIL import Image, ImageDraw, ImageFont
import pandas as pd

form = pd.read_csv("test_mail_new.csv")

#name_list = ["A", "B", "C"]
#c_no = ["ABC123", "ABC124", "ABC125"]

c_no = form['certificate_no'].to_list()
name_list = form['receiver_names'].to_list()

for i,j in zip(name_list, c_no):
    im = Image.open("Demo-Auto-Template.jpg")
    d = ImageDraw.Draw(im)
    location = (1370, 970)
    text_color = (0, 0, 0)
    font = ImageFont.truetype("georgia italic.ttf", 150, encoding="unic")
    d.text(location, i, fill=text_color,font=font)

    location_new = (755, 2160)
    text_color_new = (0, 0, 0)
    font_new = ImageFont.truetype("arial.ttf", 55, encoding="unic")
    d.text(location_new, j, fill=text_color_new,font=font_new)
    im.save("certificate_"+i+".pdf")
