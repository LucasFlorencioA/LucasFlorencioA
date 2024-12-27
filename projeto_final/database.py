import sqlite3

def inicializar_banco():
    
    conn = sqlite3.connect("industrias_wayne.db")
    cursor = conn.cursor()
    # Criação da tabela de usuários
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT UNIQUE NOT NULL,
        senha TEXT NOT NULL,
        role TEXT NOT NULL
    )
    """)

    # Criação da tabela de recursos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resources (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        categoria TEXT NOT NULL,
        status TEXT NOT NULL
    )
    """)

    # Inserção de um administrador padrão
    cursor.execute("""
    INSERT OR IGNORE INTO usuarios (nome, senha, role) 
    VALUES ('admin', '1234', 'Administrador')
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    inicializar_banco()