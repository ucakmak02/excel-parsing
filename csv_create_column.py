#Format
""" 
News Date —> Haberin çekildiği tarih
Event Date —> Haberin tarihi
Source —> Kaynak
Country —> Libya
Location —> Bizim cikardigimiz location i koyabiliriz.
Author —> Haber yazarı
Headline —> Haber basligi
Abstract —> Koyu renkli yazılan headline in altında, haberin başındaki yer. Bunu ayrica belirtiyor mu eventregistery?
First Part —> Abstract haric, Ilk 5 cumle
Body —> Haber body
Tags —> Haberin en altındaki taler. Bunu cekmiyor olabiliriz.
URL —> Haberin linki 
"""


from nltk import tokenize
""" print(len(tokenize.sent_tokenize(text)))


import csv
with open('energy.csv','rt')as f:
  data = csv.reader(f)
  for row in data:
       _text = row[1]
       tokenize.sent_tokenize(_text) """

import csv

with open('energy2.csv','r') as csvinput:
    with open('energy3.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []
        row = next(reader)
        """ row.append('Abstract') """
        """ row.append('First Part') """
        row.append('_Body')
        all.append(row)

        for row in reader:
            _text = row[2]
            """ _list = tokenize.sent_tokenize(_text)[0:2] """
            """ _list = tokenize.sent_tokenize(_text)[2:6] """
            _list = tokenize.sent_tokenize(_text)[6:]
            text = ""
            for i in _list:
                text = text + i
            row.append(text)
            all.append(row)

        writer.writerows(all)