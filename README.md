# Gerador de Estrutura de Projetos (Scaffold Generator)

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![YAML](https://img.shields.io/badge/Config-YAML-lightgrey.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

Um gerador de linha de comando robusto e flexível para criar rapidamente estruturas de diretórios e arquivos padronizadas para diferentes tipos de projetos. Ele utiliza arquivos de configuração YAML para permitir a criação de projetos "esqueleto" com conteúdo inicial, acelerando o início de novos desenvolvimentos.

## 🚀 Funcionalidades

* **Geração Rápida:** Crie a estrutura completa de um novo projeto em segundos.
* **Templates Reutilizáveis:** Defina modelos para diversos tipos de projetos (Python, HTML/CSS/JS, Node.js).
* **Configuração via YAML:** Adicione novos templates ou modifique os existentes de forma declarativa, sem alterar o código principal.
* **Variáveis Dinâmicas:** Preencha arquivos de template com informações específicas do projeto (nome, autor, portas, etc.) através de variáveis.
* **Interatividade:** Solicita valores para variáveis não definidas em tempo de execução.
* **Extensível:** Facilmente adaptável para incluir novos tipos de projetos e funcionalidades.

## 📦 Estrutura do Projeto do Gerador

A organização do seu gerador é modular, facilitando a adição de novos templates e a manutenção:

my-scaffolder/                 <-- Diretório raiz do SEU gerador
├── main.py                    <-- Script principal do gerador
├── config/
│   └── projects.yaml          <-- Definições dos tipos de projeto e suas variáveis
└── templates/                 <-- Modelos de estrutura e arquivos para os projetos
├── nodejs-express/        <-- Exemplo: Template para Node.js Express API
│   ├── .env
│   ├── .gitignore
│   ├── package.json
│   └── src/
│       ├── app.js
│       └── routes/
│           └── index.js
├── python-basic/          <-- Exemplo: Template para Projeto Python Básico
│   ├── .gitignore
│   ├── requirements.txt
│   └── main.py
└── html-css-js/           <-- Exemplo: Template para Website Estático
├── index.html
├── css/
│   └── style.css
└── js/
└── script.js


## 🛠️ Instalação

1.  **Clone (ou Baixe) o Repositório:**
    Se este gerador estiver em um repositório Git:
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd my-scaffolder 
    ```
    Caso contrário, apenas organize os arquivos na estrutura acima.

2.  **Instale as Dependências Python:**
    Este projeto requer `Jinja2` para o sistema de templates e `PyYAML` para ler os arquivos de configuração.
    
    ```bash
    pip install Jinja2 PyYAML
    ```

## 🚀 Como Usar

Para usar o gerador, navegue até o diretório `my-scaffolder/` (onde o `main.py` está) no seu terminal e execute o script com os argumentos necessários:

```bash
python main.py <tipo_do_projeto> <diretorio_destino> [OPÇÕES]
