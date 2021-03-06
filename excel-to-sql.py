import pandas as pd

from config import cur

all_columns = ['Country','1949' ,'1950' ,'1951','1952' ,'1953',
   '1954' ,'1955', '1956' ,'1957' ,'1958' ,'1959','1960' ,'1961' ,'1962' ,
  '1963'  ,'1964'  ,'1965'  ,'1966'  ,'1967'  ,'1968'  ,'1969'  ,'1970' , 
  '1971'  ,'1972'  ,'1973'  ,'1974'  ,'1975'  ,'1976'  ,'1977'  ,'1978'  ,
  '1979'  ,'1980'  ,'1981'  ,'1982'  ,'1983'  ,'1984'  ,'1985'  ,'1986'  ,'1987' ,
  '1988'  ,'1989' ,'1990' ,'1991' ,'1992' ,'1993' ,'1994' ,'1995' ,'1996' ,
  '1997' ,'1998' ,'1999' ,'2000' ,'2001' ,'2002' ,'2003' ,'2004' ,'2005' ,
  '2006' ,'2007' ,'2008' ,'2009' ,'2010' ,'2011' ,'2012','2013', '2014' ,'2015' ,
  '2016' ,'2017','2018' ,'2019']
_db ="Country,1960,1961,1962,1963 ,1964 ,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019"
# Import CSV
data = pd.read_excel ('./wb.xlsx')   
df = pd.DataFrame(data, columns= all_columns)
for i, row in df.iterrows():
    cursor = cur.cursor ()
    try:
        cursor.execute(f"INSERT INTO `military_expenditure` ({_db}) VALUES(`{row['Series Name']}`,`{row['Series Code']}` ,`{row['Country Name']}` ,`{row['Country Code']}` ,'{row['1960 [YR1960]']}' ,'{row['1961 [YR1961]']}' ,'{row['1962 [YR1962]']}' ,'{row['1963 [YR1963]']}'  ,'{row['1964 [YR1964]']}'  ,'{row['1965 [YR1965]']}'  ,'{row['1966 [YR1966]']}'  ,'{row['1967 [YR1967]']}'  ,'{row['1968 [YR1968]']}'  ,'{row['1969 [YR1969]']}'  ,'{row['1970 [YR1970]']}' , '{row['1971 [YR1971]']}'  ,'{row['1972 [YR1972]']}'  ,'{row['1973 [YR1973]']}'  ,'{row['1974 [YR1974]']}'  ,'{row['1975 [YR1975]']}'  ,'{row['1976 [YR1976]']}'  ,'{row['1977 [YR1977]']}'  ,'{row['1978 [YR1978]']}'  ,'{row['1979 [YR1979]']}'  ,'{row['1980 [YR1980]']}'  ,'{row['1981 [YR1981]']}'  ,'{row['1982 [YR1982]']}'  ,'{row['1983 [YR1983]']}'  ,'{row['1984 [YR1984]']}'  ,'{row['1985 [YR1985]']}'  ,'{row['1986 [YR1986]']}'  ,'{row['1987 [YR1987]']}' ,'{row['1988 [YR1988]']}'  ,'{row['1989 [YR1989]']}' ,'{row['1990 [YR1990]']}' ,'{row['1991 [YR1991]']}' ,'{row['1992 [YR1992]']}' ,'{row['1993 [YR1993]']}' ,'{row['1994 [YR1994]']}' ,'{row['1995 [YR1995]']}' ,'{row['1996 [YR1996]']}' ,'{row['1997 [YR1997]']}' ,'{row['1998 [YR1998]']}' ,'{row['1999 [YR1999]']}' ,'{row['2000 [YR2000]']}' ,'{row['2001 [YR2001]']}' ,'{row['2002 [YR2002]']}' ,'{row['2003 [YR2003]']}' ,'{row['2004 [YR2004]']}' ,'{row['2005 [YR2005]']}' ,'{row['2006 [YR2006]']}' ,'{row['2007 [YR2007]']}' ,'{row['2008 [YR2008]']}' ,'{row['2009 [YR2009]']}' ,'{row['2010 [YR2010]']}' ,'{row['2011 [YR2011]']}' ,'{row['2012 [YR2012]']}','{row['2013 [YR2013]']}', '{row['2014 [YR2014]']}' ,'{row['2015 [YR2015]']}' ,'{row['2016 [YR2016]']}' ,'{row['2017 [YR2017]']}','{row['2018 [YR2018]']}' ,'{row['2019 [YR2019]']}')")
    except Exception as e: print(e)
        print(row['Country'])

    #Create Tables
    """ try:
        cursor.execute(f"CREATE TABLE `{row['Series Name']}` (`Series_Name` varchar(255) DEFAULT NULL,`Series_Code` varchar(255) DEFAULT NULL,`Country_Name` varchar(255) DEFAULT NULL,`Country_Code` varchar(255) DEFAULT NULL,`_1960` varchar(255) DEFAULT NULL,`_1961` varchar(255) DEFAULT NULL,`_1962` varchar(255) DEFAULT NULL,`_1963` varchar(255) DEFAULT NULL,`_1964` varchar(255) DEFAULT NULL,`_1965` varchar(255) DEFAULT NULL,`_1966` varchar(255) DEFAULT NULL,`_1967` varchar(255) DEFAULT NULL,`_1968` varchar(255) DEFAULT NULL,`_1969` varchar(255) DEFAULT NULL,`_1970` varchar(255) DEFAULT NULL,`_1971` varchar(255) DEFAULT NULL,`_1972` varchar(255) DEFAULT NULL,`_1973` varchar(255) DEFAULT NULL,`_1974` varchar(255) DEFAULT NULL,`_1975` varchar(255) DEFAULT NULL,`_1976` varchar(255) DEFAULT NULL,`_1977` varchar(255) DEFAULT NULL,`_1978` varchar(255) DEFAULT NULL,`_1979` varchar(255) DEFAULT NULL,`_1980` varchar(255) DEFAULT NULL,`_1981` varchar(255) DEFAULT NULL,`_1982` varchar(255) DEFAULT NULL,`_1983` varchar(255) DEFAULT NULL,`_1984` varchar(255) DEFAULT NULL,`_1985` varchar(255) DEFAULT NULL,`_1986` varchar(255) DEFAULT NULL,`_1987` varchar(22) DEFAULT NULL,`_1988` varchar(255) DEFAULT NULL,`_1989` varchar(255) DEFAULT NULL,`_1990` varchar(255) DEFAULT NULL,`_1991` varchar(255) DEFAULT NULL,`_1992` varchar(255) DEFAULT NULL,`_1993` varchar(255) DEFAULT NULL,`_1994` varchar(255) DEFAULT NULL,`_1995` varchar(255) DEFAULT NULL,`_1996` varchar(255) DEFAULT NULL,`_1997` varchar(255) DEFAULT NULL,`_1998` varchar(255) DEFAULT NULL,`_1999` varchar(255) DEFAULT NULL,`_2000` varchar(255) DEFAULT NULL,`_2001` varchar(255) DEFAULT NULL,`_2002` varchar(255) DEFAULT NULL,`_2003` varchar(255) DEFAULT NULL,`_2004` varchar(255) DEFAULT NULL,`_2005` varchar(255) DEFAULT NULL,`_2006` varchar(255) DEFAULT NULL,`_2007` varchar(255) DEFAULT NULL,`_2008` varchar(255) DEFAULT NULL,`_2009` varchar(255) DEFAULT NULL,`_2010` varchar(255) DEFAULT NULL,`_2011` varchar(255) DEFAULT NULL,`_2012` varchar(255) DEFAULT NULL,`_2013` varchar(255) DEFAULT NULL,`_2014` varchar(255) DEFAULT NULL,`_2015` varchar(22) DEFAULT NULL,`_2016` varchar(255) DEFAULT NULL,`_2017` varchar(255) DEFAULT NULL,`_2018` varchar(255) DEFAULT NULL,`_2019` varchar(255) DEFAULT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;")
    except:
        pass """
    cur.commit ()
