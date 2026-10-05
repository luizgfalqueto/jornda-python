# Jornada Python 🚀

Este repositório contém os projetos desenvolvidos durante a **Jornada Python**. Cada pasta representa um projeto prático que aborda um pilar fundamental da programação com Python: automação, análise de dados, inteligência artificial e desenvolvimento de aplicações web/dashboards.

Abaixo, apresentamos uma visão geral de cada um dos projetos.

---

## 📁 Projetos

### 1. Automação de Tarefas (`Aula1_automacao_tarefas`)
* **Descrição:** Script de automação robótica de processos (RPA) para simular a interação humana com o sistema operacional e navegador. O programa abre o navegador Google Chrome, faz login em um sistema de treinamento e realiza o cadastro automatizado de produtos a partir de uma base de dados local (`produtos.csv`).
* **Tecnologias:** `pyautogui`, `pandas`, `time`.
* **Como executar:** `python codigo.py`

### 2. Análise de Dados e Insights (`Aula2_analise_dados`)
* **Descrição:** Projeto de análise exploratória e tratamento de dados voltado para a redução do índice de cancelamento de clientes (Churn Rate). A partir de uma base de dados com mais de 800 mil registros, o notebook analisa os principais motivos que levam os clientes a cancelarem os serviços e propõe insights acionáveis para solucionar o problema.
* **Tecnologias:** `pandas`, `plotly`, `openpyxl`, Jupyter Notebook.
* **Como executar:** Abra o arquivo `inicial.ipynb` no VS Code ou Jupyter Environment e execute as células.

### 3. Chatbot com Inteligência Artificial (`Aula3_chatbot_ai`)
* **Descrição:** Uma aplicação web de chat interativo integrada com inteligência artificial. O chatbot consome o modelo `gemini-flash-lite-latest` via interface compatível da OpenAI e possui gerenciamento de estado de sessão (`st.session_state`) para manter o histórico da conversa entre o usuário e a IA.
* **Tecnologias:** `streamlit`, `openai` (configurado para a API Gemini).
* **Como executar:** `streamlit run codigo.py`

### 4. Sistema de Vendas e Dashboard (`Aula4_sistema_vendas`)
* **Descrição:** Aplicação web interativa para controle financeiro e de vendas. O sistema conta com uma barra lateral para cadastrar novas vendas diretamente em uma tabela local (`vendas.csv`) e exibe, em tempo real, o faturamento total da empresa e gráficos interativos detalhando o desempenho de vendas por vendedor e por tipo de produto.
* **Tecnologias:** `streamlit`, `pandas`, `plotly`.
* **Como executar:** `streamlit run main.py`

---

## 🛠️ Como executar os projetos localmente

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/jornada_python.git
   cd jornada_python
   ```

2. **Instale as dependências gerais:**
   Cada pasta de projeto possui suas respectivas bibliotecas. Você pode instalar os requisitos principais usando:
   ```bash
   pip install pandas pyautogui plotly streamlit openai openpyxl
   ```
