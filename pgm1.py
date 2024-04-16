import mysql.connector
con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sample1"
)
print(con)
mycursor=con.cursor()
#mycursor.execute("create database sample1")
#mycursor.execute("create table student(stud_id int auto_increment primary key,name varchar(255),place varchar(255))")
sql='insert into student(name,place) values(%s,%s)'
value=[('appu','aaa'),('meenu','mmm')]
mycursor.executemany(sql,value)
mycursor.execute('insert into student(name,place) values("aram","pala")')
con.commit()