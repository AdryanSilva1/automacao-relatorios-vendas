````markdown
# Sistema de Automação de Relatórios de Vendas em Python

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![Automation](https://img.shields.io/badge/Automation-Yes-orange)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)

Automatize relatórios financeiros com Python!  
Este sistema lê dados de vendas em CSV, gera análises inteligentes e envia relatórios automáticos por e-mail — ideal para **pequenas empresas**, **analistas de dados** e **autônomos** que desejam otimizar tarefas repetitivas.

---

## Começando Rapidamente

### Pré-requisitos
- Python **3.8+**
- Pip (gerenciador de pacotes do Python)

---

### ⚡ Instalação Rápida

```bash
# 1. Crie a estrutura de pastas
mkdir projeto_relatorios
cd projeto_relatorios
mkdir data

# 2. Crie os arquivos do projeto (copie os códigos abaixo)
# - main.py
# - report_utils.py  
# - email_utils.py
# - requirements.txt
# - data/vendas.csv

# 3. Instale as dependências
pip install pandas python-dotenv

# 4. Execute o sistema
python main.py
````

---

## Configuração do E-mail (Opcional)

Para enviar relatórios automáticos por e-mail, configure as credenciais do seu ambiente:

**Linux/Mac:**

```bash
export EMAIL_USER="seu_email@gmail.com"
export EMAIL_PASSWORD="sua_senha_de_app"
```

**Windows (PowerShell):**

```powershell
$env:EMAIL_USER="seu_email@gmail.com"
$env:EMAIL_PASSWORD="sua_senha_de_app"
```

> **Importante:** Para Gmail, use uma [Senha de App](https://support.google.com/accounts/answer/185833) em vez da senha normal por questões de segurança.

---

## Como Usar

```bash
# Exibir relatório no terminal
python main.py

# Enviar relatório simples por e-mail
python main.py --email destinatario@empresa.com

# Enviar relatório detalhado por e-mail
python main.py --email destinatario@empresa.com --tipo detalhado
```

---

## Exemplo de Saída

```
RELATÓRIO DE VENDAS - 15/01/2024

RESUMO FINANCEIRO:
   • Total vendido: R$ 8.501,00
   • Ticket médio: R$ 944,56
   • Maior venda: R$ 3.500,00
   • Menor venda: R$ 180,00

ESTATÍSTICAS:
   • Quantidade de vendas: 9
   • Clientes únicos: 9
   • Data mais recente: 19/01/2024
```

---

## Estrutura do Projeto

```
projeto_relatorios/
├── data/
│   └── vendas.csv          # Dados de vendas
├── main.py                 # Script principal
├── report_utils.py         # Análise e geração de relatórios
├── email_utils.py          # Envio de e-mails automáticos
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação completa
```

---

## Tecnologias Utilizadas

* **Python 3.8+**
* **Pandas** → Análise de dados
* **smtplib / email.message** → Envio automatizado de e-mails
* **dotenv** → Gestão de credenciais com variáveis de ambiente

---

## Próximas Melhorias

* [ ] Agendamento automático (cron jobs)
* [ ] Geração de relatórios em PDF
* [ ] Integração com banco de dados SQL
* [ ] Dashboard web interativo
* [ ] Análises preditivas com Machine Learning

---

## Arquivo `requirements.txt`

```txt
pandas>=1.5.0
python-dotenv>=0.19.0
```

---

##  Autor

Criado com 💻 e ☕ por **Adryan Silva**
📫 Contato: 🔗 [linkedin.com/in/adryan-silva-santos](https://linkedin.com/in/adryan-silva-santos)
🔗 Em breve: portfólio profissional

---

**Se este projeto te ajudou, deixe uma estrela no repositório!**

``````
