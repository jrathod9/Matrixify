from flask import Flask, render_template , url_for ,flash, redirect, request
app = Flask(__name__)

app.config['SECRET_KEY']='151de16d04dacf29c88db46b69194afb'

@app.route("/")
@app.route("/home")
def home():
	return render_template('index.html')

@app.route("/result",method = ['GET','POST'])
def result():
	return render_template('result.html')

if __name__ == '__main__':
	app.run(debug=True)