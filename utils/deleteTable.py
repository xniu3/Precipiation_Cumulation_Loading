import sqlite3


def deleteTable():
    conn = sqlite3.connect('../db.sqlite3')
    c = conn.cursor()
    sql = '''
        DROP TABLE EMPLOYEE;
    '''
    c.execute(sql)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    deleteTable()