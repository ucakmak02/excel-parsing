import pandas as pd  
    
# making data frame  
data = pd.read_csv("afghanistan.csv")  
    
# calling head() method   
# storing in new variable  
data_top = data.head()  
    
# display  
print(data_top) 