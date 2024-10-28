import MySQLdb 
db=MySQLdb.connect(host="127.0.0.1",user="root",password="",database="sample")
cursor=db.cursor()
try:
    cursor.execute("select * from emp")
    db.commit
except Exception as e:
    print(e)
else:
    print("success")