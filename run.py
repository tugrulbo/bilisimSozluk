import os
import pandas as pd
import mysql.connector
from mysql.connector import Error
import configparser
import json

##Excel Dosyası İşlemleri##
data = pd.read_excel ("../bilisimsozluk/newList.xlsx")#Excel dosyasının bulunduğu dosya yolu
df_English = pd.DataFrame(data, columns= ['english']) #Excel dosyasındaki belirli bir sutunu çekme
df_Turkish = pd.DataFrame(data, columns= ['turkish']) #Excel dosyasındaki belirli bir sutunu çekme
english_Words = df_English.values.tolist()#Excel dosyasındaki bilgileri listeye çevirme
turkish_Words = df_Turkish.values.tolist()#Excel dosyasındaki bilgileri listeye çevirme

#Bilgilerin doğrulu hakkında ufak bir kontrol
for i in range(10):
    print(english_Words[i])
    print(turkish_Words[i])



#Veritabanı Bağlantısı
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="bilisimsozluk"
)

mycursor = mydb.cursor()
k = 0
if k<=len(english_Words):
  for k in range(len(english_Words)):
    word = english_Words[k]
    strWord = json.dumps(word)
    startWord = strWord.replace('"',"")
    en = startWord.replace("[","")
    enWord = en.replace("]","")
    
    wordT = turkish_Words[k]
    strWordT = json.dumps(wordT,ensure_ascii=False)
    startWordT = strWordT.replace('"',"")
    tr = startWordT.replace("[","")
    trWord = tr.replace("]","")
    if(enWord =="NaN"):
      k += 1
      print(f"NaN:{k}")
      continue
    sql = "INSERT INTO words (english, turkish) VALUES (%s, %s)"
    val = (enWord, trWord)
    mycursor.execute(sql, val)
    mydb.commit()
else:
  print("Bir hatayla bir karşılaşıldı")   


print("İşlem tamamlandı")




