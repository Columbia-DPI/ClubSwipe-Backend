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

#while(sheet["A"+str(iterator)].value!=None):
print(sheet['A'+str(iterator)].value)
iterator+=1
