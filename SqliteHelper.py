import sqlite3

class SqliteHelper:

    def __init__(self,name=None):
        self.conn = None
        self.cursor = None

        if name:
            self.open(name)

    def open(self, name):
        try:
            self.conn = sqlite3.connect(name)
            self.cursor = self.conn.cursor()
            print(sqlite3.version)
        except sqlite3.Error as e:
            print("Failed connecting to database...")

    def create_table(self):
        c = self.cursor
        c.execute("""CREATE TABLE users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    year INTEGER,
                    admin INTEGER
                )""")
    def edit(self,query):#INSERT & UPDATE
        c = self.cursor
        c.execute(query)
        self.conn.commit()

    def select(self,query):#SELECT
        c = self.cursor
        c.execute(query)
        return c.fetchall()
        

test = SqliteHelper("test.db")
#test.create_table()

#test.edit("INSERT INTO users (name,year,admin) VALUES ('john',1992,0) ")
test.edit("UPDATE users SET name='jack' WHERE name = 'john'")
print(test.select("SELECT * FROM users"))
