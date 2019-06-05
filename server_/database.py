#! usr/bin/python3
import pymysql

server = pymysql.connect(host="localhost", user="root",passwd="mine")

cursor = server.cursor()

sql ="CREATE DATABASE IF NOT EXIST EdMan;"
cursor.execute(sql)

sql = "USE EdMan ;"
cursor.execute(sql)

sql=CREATE TABLE IF NOT EXIST owners (id integer NOT NULL AUTO_INCREMENT,)

