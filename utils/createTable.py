import sqlite3
def createTable():
    conn = sqlite3.connect('../db.sqlite3')
    c = conn.cursor()
    sql = '''
        CREATE TABLE EMPLOYEE(
            ID INT PRIMARY KEY NOT NULL,
            FIRST_NAME CHAR(20) NOT NULL,
            LAST_NAME CHAR(20),
            EMAIL VARCHAR(50) NOT NULL
        )
    '''
    c.execute(sql)
    conn.commit()
    conn.close()
if __name__ == '__main__':
    createTable()