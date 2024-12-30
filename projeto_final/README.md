# Documentação do Sistema de Gestão das Indústrias Wayne

Bem-vindo à documentação do sistema de gestão desenvolvido para as Indústrias Wayne. Este guia detalha o processo de instalação, configuração e uso do sistema, além das permissões atribuídas aos diferentes tipos de usuários.

---

## **1. Visão Geral do Sistema**

O sistema de gestão das Indústrias Wayne foi projetado para facilitar o gerenciamento de recursos e usuários. Principais funcionalidades:

- Gerenciamento de recursos, como máquinas, equipamentos e ferramentas.
- Controle de permissões baseado em funções de usuários (Administrador, Gerente e Funcionário).
- Visualização de dados interativos por meio de dashboards.
- Sistema seguro de login.

---

## **2. Instalação**

### **2.1. Requisitos**

Certifique-se de que o ambiente atenda aos seguintes requisitos:
- Python 3.9 ou superior.
- Gerenciador de pacotes `pip`.
- SQLite3 (integrado ao Python).
- Dependências especificadas no arquivo `requirements.txt`.

### **2.2. Etapas de Instalação**

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

## **3. Configuração do Banco de Dados**

O sistema utiliza SQLite como banco de dados. Siga os passos abaixo para configurar:

1. **Inicialização do banco de dados:**
   O banco de dados `industrias_wayne.db` já foi previamente criado, portanto, não é necessário executá-lo pela primeira vez para gerar o arquivo.

2. **Estrutura do banco de dados:**
   O banco contém as seguintes tabelas principais:
   - **usuarios:** Armazena informações dos usuários (nome, senha e função).
   - **resources:** Armazena os recursos cadastrados (ID, nome, categoria e status).

3. **Adicionar usuários iniciais:**
   Para adicionar um usuário administrador, execute o seguinte código no Python:
   ```python
   import sqlite3

   conn = sqlite3.connect("industrias_wayne.db")
   cursor = conn.cursor()

   cursor.execute("INSERT INTO usuarios (nome, senha, role) VALUES (?, ?, ?)", ("admin", "admin123", "Administrador"))
   conn.commit()
   conn.close()
   ```

---

## **4. Uso do Sistema**

### **4.1. Login**

1. Ao abrir o sistema, será exibida uma tela de login.
2. Insira o nome de usuário e a senha para acessar as funcionalidades.

### **4.2. Painel de Administração**

Usuários com função de **Administrador** ou **Gerente** podem:

- Adicionar recursos com nome, categoria e status.
- Atualizar o status de recursos existentes.
- Remover recursos.
- Visualizar todas as informações sobre os recursos.

### **4.3. Painel do Funcionário**

Disponível para usuários com função de **Funcionário**, permite:

- Visualizar recursos cadastrados, incluindo categoria e status.
- Consultar recursos disponíveis para uso.

### **4.4. Dashboard Interativo**

- Exibe gráficos e métricas relacionadas aos recursos.
- Permite uma análise rápida e eficaz do status e da distribuição dos recursos.

### **4.5. Logout**

Para sair do sistema, selecione a opção **Sair** no menu lateral. Caso o logout automático não ocorra, clique na opção **Conecte-se** ou atualize a página para retornar à tela inicial.

---

## **5. Permissões de Usuários**

| Função           | Permissão                                                         |
|-------------------|-----------------------------------------------------------------|
| **Administrador** | Gerenciar recursos, visualizar dashboard e acessar todas as áreas. |
| **Gerente**       | Gerenciar recursos e visualizar dashboard.                     |
| **Funcionário**   | Apenas visualizar o dashboard e consultar recursos.            |

---

## **6. Personalização e Extensão**

Para personalizar o sistema:

1. **Configurar novos gráficos:**
   Ajuste o código no arquivo `app.py` para incluir novos gráficos interativos.

2. **Adicionar funcionalidades:**
   Utilize as classes existentes como base para implementar novos módulos.

3. **Temas:**
   Consulte a documentação do Streamlit para criar temas personalizados.

4. **Integrações:**
   Adicione integrações com APIs externas ou sistemas corporativos, se necessário.

---

## **7. Suporte**

Caso tenha dúvidas ou precise de suporte, entre em contato com o desenvolvedor ou abra uma issue no repositório oficial do projeto.

