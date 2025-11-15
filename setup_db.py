import sqlite3

conn = sqlite3.connect("denuncias.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS denuncias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_ocorrencia TEXT,
    data_acontecimento TEXT,
    setor_acontecimento TEXT,
    relato TEXT
)
""")

conn.commit()
conn.close()

print("Banco e tabela criados com sucesso.")