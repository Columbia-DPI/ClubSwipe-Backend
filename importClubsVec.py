import requests
from openpyxl import Workbook, load_workbook
import pandas as pd
import numpy as np
import json


URL='http://127.0.0.1:5000/api/addClub'
# df = pd.read_excel('clubdb.xlsx');
#print(df.ix[:, 'Club Name']);

# dfToList = df['Club Name'].tolist()
# dfToList = dfToList[1:]
#
# dfSet = set(dfToList);
# dfList = list(dfToList);
# for element in dfList:

excel = load_workbook(filename = 'expo.xlsx')
sheet=excel.active
iterator=2
letters=['A','B','C','D','E','F','G','H','I','J','K']
while(sheet["A"+str(iterator)].value!=None):
    doc= {
        'club_data':{
                "name": sheet['A'+str(iterator)].value,
                "email": "dpi@dpi.com",
                "description": "Description here",
                "website": "https://www.columbiadpi.com/",
                "logo": "https://images.squarespace-cdn.com/content/5d683b6a3f805a000151f7cf/1567126137978-ZRN06BNEQLUIWTE31JSJ/CDPI+logo+large.png?content-type=image%2Fpng"
            	"vector":{
            			"active": sheet['B'+str(iterator)].value,
            			"governing": sheet['C'+str(iterator)].value,
            			"tech design": sheet['D'+str(iterator)].value,
            			"music arts": sheet['E'+str(iterator)].value,
            			"preproffesional": sheet['F'+str(iterator)].value,
            			"publications": sheet['G'+str(iterator)].value,
            			"activism service": sheet['H'+str(iterator)].value,
            			"hours": sheet['K'+str(iterator)].value,
            			"selectivity": sheet['J'+str(iterator)].value,
            			"size": sheet['I'+str(iterator)].value,
            		}
            }
        }

    data_string = json.dumps(doc) #data serialized

    r=requests.post( URL,data_string)
    print(r)
