from flask import Flask
app= Flask(__name__)

@app.route("/")
def home():
	return "HELLO WORLD FROM VERCEL USING FLASK"


@app.route("/about")
def about():
	return "HELLO ABOUT"