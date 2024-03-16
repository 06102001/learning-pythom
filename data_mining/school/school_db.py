'''
Dev: Camilo Mosquera
Scripts description: Configure SQLite3 database
'''

#Import engine database pack
import sqlite3

#Create a database connection (Database name)
con = sqlite3.connect('school.db')

#Creating cursor objet by conection => let us execute sql comands operations (Query)
cur = con.cursor()

#create user table
user_table = '''
    CREATE TABLE IF NOT EXISTS users (
        id INT NOT NULL,
        email VARCHAR NOT NULL,
        password VARCHAR NOT NULL,
        status BOOLEAN NULL,
        created_at DATETIME NOT NULL,
        updated_at DATETIME NOT NULL,
        deleted_at DATETIME NULL
    ); 
'''

#create students table
students_table = '''
    CREATE TABLE IF NOT EXISTS students (
        id INT NOT NULL,
        code VARCHAR NOT NULL,
        id_person INT NOT NULL,
        status BOOLEAN NULL,
        created_at DATETIME NOT NULL,
        updated_at DATETIME NOT NULL,
        deleted_at DATETIME NULL
    ); 
'''
#EXECUTE SQL (Query)
cur.execute(user_table)
cur.execute(students_table)

#Save changes database
con.commit()

#print(":::Database market has been create:::")