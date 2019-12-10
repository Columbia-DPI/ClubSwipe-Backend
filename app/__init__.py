from flask import Flask, render_template, request, jsonify
from .modules import MongoHelper
from .modules import RegressionModel

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True
db, usercol, clubcol = MongoHelper.init_Mongo()

@app.route("/api/login", methods=["POST"])
def login():
	post_data = request.get_json()
	email = post_data["email"]
	password = post_data["password"]
	hasher = hashlib.sha256()
	hasher.update(password.encode('utf8'))
	password = hasher.digest()
	# Check the mongo to log the user in
	statusCode = "3" # Different statuses would symbolise different types of issues, while 0 would imply a successful login - used to update the frontend

	resultJson = MongoHelper.DB_login_user(db, usercol, email, password, statusCode)
    
	print(resultJson)

	'''
	Status Codes:
	0 - Sucessful
	1 - Wrong Password
	2 - Email ID doesn't exist
	3 - Unforseen error
	'''

	return resultJson


@app.route("/api/signup", methods=["POST"])
def signup():
	return True

@app.route("/api/fetchAllClubs", methods=["GET"])
def fetch_all_clubs():
	payload = MongoHelper.fetchClubs()
	return jsonify(payload)

@app.route("/api/fetchCuratedClubs", methods=["POST"])
def fetch_curated_clubs():
	# Do some ML stuff here
	vector = request.get_json(force=True)
	
	#testVector = {"active": '0.7', "governing": '0', "tech design": '0', "music arts": '0', "preproffesional": '0.2', "publications": '0', "activism service": '0.1', "hours": '0', "selectivity": '0', "size": '0'}

	club = RegressionModel.optimize(db, clubcol, vector)
	print(club)

	return jsonify(club)

# Ishaan - this is what you need to call. If you run the server and make a POST call to this route, then it adds the payload to the MongoDB backend
'''Sample POST payload call:
{
	"club_data": {
    "name": "Columbia Data Product Initiative",
    "email": "dpi@dpi.com",
    "description": "Description here",
    "website": "https://www.columbiadpi.com/",
    "logo": "https://images.squarespace-cdn.com/content/5d683b6a3f805a000151f7cf/1567126137978-ZRN06BNEQLUIWTE31JSJ/CDPI+logo+large.png?content-type=image%2Fpng"
	}
}
'''
@app.route("/api/addClub", methods=["POST"])
def add_club():
	post_data = request.get_json(force=True)
	payload = post_data["club_data"]
	MongoHelper.DB_insert_club(db, clubcol, payload)
	return jsonify({"valid":True})

@app.route("/")
@app.route("/index")
def render_index():
	return render_template('index.html')

if __name__ == "__main__":
    app.run()

