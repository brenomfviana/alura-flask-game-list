import mysql.connector
from flask_bcrypt import generate_password_hash
from mysql.connector import errorcode

print("Conectando...")
try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="#Admin123",
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Existe algo errado no nome de usuário ou senha")
    else:
        print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `jogoteca`;")

cursor.execute("CREATE DATABASE `jogoteca`;")

cursor.execute("USE `jogoteca`;")

# criando tabelas
TABLES = {}
TABLES[
    "Game"
] = """
      CREATE TABLE `game` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `name` varchar(50) NOT NULL,
      `category` varchar(40) NOT NULL,
      `platform` varchar(20) NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;"""

TABLES[
    "User"
] = """
      CREATE TABLE `user` (
      `name` varchar(20) NOT NULL,
      `nickname` varchar(8) NOT NULL,
      `password` varchar(100) NOT NULL,
      PRIMARY KEY (`nickname`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;"""

for table in TABLES:
    table_sql = TABLES[table]
    try:
        print("Criando tabela {}:".format(table), end=" ")
        cursor.execute(table_sql)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Já existe")
        else:
            print(err.msg)
    else:
        print("OK")


# inserindo usuarios
user_sql = "INSERT INTO user (name, nickname, password) VALUES (%s, %s, %s)"
users = [
    (
        "Admin",
        "admin",
        generate_password_hash("admin").decode("utf-8"),
    ),
    (
        "Bruno Divino",
        "BD",
        generate_password_hash("alohomora").decode("utf-8"),
    ),
    (
        "Camila Ferreira",
        "Mila",
        generate_password_hash("paozinho").decode("utf-8"),
    ),
    (
        "Guilherme Louro",
        "Cake",
        generate_password_hash("python_eh_vida").decode("utf-8"),
    ),
]
cursor.executemany(user_sql, users)

cursor.execute("select * from jogoteca.user")
print(" -------------  Usuários:  -------------")
for user in cursor.fetchall():
    print(user[1])

# inserindo jogos
games_sql = "INSERT INTO game (name, category, platform) VALUES (%s, %s, %s)"
games = [
    ("Tetris", "Puzzle", "Atari"),
    ("God of War", "Hack n Slash", "PS2"),
    ("Mortal Kombat", "Luta", "PS2"),
    ("Valorant", "FPS", "PC"),
    ("Crash Bandicoot", "Hack n Slash", "PS2"),
    ("Need for Speed", "Corrida", "PS2"),
]
cursor.executemany(games_sql, games)

cursor.execute("select * from jogoteca.game")
print(" -------------  Jogos:  -------------")
for game in cursor.fetchall():
    print(game[1])

# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()
