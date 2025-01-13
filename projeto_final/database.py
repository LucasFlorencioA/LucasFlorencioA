import sqlite3

def inicializar_banco():
    
    conn = sqlite3.connect("industrias_wayne.db")
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        senha TEXT NOT NULL,
        role TEXT NOT NULL
    )''')

    cursor.execute('''
    INSERT OR IGNORE INTO usuarios (id, nome, senha, role)VALUES 
            (1, 'admin', 'Bmtn8795@', 'Administrador'),
            (2, 'alfred', '86912Ql/T*lo', 'Gerente'),
            (3,'grace', 'j9658@Jer8*', 'Funcionario')
            ''')
   
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resources (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        categoria TEXT NOT NULL,
        status TEXT NOT NULL
    )
    """)
    
    
    cursor.execute('''
    INSERT OR IGNORE INTO resources (id, nome, categoria, status) VALUES
        (1, 'Batmóvel', 'Veículo', 'Disponível'),
        (2, 'Cinto de Utilidades', 'Equipamento', 'Em Uso'),
        (3, 'Batcomputador', 'Tecnologia', 'Manutenção'),
        (4, 'Batwing', 'Veículo', 'Disponível'),
        (5, 'Batlança', 'Equipamento', 'Em Uso'),
        (6, 'Batmoto', 'Veículo', 'Disponível'),
        (7, 'Batdrone', 'Tecnologia', 'Disponível'),
        (8, 'Batcaverna', 'Instalação', 'Manutenção'),
        (9, 'Batcomunicador', 'Equipamento', 'Em Uso'),
        (10, 'Batcomputador Secundário', 'Tecnologia', 'Disponível'),
        (11, 'Batlancha', 'Veículo', 'Disponível'),
        (12, 'Batarangue', 'Equipamento', 'Em Uso'),
        (13, 'Batgrua', 'Equipamento', 'Manutenção'),
        (14, 'Batplane', 'Veículo', 'Em Uso'),
        (15, 'Batcomputador Tático', 'Tecnologia', 'Disponível')
    ''')

    conn.commit()
    conn.close()


if __name__ == "__main__":
    inicializar_banco()