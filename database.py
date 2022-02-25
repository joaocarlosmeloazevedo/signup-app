import sqlite3

conn = sqlite3.connect("employee.db")

c = conn.cursor()


def show_data():
    c.execute("SELECT * FROM employee")
    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()
    conn.close()

