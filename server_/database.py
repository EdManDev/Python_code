#! usr/bin/python3
import pymysql

server = pymysql.connect(host="localhost", user="root",passwd="mine")

cursor = server.cursor()

sql ="CREATE DATABASE IF NOT EXIST EdMan;"
cursor.execute(sql)

sql = "USE EdMan ;"
cursor.execute(sql)

sql='''CREATE TABLE IF NOT EXIST owners (id integer NOT NULL AUTO_INCREMENT,
                                        name varchar(30) NOT NULL,
                                        gender varchar(7),
                                        phone varchar(10),
                                        PRIMARY KEY (id));'''
cursor.execute(sql)
sql= 'CREATE TABLE IF NOT EXISTS pets(pet_id integer NOT NULL AUTO_INCREMENT, owner_id integer, name varchar(30),gender varchar varchar(7), species varchar(20),color varchar(10), age integer, PRIMARY KEY (pet_id), FOREIGN KEY (owner_id) REFERNECES owners(id));'
cursor.execute(sql)

sql="SHOW tables;"
cursor.execute(sql)
print(cursor.fetchall())