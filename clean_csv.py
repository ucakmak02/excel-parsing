
# importing the module 
import pandas as pd  
    
# making data frame from the csv file  
dataframe = pd.read_csv("libya.csv")  
    
# using the replace() method 
dataframe.replace(to_replace ="\n",  
                 value = "",  
                  inplace = True) 
  
# writing  the dataframe to another csv file 
dataframe.to_csv('outputfile.csv',  
                 index = False)