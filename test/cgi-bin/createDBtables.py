import sqlite3

#Step 1 : connect
connection = sqlite3.connect('coachdata.sqlite')

#Step 2 : establish a cursor
cursor = connection.cursor()


#Step 3 : interactive
cursor.execute("""CREATE TABLE athletes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    name TEXT NOT NULL,
                    dob DATE NOT NULL )""")
cursor.execute("""CREATE TABLE timing_data (
                    athlete_id INTEGER NOT NULL,
                    value TEXT NOT NULL,
                    FOREIGN KEY (athlete_id) REFERENCES athletes)""")


#Step 4 : commit/abort
connection.commit()
#Step 5 : close
connection.close()