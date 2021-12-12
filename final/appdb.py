import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    database = 'borrow',
    user = 'root',
    password = ''
)

mycursor = mydb.cursor(dictionary=True)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS user(
        ID INT NOT NULL AUTO_INCREMENT,
        student_name VARCHAR(225),
        student_id VARCHAR(225),
        book_name VARCHAR(225),
        edition VARCHAR(10),
        author VARCHAR(255),
        date1 date,
        PRIMARY KEY(ID)
    )
    """
)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS attendant(
      username VARCHAR(100),
      password VARCHAR(100)
    )"""
)

