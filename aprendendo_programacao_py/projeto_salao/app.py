import sqlite3
import streamlit as st


def connect_db():
    return sqlite3.connect("salon.db")

def criar_tabela_agendamentos():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS agendamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_nome TEXT NOT NULL,
            cliente_telefone TEXT NOT NULL,
            servico TEXT NOT NULL,
            data_agendamento TEXT NOT NULL,
            hora_agendamento TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def obter_horarios_disponiveis(data_agendamento):
    horarios = ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00']
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT hora_agendamento FROM agendamentos WHERE data_agendamento = ?', (data_agendamento,))
    agendamentos = cursor.fetchall()
    conn.close()
    horarios_ocupados = [agendamento[0] for agendamento in agendamentos]
    return [horario for horario in horarios if horario not in horarios_ocupados]


def listar_agendamentos():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM agendamentos')
    agendamentos = cursor.fetchall()
    conn.close()
    return agendamentos


def adicionar_agendamento(cliente_nome, cliente_telefone, servico, data_agendamento, hora_agendamento):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO agendamentos (cliente_nome, cliente_telefone, servico, data_agendamento, hora_agendamento)
        VALUES (?, ?, ?, ?, ?)
    ''', (cliente_nome, cliente_telefone, servico, data_agendamento, hora_agendamento))
    conn.commit()
    conn.close()


criar_tabela_agendamentos()


st.title("Agendamento de Salão de Beleza")


with st.form("form_agendamento"):
    st.header("Agende seu horário")
    cliente_nome = st.text_input("Nome do Cliente", key="cliente_nome")
    cliente_telefone = st.text_input("Telefone", key="cliente_telefone")
    servico = st.selectbox("Serviço", ["Corte", "Penteado", "Coloração", "Tratamento"], key="servico")
    data_agendamento = st.date_input("Data do Agendamento", key="data_agendamento")
    horarios_disponiveis = obter_horarios_disponiveis(str(data_agendamento))
    hora_agendamento = st.selectbox("Horário", horarios_disponiveis, key="hora_agendamento")
    submit_button = st.form_submit_button("Agendar")

    if submit_button:
        if cliente_nome and cliente_telefone and servico and hora_agendamento:
            adicionar_agendamento(cliente_nome, cliente_telefone, servico, str(data_agendamento), hora_agendamento)
            st.success("Agendamento realizado com sucesso!")
        else:
            st.error("Preencha todos os campos!")


st.header("Agendamentos Realizados")
agendamentos = listar_agendamentos()
for agendamento in agendamentos:
    st.write(f"**Cliente:** {agendamento[1]} - **Serviço:** {agendamento[3]} - **Data:** {agendamento[4]} - **Hora:** {agendamento[5]}")
