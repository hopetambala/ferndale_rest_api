import requests
import json
import pandas as pd
import datetime as DT
from . import  script
#import script #dev if working only on this file

'''
    #Prints cols
    cols = list(df.columns.values)

    for x in cols:
        print(x)
'''

df = pd.read_csv("data_aggregation/data.csv")

'''
Clean
'''
#df = df[['objectId', 'fname', 'lname','nickname', 'sex', 'dob','telephoneNumber','educationLevel','occupation','city','province','clinicProvider','cedulaNumber','surveyingOrganization','latitude','longitude']]


'''
ReClean NaNs
'''
df = df.replace({pd.np.nan: ''})


df_json = df.to_json(orient='records')
df_dict = df.to_dict("records")

#print(df_dict)


