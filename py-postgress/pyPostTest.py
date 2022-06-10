import psycopg2


hostname= 'localhost'
database = 'testPyPostgres'
username = 'root'
pwd = 'root'
port_id= 5432
conn = None
cur =None

try:
    
    conn = psycopg2.connect(
            host =hostname,
            dbname= database,
            user=username,
            password= pwd,
            port =port_id 
        )
    cur= conn.cursor()
    
    cur.execute('DROP TABLE IF EXISTS employee')
    create_script = ''' CREATE TABLE IF NOT EXISTS employee (
                            id      int PRIMARY KEY,
                            name    varchar(40) NOT NULL,
                            salary  int,
                            dept_id varchar(30)) '''
    cur.execute(create_script)
    
    insert_script = 'INSERT INTO employee (id,name,salary,dept_id) VALUES (%s,%s,%s,%s)'
    insert_value = [(1,'James',1200, 'D1'),(2,'David',1222, 'D2'),(3,'Peter',900, 'D3'),(4,'Jhon',100, 'D4')]
    for record in insert_value:
        cur.execute(insert_script,record)
    
    update_script = 'UPDATE employee SET salary = salary + (salary * 0.5)'
    cur.execute(update_script)
    
    delete_script = 'DELETE FROM employee WHERE name = %s'
    delete_record =('James',)
    cur.execute(delete_script,delete_record)
    
    cur.execute('SELECT * FROM EMPLOYEE')
    for record in cur.fetchall():
        print(record[0],record[1])
    
    
    conn.commit()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
        

