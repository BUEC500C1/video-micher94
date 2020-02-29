from PIL import Image, ImageDraw, ImageFont


def makeimage(num,tweet):
	tweet=tweet.encode('utf-8') 
	font = ImageFont.load_default()
	# https://code-maven.com/create-images-with-python-pil-pillow
	filename = str(num) + ".png"
	image = Image.new(mode = "RGB", size = (100,100), color = 'blue')
	tweeter = ImageDraw.Draw(image)
	tweeter.text((0,0),tweet,fill=(255,255,0),spacing=10,align='center',stroke_width=1)

	image.save(filename)