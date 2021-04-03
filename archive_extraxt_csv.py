import pandas as pd
import MySQLdb
import csv

from config import cur
cursor = cur.cursor ()
cursor.execute(f'Select aoi,timeInterval,assesment from key_event_archive ')
data = cursor.fetchall()

df = pd.DataFrame(data,columns=['Aoi','Time Interval','Assesment'])
df.to_csv (r'archive-info.csv', index = False) # place 'r' before the path name to avoid any errors in the path