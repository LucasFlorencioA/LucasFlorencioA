# Documentação do Sistema de Gestão das Indústrias Wayne

Bem-vindo à documentação do sistema de gestão desenvolvido para as Indústrias Wayne. Este guia detalha como instalar, configurar e usar o sistema, bem como as permissões atribuídas aos diferentes tipos de usuários.

---

## **1. Instalação**

### **1.1. Requisitos**

Certifique-se de que o ambiente atenda aos seguintes requisitos:
- Python 3.9 ou superior.
- Gerenciador de pacotes `pip`.
- SQLite3 (integrado ao Python).
- Dependências especificadas no arquivo `requirements.txt`.

### **1.2. Etapas de Instalação**

1. Clone este repositório para sua máquina local:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate # No Windows: .venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o sistema:
   ```bash
   streamlit run app.py
   ```

---

## **2. Configuração do Banco de Dados**

O sistema utiliza SQLite como banco de dados. Siga os passos abaixo para configurar:

1. **Inicialização do banco de dados:**
   O arquivo `industrias_wayne.db` será gerado automaticamente ao executar o sistema pela primeira vez.

2. **Estrutura do banco de dados:**
   O banco contém as seguintes tabelas principais:
   - **usuarios:** Armazena informações dos usuários (nome, senha e função).
   - **resources:** Armazena os recursos cadastrados (ID, nome, categoria e status).

3. **Adicionar usuários iniciais:**
   Execute o seguinte comando no Python para adicionar um usuário administrador:
   ```python
   import sqlite3

   conn = sqlite3.connect("industrias_wayne.db")
   cursor = conn.cursor()

   cursor.execute("INSERT INTO usuarios (nome, senha, role) VALUES (?, ?, ?)", ("admin", "admin123", "Administrador"))
   conn.commit()
   conn.close()
   ```

---

## **3. Uso Básico**

### **3.1. Login**

1. Ao abrir o sistema, será exibida uma tela de login.
2. Insira o nome de usuário e a senha para acessar as funcionalidades.

### **3.2. Painel de Administração**

Usuários com função de **Administrador** ou **Gerente** podem:
- Adicionar recursos com nome, categoria e status.
- Atualizar o status de recursos existentes.
- Remover recursos.

### **3.3. Dashboard de Visualização**

Disponível para todos os usuários. Exibe:
- Métricas sobre os recursos cadastrados.
- Gráficos interativos para análise de categorias e status.
- Recursos recentemente adicionados.

### **3.4. Logout**

Para sair do sistema, selecione a opção **Sair** no menu lateral.

---

## **4. Permissões**

| Função           | Permissão                                                         |
|-------------------|-----------------------------------------------------------------|
| **Administrador** | Gerenciar recursos, visualizar dashboard e acessar todas as áreas. |
| **Gerente**       | Gerenciar recursos e visualizar dashboard.                     |
| **Usuário**       | Apenas visualizar o dashboard.                                 |

---

## **5. Personalização**

Caso deseje personalizar o sistema:
- **Configurar novos gráficos:** Ajuste o código no arquivo `app.py`.
- **Adicionar funcionalidades:** Utilize as classes existentes como base.
- **Temas:** Consulte a documentação do Streamlit para criar temas personalizados.

---

Caso tenha dúvidas ou precise de suporte, entre em contato com o desenvolvedor.

