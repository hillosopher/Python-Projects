
import tkinter as tk
import sqlite3


# Create db or connect to the one that exists

def addStudent(first_name, last_name, phone_num, email_add, cur_course):
    # create / connect to database
    conn = sqlite3.connect('student_tracking.db')
    cur = conn.cursor()

    # create table if it doesn't exist
    with conn:
        cur.execute("""CREATE TABLE IF NOT EXISTS student_info(
        first_name TEXT,
        last_name TEXT,
        phone_number INTEGER,
        email_address TEXT,
        current_course TEXT
                ) """)

    #add student 
        cur.execute("INSERT INTO student_info VALUES (?, ?, ?, ?, ?)",
                    (first_name, last_name, phone_num, email_add, cur_course))


    # Commit changes and close
        conn.commit()
    conn.close()

    

#def removeStudent():
# use fetchall to pull results from query


if __name__ == '__main__':
    pass

