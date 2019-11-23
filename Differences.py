
FROM init

        @app.route("/api/searchClubs", methods=["POST"])
        def search_clubs():
        	payload=MongoHelper.fetchClubs()
        	post_data = request.get_json()
        	keyword=post_data["keywords"]
        	searched_clubs=[]
        	for club in payload:
        		for key in keyword:
        			if keyword[key].lower() in club["name"].lower():
        				searched_clubs.append(club)
        	return searched_clubs
'''Sample POST search payload call:
{
	"keywords": {
    	"keyword": "dpi"
	}
}
'''
