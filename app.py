from flask import Flask, render_template , url_for ,flash, redirect, request
app = Flask(__name__)
from PIL import Image

app.config['SECRET_KEY']='151de16d04dacf29c88db46b69194afb'

# SYMBOLS = ['.',',',':',';','+','*','?','%','S','#','@']
SYMBOLS = ['.',',',':',';','1','2','3','4','5','6','@']
resize_width = 50
# SYMBOLS = SYMBOLS[::-1]

def resize(image):
    (curr_w, curr_h) = image.size
    new_h = int(float(curr_h)/float(curr_w) * resize_width)		#aspect ratio * width
    dimensions = (resize_width, new_h)
    new_image = image.resize(dimensions)
    return new_image

def symbolizer(image):
	scaler = 25
	new_image_pixels = []
	pixels = list(image.getdata())
	for pixel in pixels:
		new_image_pixels.append(SYMBOLS[pixel//scaler])
	return new_image_pixels


@app.route("/")
@app.route("/home",methods = ['GET','POST'])
def home():
	return render_template('index.html')

@app.route("/result",methods = ['GET','POST'])
def result():
	if request.method == 'POST':
		image = request.form["file"]
		im = Image.open(image,'r')
		im = resize(im)
		clr=[]
		im_list = list(im.getdata())
		for ele in im_list:
			clr.append(ele)
		im = im.convert('L')
		im = symbolizer(im)

		count = 0
		length = len(im)
		new_image = [im[index:index+resize_width] for index in range(0, length, resize_width)]
		for ele in new_image:
			for pixel in ele:
				pixel = [pixel,clr[0],clr[1],clr[2],clr[3]]
				print(pixel[0],end="")
			print("")
	return render_template('result.html',image = new_image)

if __name__ == '__main__':
	app.run(debug=True)