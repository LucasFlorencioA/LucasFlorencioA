import sqlite3
import streamlit as st
import pandas as pd
import plotly.express as px

def login():
    st.title("Bem-vindo ao Sistema de Gestão das Indústrias Wayne.") 
    st.subheader("Conecte-se")
    username = st.text_input("Nome de usuário")
    password = st.text_input("Senha", type="password")

    if st.button("Conecte-se"):
        user = autenticacao(username, password)
        if user:
            st.success(f"Bem vindo {username}, Função: {user[0]}")
            st.session_state.logged_in = True
            st.session_state.user_role = user[0]
            main() 
          
        else:
            st.error("Nome de usuário ou senha inválidos")

def main():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.user_role = None

    if not st.session_state.logged_in:
        login()
    else:
        st.sidebar.title("Menu")
        menu_options = ["Login", "Gerenciar Recursos", "Dashboard de Visualização", "Sair"]
        escolha = st.sidebar.radio("Navegação", menu_options)

        if escolha == "Dashboard de Visualização":
            carregar_painel()
        elif escolha == "Gerenciar Recursos" and st.session_state.user_role in ["Administrador", "Gerente"]:
            admin_painel()
        
        elif escolha == "Gerenciar Recursos" and st.session_state.user_role in ["Funcionario"]:
            st.info("Desculpe, mas você não tem acesso ao Gerenciador de recursos")
            
        elif escolha == "Sair":
            st.session_state.logged_in = False
            st.session_state.user_role = None
            st.session_state.updated = False
            st.success("Você selecionou sair! Redirecionando para a tela de login...")
            

def autenticacao(nome, senha):
    conn = sqlite3.connect("industrias_wayne.db")
    cursor = conn.cursor()
    cursor.execute("SELECT role FROM usuarios WHERE nome = ? AND senha = ?", (nome, senha))
    user = cursor.fetchone()
    conn.close()
    return user

class Gerenciador_de_recursos:
    def __init__(self):
        self.conn = sqlite3.connect("industrias_wayne.db")

    def add_recursos(self, name, category, status):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO resources (nome, categoria, status) VALUES (?, ?, ?)",
            (name, category, status),
        )
        self.conn.commit()
    
    def list_recursos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM resources")
        return cursor.fetchall()
    
    def remove_recurso(self, recurso_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM resources WHERE id = ?", (recurso_id,))
        self.conn.commit()

    def update_status(self, recurso_id, novo_status):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE resources SET status = ? WHERE id = ?",
            (novo_status, recurso_id),
        )
        self.conn.commit()
        

def carregar_painel():
    st.title("Dashboard de Visualização")
    st.subheader("Resumo dos Recursos")

   
    resource_manager = Gerenciador_de_recursos()
    resources = resource_manager.list_recursos()

    if resources:
     
        df = pd.DataFrame(resources, columns=["ID", "Nome", "Categoria", "Status"])

     
        st.metric("Total de Recursos", len(df))
        st.metric("Categorias Únicas", df["Categoria"].nunique())
        st.metric("Status Únicos", df["Status"].nunique())


        category_chart = px.bar(
            df.groupby("Categoria").size().reset_index(name="Quantidade"),
            x="Categoria",
            y="Quantidade",
            title="Distribuição por Categoria"
        )
        st.plotly_chart(category_chart)


        status_chart = px.pie(
            df,
            names="Status",
            title="Distribuição por Status"
        )
        st.plotly_chart(status_chart)


        st.subheader("Recursos Recentemente Adicionados")
        st.dataframe(df.tail(5))

    else:
        st.warning("Nenhum recurso disponível para exibição no momento.")


def admin_painel():
    st.header("Painel do Administrador")
    resource_manager = Gerenciador_de_recursos()

    # Adicionar recurso
    st.subheader("Gerenciar Recursos")
    with st.form("Adicionar Recurso"):
        name = st.text_input("Nome do Recurso")
        category = st.text_input("Categoria")
        status = st.selectbox("Status", ["Disponível", "Em Uso", "Manutenção"])
        submit = st.form_submit_button("Adicionar")
        if submit:
            resource_manager.add_recursos(name, category, status)
            st.success("Recurso adicionado com sucesso!")
            st.session_state.updated = True 

    # Lista de recursos
    if "updated" not in st.session_state:
        st.session_state.updated = False

    resources = resource_manager.list_recursos()
    if st.session_state.updated:
        resources = resource_manager.list_recursos()  
        st.session_state.updated = False  


    df = pd.DataFrame(columns=["ID", "Nome", "Categoria", "Status"])
    if resources:
        df = pd.DataFrame(resources, columns=["ID", "Nome", "Categoria", "Status"])
        st.dataframe(df)
    else:
        st.info("Nenhum recurso cadastrado.")


    st.subheader("Atualizar Status do Recurso")
    recurso_id = st.number_input("ID do Recurso", min_value=1, step=1, key="update_recurso_id")
    novo_status = st.selectbox("Novo Status", ["Disponível", "Em Uso", "Manutenção"], key="update_novo_status")
    if st.button("Atualizar Status", key="update_status_button"):
        if not df.empty and recurso_id in df["ID"].values:
            resource_manager.update_status(recurso_id, novo_status)
            st.success(f"Status do recurso com ID {recurso_id} atualizado para '{novo_status}'!")
            st.session_state.updated = True  # Marca que houve atualização
        else:
            st.error("ID não encontrado na lista de recursos.")


    st.subheader("Remover Recurso")
    recurso_id_remover = st.number_input("ID do Recurso a Remover", min_value=1, step=1, key="remove_recurso_id")
    if st.button("Remove", key="remove_button"):
        if not df.empty and recurso_id_remover in df["ID"].values:
            resource_manager.remove_recurso(recurso_id_remover)
            st.success(f"Recurso com ID {recurso_id_remover} removido com sucesso!")
            st.session_state.updated = True  # Marca que houve atualização
        else:
            st.error("ID não encontrado na lista de recursos.")


if __name__ == "__main__":
    main()