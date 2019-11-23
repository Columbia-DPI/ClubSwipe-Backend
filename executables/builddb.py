'''
For this function to work correctly, the server must be running at the given URL
'''
import requests
import json

def send_entry(url, entry):
	payload = {}
	payload["club_data"] = entry
	payload = json.dumps(payload)
	print(payload)
	response = requests.post(url, data=payload)
	print(response.text)

DATA_MOCK = [{
    "name": "Columbia Data Product Initiative",
    "email": "dpi@dpi.com",
    "description": "Description here",
    "website": "https://www.columbiadpi.com/",
    "logo": "https://images.squarespace-cdn.com/content/5d683b6a3f805a000151f7cf/1567126137978-ZRN06BNEQLUIWTE31JSJ/CDPI+logo+large.png?content-type=image%2Fpng"
	},{
    "name": "Columbia Data Product Initiative",
    "email": "dpi@dpi.com",
    "description": "Description here",
    "website": "https://www.columbiadpi.com/",
    "logo": "https://images.squarespace-cdn.com/content/5d683b6a3f805a000151f7cf/1567126137978-ZRN06BNEQLUIWTE31JSJ/CDPI+logo+large.png?content-type=image%2Fpng"
	},{
    "name": "Columbia Data Product Initiative",
    "email": "dpi@dpi.com",
    "description": "Description here",
    "website": "https://www.columbiadpi.com/",
    "logo": "https://images.squarespace-cdn.com/content/5d683b6a3f805a000151f7cf/1567126137978-ZRN06BNEQLUIWTE31JSJ/CDPI+logo+large.png?content-type=image%2Fpng"
	},{
    "name": "Columbia Data Product Initiative",
    "email": "dpi@dpi.com",
    "description": "Description here",
    "website": "https://www.columbiadpi.com/",
    "logo": "https://images.squarespace-cdn.com/content/5d683b6a3f805a000151f7cf/1567126137978-ZRN06BNEQLUIWTE31JSJ/CDPI+logo+large.png?content-type=image%2Fpng"
	}]

for datapoint in DATA_MOCK:
	send_entry("http://localhost:5000/api/addClub", datapoint)
