import requests
import json

def save_data(filename, data):
	with open(filename, 'w') as fp:
		json.dump(data, fp)

URL='http://127.0.0.1:5000/api/fetchCuratedClubs'
URL2='http://127.0.0.1:5000/api/fetchAllClubs'
# df = pd.read_excel('clubdb.xlsx');
#print(df.ix[:, 'Club Name']);

# dfToList = df['Club Name'].tolist()
# dfToList = dfToList[1:]
#
# dfSet = set(dfToList);
# dfList = list(dfToList);
# for element in dfList:

# excel = load_workbook(filename = 'expo.xlsx')
# sheet=excel.active
# iterator=2
doc={"get duped stupid": "lol"}
data_string = json.dumps(doc) #data serialized

r=requests.post(URL,data_string)

save_data("curated.json", r.json())
# print(r)

r = requests.get(url=URL2)
save_data("all.json", r.json())

