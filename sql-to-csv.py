import pandas as pd
import MySQLdb
import csv
""" and (voting_average IS NOT NULL OR news_class != "None") """

from config import cur

""" import pandas as pd
import csv

import MySQLdb
cur = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="blackbird",         # your username
                     passwd="1986#Eagle?",  # your password
                     db="bh_db")        # name of the data base """

cursor = cur.cursor ()
cursor.execute(f'Select news_id,news_date,full_content,site_id,aoi,latLng,news_location,title,link,news_class,voting_average from news_api where aoi="libya" and api_source="Event Registry" and (news_date BETWEEN "2020-01-01" AND "2021-01-01") ')
data = cursor.fetchall()

df = pd.DataFrame(data,columns=['Id','News Date','Body','Source','Country','Location (LatLng)','Locations','Headline','URL','Clases','Scale'])
df.to_csv (r'libya.csv', index = False) # place 'r' before the path name to avoid any errors in the path

""" scp -r root@51.15.243.166:/root/energy-2020.csv /Users/ugurcakmak/hs/projects/excel-parsing """




""" import pandas as pd

f=pd.read_csv("energy3.csv")
keep_col = ['Id','News Date','Source','Country','Location (LatLng)','Locations','Headline','URL','Abstract','First Part','_Body']
new_f = f[keep_col]
new_f.to_csv("energy-output-all.csv", index=False) """