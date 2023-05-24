import sqlite3 as sql
import json as js

conn = sql.connect('Test.db')

f = open("mytest.json")

data = js.load(f)

addlist = [];

for item in data['people']:
    templist = []
    name = item['name']
    phone = item['phone']
    email = item['emails'][0]
    templist.append(name)
    templist.append(phone)
    templist.append(email)
    addlist.append(templist)

for i in addlist:
    print(i)


c = conn.cursor()

c.execute("INSERT INTO person VALUES(?,?)", addlist)


conn.commit()