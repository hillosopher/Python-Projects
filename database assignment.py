## Version:    Python 3.11.1
##
## Author:     Josh Hill
##
## Purpose:    To complete the database assignment as a part of my Tech Academy curriculum


import sqlite3
    
    
# creates DB and columns
def createDb():
    conn = sqlite3.connect('databased.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS only_table ( \
                      id INTEGER PRIMARY KEY, \
                      item TEXT, \
                      UNIQUE(id, item) \
                  );"
                )
    conn.close()

# examines list of files and prints all .txt files to the console
def addPrintData():
    fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
                'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg', 'sup.txt')
    for f in fileList:
        conn = sqlite3.connect('databased.db')
        cur = conn.cursor()
        if f.endswith('txt'):
            with conn:
                cur.execute("""
                                INSERT OR REPLACE INTO only_table(item) VALUES(?)
                            """,(f, ))
            print(f)
        conn.close()

if __name__ == '__main__':
    createDb()
    addPrintData()


