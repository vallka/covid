import pandas as pd
import sqlite3

data1 = pd.read_excel ('weekly-deaths-by-location-age-group-sex-15-19.xlsx',
        sheet_name='Data',
        skiprows=4,
        skipfooter=2,
        usecols='A:F',
        header=None,
        names=['year','week','location','sex','age','deaths'])

data1['cause'] = ''

#print(data)

conn=sqlite3.connect('covid.db')
data1.to_sql('weekly_deaths', conn, if_exists='replace', index = False)
conn.commit()

data2 = pd.read_excel ('weekly-deaths-by-location-age-sex.xlsx',
        sheet_name='Data',
        skiprows=4,
        skipfooter=2,
        usecols='A:F',
        header=None,
        names=['yearweek','location','sex','age','cause','deaths'])

data2['year'] = data2.yearweek.str.slice(0,2).astype(int)
data2['week'] = data2.yearweek.str.slice(3,5).astype(int)

del data2['yearweek']

neworder =['year','week','location','sex','age','deaths','cause']
data2 = data2.reindex(columns=neworder)

#print(data2)

conn=sqlite3.connect('covid.db')
data2.to_sql('weekly_deaths', conn, if_exists='append', index = False)
conn.commit()
