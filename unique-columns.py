from more_itertools import unique_everseen
with open('archive-info.csv','r') as f, open('archive-info-unique.csv','w') as out_file:
    out_file.writelines(unique_everseen(f))