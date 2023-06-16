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
nome1 = "ronaldinho"
cpf1 = '85947632546'
telefone1 = '36974173915'
media = 8
fk_turma = 2
meucursor = banco.cursor()
sql = "insert into alunos(nome, cpf, telefone, media, fk_turma) values(%s, %s, %s, %s, %s)"
data = (nome1, cpf1, telefone1, media, fk_turma)
meucursor.execute(sql, data)
banco.commit()
userid = meucursor.lastrowid
print(userid)
meucursor.close()
banco.close()
