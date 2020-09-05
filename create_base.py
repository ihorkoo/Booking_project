import sqlite3

sql_text = """

create table client_status
    (
    id INREGER PRIMARY KEY,
    status_name TEXT NOT NULL,
    order_with_call INTEGER NOT NULL)

    ;
    
create table client
    (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    telegram_id INTEGER NOT NULL,
    status_id INTEGER NOT NULL,
    FOREIGN KEY (status_id)
        REFERENCES client_status (id))
"""

if __name__ == '__main__':
    conn = sqlite3.connect("base.sqlite3")
    c = conn.cursor()
    c.executescript(sql_text)
