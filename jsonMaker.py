import requests
from openpyxl import Workbook, load_workbook
import pandas as pd
import numpy as np
import json


URL='http://127.0.0.1:5000/api/fetchCuratedClubs'
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

r=requests.post( URL,data_string)
print(r)
URL='http://127.0.0.1:5000/api/fetchAllClubs'

r = requests.get(url = URL)
print(r)
