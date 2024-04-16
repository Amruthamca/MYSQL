import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="",database="sample")
print(con)
mycursor=con.cursor()
#mycursor.execute("create database sample")
""" mycursor.execute("show databases")
result=mycursor.fetchall()
for i in result:
    print(i) """
#mycursor.execute("create table person(person_id int,name varchar(255),address varchar(255))")
""" mycursor.execute('insert into person values(101,"ammu","abc")')
con.commit() """
#mycursor.execute("create table student(id int auto_increment primary key,name varchar(255),address varchar(255))")
#mycursor.execute('insert into student(name,address) values("malu","bca")')
""" sql="insert into student(name,address) values(%s,%s)"
value=[("anju","aaa"),("arun","bbb"),("anu","ccc")]
mycursor.executemany(sql,value)
con.commit() """
#mycursor.execute("update student set name='meenu' where id=4 ")
#mycursor.execute("delete from student where id=4")
#con.commit()
""" mycursor.execute("select * from student where id=3")
result=mycursor.fetchall()
for i in result:
    print(i) """
""" mycursor.execute("select * from student")
result=mycursor.fetchone()
print(result) """
#mycursor.execute("select * from student order by name")
#mycursor.execute("select *from student where name like '%u'")
mycursor.execute("select *from student limit 2 offset 1")
result=mycursor.fetchall()
for i in result:
    print(i)
