import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost", user = "root", password = "root", db = "DB_SCHEME"
)

#print(mydb)

'''
#select statement
mycursor = mydb.cursor()
mycursor.execute("select * from cbr")
var = mycursor.fetchall()
#print(var)
for all in var:
    print(all)
'''

'''
# insert statement
mycursor = mydb.cursor()
sql = "insert into cbr values(%s, %s, %s, %s, %s, %s, %s)"
val = (None,100,0,0,"normal","yes","yes")
mycursor.execute(sql,val)
mydb.commit()

#or
mycursor = mydb.cursor()
mycursor.execute("insert into cbr values(null,100,0,0,'normal','yes','yes')")
'''

'''
# delete statement
mycursor = mydb.cursor()
mycursor.execute("delete from cbr where Patient_ID = 7")
mydb.commit()
'''



