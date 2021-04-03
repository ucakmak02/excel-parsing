import pandas as pd
import MySQLdb
import csv

from config import cur

""" import pandas as pd
import csv

import MySQLdb
cur = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="blackbird",         # your username
                     passwd="1986#Eagle?",  # your password
                     db="bh_db")        # name of the data base """
cursor = cur.cursor ()
cursor.execute('Select news_date,SUBSTRING_INDEX(full_content,".",2),SUBSTRING_INDEX(SUBSTRING_INDEX(full_content, ".",  8), ".", -4) ,SUBSTRING(full_content, LOCATE(SUBSTRING_INDEX(SUBSTRING_INDEX(full_content, ".",  8), ".", -4), full_content)),site_id,aoi,latLng,news_location,title,source_text,link,voting_average,news_class from news_api where aoi="energy" and api_source="Event Registry" and (voting_average IS NOT NULL OR news_class != "None")')
data = cursor.fetchall()

df = pd.DataFrame(data,columns=['News Date','Abstract','First Part','Body','Source','Country','Location (LatLng)','Locations','Headline','First Part','URL','Voting','Class'])
df.to_csv (r'energy.csv', index = False) # place 'r' before the path name to avoid any errors in the path

""" scp -r root@51.15.243.166:/root/libya.csv /Users/ugurcakmak/hs/projects/excel-parsing """