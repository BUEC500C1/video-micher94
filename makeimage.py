from PIL import Image, ImageDraw, ImageFont


def makeimage(num1,num2,tweet):
	tweet=tweet.encode('utf-8') 
	font = ImageFont.load_default()
	# https://code-maven.com/create-images-with-python-pil-pillow
	filename = str(num1) + "-" + str(num2) + ".png"
	image = Image.new(mode = "RGB", size = (1000,100), color = 'black')
	tweeter = ImageDraw.Draw(image)
	tweeter.text((0,50),tweet,fill=(255,255,0),spacing=250,align='center')

	image.save(filename)