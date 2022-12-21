import sqlite3


def selectTable():
    conn = sqlite3.connect('../db.sqlite3')
    c = conn.cursor()
    cursor = c.execute("SELECT ID, FIRST_NAME, LAST_NAME, EMAIL  from EMPLOYEE")
    for row in cursor:
        print("ID = ", row[0])
        print("FIRST_NAME = ", row[1])
        print("LAST_NAME = ", row[2])
        print("EMAIL = ", row[3], "\n")
    conn.commit()
    conn.close()


if __name__ == '__main__':
    selectTable()