import urllib.request
import json
import requests
import os
import os.path
import time
import hashlib
import pyperclip

from datetime import date

from PIL import ImageFont, ImageDraw, Image, ImageFilter, ImageChops

#DO NOT TOUCH текущая дата
# text_date = date.today()
# text_date = str(text5_subscribers.strftime("%d.%m.%Y"))
filename = input("Введите номер фона: ")
filename = "image_background"+str(filename)+".png"
#filename = "image_background3.png"
while True:
	text = input(": ")
	font_lenght = 60
	font_shadow_lenght = 62
	sym_max = 25
	ypl = 0
	while True:
		if len(text) > sym_max:
			font = ImageFont.truetype("font.ttf", font_lenght)
			shadow_font = ImageFont.truetype("font.ttf", font_shadow_lenght)
			font_lenght-=3
			font_shadow_lenght-=3
			sym_max+=1.5
			ypl+=2
			print(font_lenght, font_shadow_lenght, sym_max)
		else:
			font = ImageFont.truetype("font.ttf", font_lenght)
			shadow_font = ImageFont.truetype("font.ttf", font_shadow_lenght)
			break

	image = Image.open(filename)

	draw = ImageDraw.Draw(image)

	#Шрифт в формате .ttf
	# font = ImageFont.truetype("font.ttf", 60)

	# shadow_font = ImageFont.truetype("font.ttf", 62)

	#лево-право, верх-низ
	#x , y
	x = 100
	y = 8
	y+=ypl
	#Shadowed тень первая
	shadowed = Image.new("RGBA", image.size)
	shdw = ImageDraw.Draw(shadowed)
	shdw.text((x, y), text=text, fill='black', font=shadow_font, align="left")
	shadowed = shadowed.filter(ImageFilter.BoxBlur(7))
	image.paste(shadowed, shadowed)

	draw.text((x, y), text, font=font, align="left")

	#image.show()
	image.save("1.png")
	# os.system("./1.png" > clip)
###############################################