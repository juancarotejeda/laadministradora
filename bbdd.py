import pymysql.cursors
connection = pymysql.connect(host='sql3.freesqldatabase.com',
                             user='sql3737576',
                             password='crnvx7PylZ',
                             database='sql3737576')

def modificar_db(query):
    cursor= connection.cursor()  
    cursor.execute(query)     
    connection.commit()
    connection.close()
    return

def consultar_db(query):
    cursor= connection.cursor()
    cursor.execute(query)
    Result= cursor.fetchall() 
    return Result 