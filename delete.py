import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="cdd2023",
    database="escolaturmab"
)
print(banco)

meucursor = banco.cursor()
pesquisa = 'select * from alunos;'
meucursor.execute(pesquisa)
resultado = meucursor.fetchall()
for x in resultado:
    print(x)

cursor = banco.cursor()
sql = "delete from alunos where matricula = 4;"
cursor.execute(sql)
banco.commit()
userid = meucursor.lastrowid
print(userid)
cursor.close()
banco.close()
