import sqlite3 as db
from datetime import date, datetime

def init():
    connection = db.connect("spent.db")
    cursor = connection.cursor()
    sql = '''
    create table if not exists expenses (
        amount number,
        category string,
        message string,
        date string
    )
    '''
    cursor.execute(sql)
    connection.commit()

def log(amount, category, message="", date=str(datetime.now())):
    if message == None:
        message = ''
    if date == None:
        date = str(datetime.now())
    connection = db.connect("spent.db")
    cursor = connection.cursor()
    sql = '''
    insert into expenses values (
        {},
        '{}',
        '{}',
        '{}'
    )
    '''.format(amount, category, message, date)
    cursor.execute(sql)
    connection.commit()



def view(category=None):
    connection = db.connect("spent.db")
    cursor = connection.cursor()
    if category:
        sql = '''
        select * from expenses where category = '{}'
        '''.format(category)
        sql2 = '''
        select sum(amount) from expenses where category = '{}'
        '''.format(category)
    else:
        sql = '''
        select * from expenses
        '''
        sql2 = '''
        select sum(amount) from expenses
        '''
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.execute(sql2)
    total = cursor.fetchone()[0]

    return total, results
