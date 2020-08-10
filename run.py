import os
import pandas as pd
import mysql.connector
from mysql.connector import Error
import configparser
import json

##Excel Dosyası İşlemleri##
data = pd.read_excel ("../bilisimsozlukbotu/words.xlsx")
df_English = pd.DataFrame(data, columns= ['English']) #Excel dosyasındaki belirli bir sutunu çekme
df_Turkish = pd.DataFrame(data, columns= ['Turkish']) #Excel dosyasındaki belirli bir sutunu çekme
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

sql = "INSERT INTO words (english, turkish) VALUES (%s, %s)"
val = (json.dumps(english_Words[0]), json.dumps(turkish_Words[0]))
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")



