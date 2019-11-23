import pandas as pd
import numpy as np


df = pd.read_excel('../clubdb.xlsx');
#print(df.ix[:, 'Club Name']);

dfToList = df['Club Name'].tolist()
dfToList = dfToList[1:]

dfSet = set(dfToList);
dfList = list(dfToList);

for element in dfList:
    print(element);
