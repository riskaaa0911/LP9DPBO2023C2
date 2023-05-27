import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="drakor_baru"   
)

dbcursor = mydb.cursor()

sql = "INSERT INTO writer(nama_writer) VALUES ('Kim Eun Sook')"
dbcursor.execute(sql)

mydb.commit()

print(dbcursor.rowcount, "record inserted.")

dbcursor = mydb.cursor()
dbcursor.execute("SELECT * FROM writer")

myresult = dbcursor.fetchall()
print("Daftar Penulis")
for x in myresult:
    print(x)
    
dbcursor = mydb.cursor()
sql = "DELETE FROM writer WHERE nama_writer = 'Kim Eun Sook'"
dbcursor.execute(sql)

mydb.commit()

print(dbcursor.rowcount, "record(s) deleted")

print("Daftar Penulis setelah dihapus")

dbcursor = mydb.cursor()
dbcursor.execute("SELECT * FROM writer")

myresult = dbcursor.fetchall()

for x in myresult:
    print(x)
    