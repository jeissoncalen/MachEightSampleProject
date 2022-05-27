#!/usr/bin/env python
import requests
import pandas
from requests.structures import CaseInsensitiveDict

input = int(input("Enter your input value: "))
## 1. Get data from server
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
resp = requests.get("https://mach-eight.uc.r.appspot.com/", headers=headers).json()['values']
## 2. Build pandas dataframe 
df = pandas.DataFrame(resp)
df['h_in'] = df['h_in'].astype(int)
## 3. Extract unique values H_In to iterate object 
hInUniqueValues = df['h_in'].unique().tolist()
resultHIn = []
## 4. Find pairs values H_In 
## Values hIn1 + hIn2 = input
for hIn1 in hInUniqueValues:
    hIn2 = input - hIn1
    if hIn2 in hInUniqueValues:
      hInUniqueValues.remove(hIn2)
      resultHIn.append([df.query('h_in == '+str(hIn1)), df.query('h_in == '+str(hIn2))])
## 5. Print values
contador = 0
print('app',input)
if len(resultHIn)>0:
    for df1, df2 in resultHIn:
      ##Pairs players with same heigth
      if df1.equals(df2):
          for index1,row1 in df1.iterrows():
            for index2,row2 in df1.iterrows():
              if(index1 < index2):
                contador+=1
                print(contador,row1['first_name'], row1['last_name'],'-',row2['first_name'], row2['last_name'])
      else:
      ##Pairs players with different heigth
        for index1, row1 in df1.iterrows():
          for index2, row2 in df2.iterrows():
            contador+=1
            print(contador,row1['first_name'], row1['last_name'],'-',row2['first_name'], row2['last_name'])
else:
    print("No matches found")