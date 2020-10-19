#! /usr/bin/python
import psycopg2, sys, os, random
from random import randint
import django
from faker import Faker
from django.db import IntegrityError
import sqlite3
from sqlite3 import Error
from django.db import transaction
from django.db import models

fake = Faker('es_ES')

fecha_inicio = '2019-05-01'
fecha_finalizacion = '2019-05-22'
curs_id = ""

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print("conexio amb la base de dades correcte")
        return conn
    except Error as e:
        print("conexio erronia")
        sys.exit(1)
 
    return None

def add_cursos(cur,num):
    c = cur.cursor()
    c.execute("DELETE FROM Curso")
    Cursos_uni = ['DABD 2019', 'DABD 2020', 'DABD 2018', 'DABD 2017', 'DABD 2016', 'DABD 2015','DABD 2014','DABD 2013','DABD 2012']
    for i in range(num):
        item = [(random.choice(Cursos_uni)),fake.past_date(start_date="-330d", tzinfo=None),fake.date_between_dates(date_start=None, date_end=None)]
        c.execute('insert or ignore into Curso values (?,?,?)', item)
        c.execute("SELECT last_insert_rowid();")
        curs_id = c.fetchone()[0] 
    print('Cursos ok')

def add_practica(cur,num):
    c = cur.cursor()
    c.execute("DELETE FROM tfg_practica")
    Practicas_uni = ['Exercici1','Exercici2','Exercici3','Exercici4','Exercici5','Exercici6','Exercici7','Exercici8','Exercici9','Exercici10','Exercici11','Exercici12','Exercici13']
    for i in range(num):
        item = [(random.choice(Practicas_uni)),fake.date_between_dates(date_start=None, date_end=None)]
        c.execute('insert or ignore into tfg_practica values (?,?)', item)
    print('Practica ok')

def add_alumno(cur,num):
    c = cur.cursor()
    c.execute("DELETE FROM Alumno")
    for i in range(num):
        item = [fake.ean(length=8),fake.first_name(),fake.last_name(),fake.last_name(), fake.free_email(), False]
        c.execute('insert or ignore into Alumno values (?,?,?,?,?,?)', item )
        b = c.execute("SELECT last_insert_rowid();")
        #b.curs_id.add(b,curs_id)
        #c.execute("INSERT INTO Alumno (dni, nombre, apellido1,apellido2,email,repetidor,curs) VALUES ("fake.ean(length=8),fake.first_name(),fake.last_name(),fake.last_name(), fake.free_email(), False, str(curs_id)")
    print('Alumnos ok')

def add_nota(cur,num):
    c = cur.cursor()
    c.execute("DELETE FROM Nota")
    for i in range(num):
        item2 = [randint(0,10)]
        c.execute('insert or ignore into Nota values (?)', item )

def main():
    database = "/home/victor/Escritorio/django/practica_final/dabd/db.sqlite3"
    cur = create_connection(database)
    with cur:
        add_cursos(cur,20)
        add_practica(cur,20)
        add_alumno(cur,20)
        #add_nota(cur,20)


if __name__ == '__main__':
    main()
