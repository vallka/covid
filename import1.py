import pandas as pd
import sqlite3

data = pd.read_excel ('weekly-deaths-by-location-age-group-sex-15-19.xlsx',
        sheet_name='Data',
        skiprows=4,
        skipfooter=2,
        usecols='A:F',
        header=None,
        names=['year','week','location','sex','age','deaths'])

data['cause'] = ''

print(data)

conn=sqlite3.connect('covid.db')
data.to_sql('weekly_deaths', conn, if_exists='replace', index = False)
conn.commit()
