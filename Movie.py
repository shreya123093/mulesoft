import mysql.connector
mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="1239"
        )
mycursor=mydb.cursor()
mycursor.execute("SHOW DATABASES")
mycursor.execute("CREATE TABLE MOVIES(M_TITLE VARCHAR(40),LEAD_ACTOR VARCHAR(40),ACTRESS VARCHAR(40),MOV_YEAR INT(4),DIRECTOR_NAME VARCHAR(40)")
mycursor.execute("INSERT INTO MOVIES VALUES('BAHUBALI','PRABBAS','TAMANNA',2015,'RAJMOULI')")
mycursor.execute("INSERT INTO MOVIES VALUES('KGF','YASH','SRINIDHI',2018,'PRASHANTH')")
mycursor.execute("INSERT INTO MOVIES VALUES('SALUTE','DULQUER','DAINA',2020,'ROSHAN')")
mycursor.execute("SELECT * FROM MOVIES")
myresult=mycursor.fetchall()

for x in myresult:
    print(x)
