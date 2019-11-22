from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/api/getData", methods=["POST"])
def get_data():
	return "Hello, world!"

@app.route("/api/login", methods=["POST"])
def login():
	post_data = request.get_json()
	email = post_data["email"]
	password = post_data["password"]
	hasher = hashlib.sha256()
	hasher.update(password.encode('utf8'))
	password = hasher.digest()
	# Check the mongo to log the user in
	result = {}
	return result


@app.route("/api/signup", methods=["POST"])
def signup():
	return True

@app.route("/api/fetchAllClubs", methods=["POST"])
def fetch_all_clubs():
	return None

@app.route("/api/fetchCuratedClubs", methods=["POST"])
def fetch_curated_clubs():
	return None

@app.route("/")
@app.route("/index")
def render_index():
	return render_template('index.html')

if __name__ == "__main__":
    app.run()

