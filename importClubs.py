import requests
from openpyxl import Workbook, load_workbook
import pandas as pd
import numpy as np
import json


URL='http://127.0.0.1:5000/api/addClub'
df = pd.read_excel('clubdb.xlsx');
#print(df.ix[:, 'Club Name']);

dfToList = df['Club Name'].tolist()
dfToList = dfToList[1:]

dfSet = set(dfToList);
dfList = list(dfToList);
for element in dfList:
    print(type(element))
    doc= {
        'club_data':{
                'name': element,
                'email': 'Coming Soon!',
                'description': 'Coming Soon!',
                'website': 'Coming Soon!',
                'logo': 'Coming Soon!'
            }
        }

    data_string = json.dumps(doc) #data serialized

    r=requests.post( URL,data_string)
    print(r)
