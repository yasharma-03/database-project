import mysql.connector

def connect():
        data=mysql.connector.connect(host='localhost',user='root',passwd='mnbv@0987', database='bookshop')
        myc=data.cursor()
        #qr='create table IF NOT EXISTS book(id int(8) primary key,title varchar(80),author varchar(30),year int(5),isbn int(20);'
        myc.execute('create table IF NOT EXISTS bookdetail(title varchar(80),author varchar(30),year int(5),ID int(20) primary key);')
        data.commit()
        data.close()

def insert(title,author,year,ID):
        data=mysql.connector.connect(host='localhost',user='root',passwd='mnbv@0987', database='bookshop')
        myc=data.cursor()
        qr="insert into bookdetail(title,author,year,ID)values(%s,%s,%s,%s)"
        rtuple=(title,author,year,ID)
        myc.execute(qr,rtuple)
        data.commit()
        data.close()
        
def view():
        data=mysql.connector.connect(host='localhost',user='root',passwd='mnbv@0987', database='bookshop')
        myc=data.cursor()
        myc.execute('select * from bookdetail')
        rows=myc.fetchall()
        data.close()
        return rows

def search(title='',author='',year='',ID=''):
        data=mysql.connector.connect(host='localhost',user='root',passwd='mnbv@0987', database='bookshop')
        myc=data.cursor()
        myc.execute('select * from bookdetail where title=%s or author=%s or year=%s or ID=%s',(title,author,year,ID))
        rows=myc.fetchall()
        data.close()
        return rows 

def delete(ID):
        data=mysql.connector.connect(host='localhost',user='root',passwd='mnbv@0987', database='bookshop')
        myc=data.cursor()
        myc.execute('delete from bookdetail where ID=%s;',(ID,))
        data.commit()
        data.close()

def update(ID,title,author,year):
        data=mysql.connector.connect(host='localhost',user='root',passwd='mnbv@0987', database='bookshop')
        myc=data.cursor()
        myc.execute('update bookdetail set title=%s,author=%s,year=%s where ID=%s',(title,author,year,ID))
        data.commit()
        data.close()

connect()
#insert('can love happen twice','ravinder singh',2018,66007)
#delete(66008)
#update(34667,'can love happen twice?','ravinder singh',2017)
#print(view())
#print(search(title='someone like you'))

