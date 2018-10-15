import pyodbc as db
server = '192.168.18.36'
database = 'HBK_Test'
username = 'maheshp'
password = 'Welcome123'
cnxn = db.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
               # "Trusted_Connection = yes;")
#cur = con.cursor()
# cursor.execute("create table samples(id int)")
# cursor.commit()
cursor.execute("insert into samples values(:id)",{'id':3})
cursor.commit()
cursor.execute("Select * from samples")
row=cursor.fetchall()
# print(row)
# cursor.execute('select * from All_Rice')
# row=cursor.fetchall()
# print(len(row))
for i in row:
    print(i)


