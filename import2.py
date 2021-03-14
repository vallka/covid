import pandas as pd
import sqlite3

data = pd.read_excel ('weekly-deaths-by-location-age-sex.xlsx',
        sheet_name='Data',
        skiprows=4,
        skipfooter=2,
        usecols='A:F',
        header=None,
        names=['yearweek','location','sex','age','cause','deaths'])

data['year'] = data.yearweek.str.slice(0,2).astype(int)
data['week'] = data.yearweek.str.slice(3,5).astype(int)

del data['yearweek']

neworder =['year','week','location','sex','age','deaths','cause']
data = data.reindex(columns=neworder)

print(data)

conn=sqlite3.connect('covid.db')
data.to_sql('weekly_deaths', conn, if_exists='append', index = False)
conn.commit()
