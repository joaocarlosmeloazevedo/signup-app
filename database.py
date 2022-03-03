import sqlite3

conn = sqlite3.connect("people.db")
c = conn.cursor()

def create_table():
    c.execute("""CREATE TABLE person(
        first_name text,
        last_name text,
        email text,
        age integer,
        salary real
    )
    """)

    conn.commit()


def insert_data():
    manyperson = [
        ('Wesley', 'Saladao', 'wesleysaladao@brasil.com', 24, 3500.5),
    ]

    c.executemany("INSERT INTO person VALUES(?,?,?,?,?)", manyperson)

    conn.commit()


def show_data():
    c.execute("SELECT * FROM person")
    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()
    conn.close()





