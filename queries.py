import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="",database="sample3")
print(con)
mycursor=con.cursor()
#mycursor.execute("create database sample3")
""" mycursor.execute('create table worker(worker_id int auto_increment primary key,first_name varchar(255),last_name varchar(255),salary int,joining_date varchar(255),department varchar(255))')
sql="insert into worker(first_name,last_name,salary,joining_date,department) values(%s,%s,%s,%s,%s)"
value=[('amrutha','biju',60000,' feb 2024','python'),
       ('anna','jose',20000,'jan 2021','java'),
       ('bharath','kumar',60000,'feb 2014','angular'),
       (' anite','jose',40000,' dec 2023','admin'),
       ('vipul','prakash',250000,'feb 2014','python'),
       ('satish','tom',90000,'march 2018','admin')]
mycursor.executemany(sql,value)
con.commit() """
""" mycursor.execute("select first_name as WORKER_NAME from worker")
result=mycursor.fetchall()
for i in result:
    print(i) """
""" mycursor.execute("select upper(first_name) from worker")
result=mycursor.fetchall()
for i in result:
    print(i) """
""" mycursor.execute("select left(first_name,3) from worker")
result=mycursor.fetchall()
for i in result:
    print(i) """
""" mycursor.execute("select RTRIM(first_name) from worker")
result=mycursor.fetchall()
for i in result:
    print(i)  """
""" mycursor.execute("select count(distinct department) from worker")
result=mycursor.fetchall()
for i in result:
    print(i)  """
""" mycursor.execute("select concat(first_name, ' ', last_name) as COMLETE_NAME from worker")
result=mycursor.fetchall()
for i in result:
    print(i) """
""" mycursor.execute("select * from worker order by first_name asc")
result=mycursor.fetchall()
for i in result:
    print(i)  """
""" mycursor.execute("select *from worker order by first_name asc ,department desc")
result=mycursor.fetchall()
for i in result:
    print(i)  """
""" mycursor.execute("select *from worker where first_name in('vipul','satish')")
result=mycursor.fetchall()
for i in result:
    print(i) """
""" mycursor.execute("select *from worker where first_name not in('vipul','satish')")
result=mycursor.fetchall()
for i in result:
    print(i) """
""" mycursor.execute("select *from worker where department='admin'")
result=mycursor.fetchall()
for i in result:
    print(i) """
""" mycursor.execute("select *from worker where first_name like '%a%'")
result=mycursor.fetchall()
for i in result:
    print(i)  """ 
""" mycursor.execute("select *from worker where first_name like '%a'")
result=mycursor.fetchall()
for i in result:
    print(i) """
""" mycursor.execute("select *from worker where first_name like '%h' and length(first_name)=6 ")
result=mycursor.fetchall()
for i in result:
    print(i)  """
""" mycursor.execute("select *from worker where salary between 100000 and 500000")
result=mycursor.fetchall()
for i in result:
    print(i) """
""" mycursor.execute("select * from worker where joining_date='feb 2014'")
result=mycursor.fetchall()
for i in result:
    print(i) """
""" mycursor.execute("select count(*) as total_workers_in_admin from worker where department='admin'")
result=mycursor.fetchall()
for i in result:
    print(i) """
""" mycursor.execute("select first_name,last_name,salary from worker where salary>=50000 and salary<=100000")
result=mycursor.fetchall()
for i in result:
    print(i)  """
""" mycursor.execute("select department,count(*) as n_oworkers from worker group by department order by n_oworkers desc")
result=mycursor.fetchall()
for i in result:
    print(i) """