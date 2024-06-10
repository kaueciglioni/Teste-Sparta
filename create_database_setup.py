import sqlite3

def create_database():
    try:
        conexaodb = sqlite3.connect('companhias.db')
        cursor = conexaodb.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS companhia (
            id INTEGER PRIMARY KEY,
            cnpj_cia TEXT,
            denom_social TEXT,
            sit TEXT,
            data TEXT
        )
        ''')

        conexaodb.commit()
        conexaodb.close()

        print("Banco de dados criado com sucesso.")
    except Exception as e:
        print("Erro ao criar banco de dados:", e)

if __name__ == "__main__":
    create_database()
