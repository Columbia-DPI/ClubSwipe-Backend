from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def render_index():
	return render_template('index.html')

@app.route("/api/getData", methods=["POST"])
def get_data():
	return "Hello, world!"

if __name__ == "__main__":
    app.run()

