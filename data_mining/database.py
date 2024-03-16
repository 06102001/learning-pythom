'''
Dev: Camilo Mosquera
Scripts description: Configure SQLite3 database
'''

#Import engine database pack
import sqlite3

#Create a database connection (Database name)
con = sqlite3.connect('market.db')

#Creating cursor objet by conection => let us execute sql comands operations (Query)
cur = con.cursor()

#create user table
user_table = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        firstname TEXT NOT NULL,
        lastname TEXT NOT NULL,
        ident_number TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    ); 
'''
#EXECUTE SQL (Query)
cur.execute(user_table)

#Save changes database
con.commit()

#print(":::Database market has been create:::")

