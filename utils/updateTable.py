import sqlite3
def updateTable():
    conn = sqlite3.connect('../db.sqlite3')
    c = conn.cursor()
    c.execute("UPDATE EMPLOYEE set FIRST_NAME = 'University' where ID=4")
    conn.commit()
    conn.close()
if __name__ == '__main__':
    updateTable()