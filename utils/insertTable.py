import sqlite3


def insertTable():
    conn = sqlite3.connect('../db.sqlite3')
    c = conn.cursor()

    c.execute("INSERT INTO EMPLOYEE (ID, FIRST_NAME, LAST_NAME, EMAIL) \
          VALUES (1, 'Century Park', 'TC', '1952066849@qq.com' )")

    c.execute("INSERT INTO EMPLOYEE (ID, FIRST_NAME, LAST_NAME, EMAIL) \
          VALUES (2, 'Southgate', 'TC', '2739887824@qq.com' )")

    c.execute("INSERT INTO EMPLOYEE (ID, FIRST_NAME, LAST_NAME, EMAIL) \
          VALUES (3, 'South Campus', 'TC', '3463368802@qq.com' )")

    c.execute("INSERT INTO EMPLOYEE (ID, FIRST_NAME, LAST_NAME, EMAIL) \
          VALUES (4, 'Mckernan Belgravia', 'TC', '1961018099@qq.com' )")
    conn.commit()
    conn.close()


if __name__ == '__main__':
    insertTable()