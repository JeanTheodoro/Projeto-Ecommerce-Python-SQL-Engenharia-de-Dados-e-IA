# 🛒 Projeto E-commerce — Data Engineering

Pipeline de dados para processamento e transformação de dados de um e-commerce, utilizando **Python, Pandas, Parquet, Supabase Storage via S3 e dbt**.

O projeto utiliza uma abordagem inspirada na **Arquitetura Medalhão**, organizando os dados nas camadas:

```text
Bronze → Silver → Gold
```

---

## 📌 Arquitetura

O fluxo principal do projeto é:

```text
                    ┌──────────────────┐
                    │   Arquivos CSV   │
                    │     data/raw     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │      Python      │
                    │     Pandas       │
                    │   CSV → Parquet  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │     Parquet      │
                    │   data/parquet   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Supabase Storage │
                    │    S3 API        │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │       dbt        │
                    │                  │
                    │ Bronze → Silver  │
                    │        → Gold    │
                    └──────────────────┘
```

---

# 📂 Estrutura do projeto

```text
src/
│
├── data/
│   ├── raw/
│   │   ├── clientes.csv
│   │   ├── preco_competidores.csv
│   │   ├── produtos.csv
│   │   └── vendas.csv
│   │
│   ├── parquet/
│   │   ├── clientes.parquet
│   │   ├── preco_competidores.parquet
│   │   ├── produtos.parquet
│   │   └── vendas.parquet
│   │
│   └── converter_csv_to_parquet.py
│
├── dbt/
│   ├── ecommerce/
│   │   ├── analyses/
│   │   ├── logs/
│   │   ├── macros/
│   │   ├── models/
│   │   │   ├── bronze/
│   │   │   ├── silver/
│   │   │   ├── gold/
│   │   │   └── example/
│   │   │
│   │   ├── seeds/
│   │   ├── snapshots/
│   │   ├── target/
│   │   └── tests/
│   │
│   └── logs/
│
├── settings/
│   └── s3/
│       └── connection.py
│
├── sql/
│
└── main.py
```

---

# 🐍 Tecnologias utilizadas

* Python
* Pandas
* PyArrow
* Boto3
* python-dotenv
* Supabase Storage
* S3 API
* Parquet
* dbt
* PostgreSQL

---

# ⚙️ Pré-requisitos

Antes de executar o projeto, tenha instalado:

* Python 3.11+
* Git
* uv
* acesso a um projeto Supabase
* dbt

---

# 📦 Instalação do ambiente Python

## 1. Clonar o projeto

```bash
git clone <URL_DO_REPOSITORIO>
```

Entrar no projeto:

```bash
cd Projeto_ecomerce
```

---

## 2. Criar o ambiente virtual

Utilizando `uv`:

```bash
uv venv
```

Ativar no Windows:

```powershell
.venv\Scripts\activate
```

No Linux/macOS:

```bash
source .venv/bin/activate
```

---

# 📚 Instalar dependências

Caso esteja utilizando `pyproject.toml`:

```bash
uv sync
```

Isso instalará as dependências especificadas no projeto.

Também é possível adicionar as principais dependências manualmente:

```bash
uv add pandas pyarrow boto3 python-dotenv
```

### Dependências

| Biblioteca      | Finalidade                           |
| --------------- | ------------------------------------ |
| `pandas`        | Leitura e transformação dos CSVs     |
| `pyarrow`       | Escrita dos arquivos Parquet         |
| `boto3`         | Comunicação utilizando a API S3      |
| `python-dotenv` | Carregamento das variáveis do `.env` |

---

# 🔐 Configuração das variáveis de ambiente

Crie um arquivo:

```text
.env
```

na raiz do projeto:

```text
Projeto_ecomerce/
├── .env
├── pyproject.toml
├── uv.lock
└── src/
```

Configure:

```env
SUPABASE_DATALAKE_ENDPOINT=SEU_ENDPOINT
SUPABASE_REGION=SUA_REGION
SUPABASE_BUCKET_NAME=SEU_BUCKET
SUPABASE_ACCESS_KEY_ID=SUA_ACCESS_KEY
SUPABASE_SECRET_ACCESS_KEY=SUA_SECRET_KEY
```

> ⚠️ Nunca versionar o arquivo `.env`.

Adicione ao `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

---

# 🗄️ Supabase Storage

O projeto utiliza o **Supabase Storage através da compatibilidade com S3**.

O `boto3` é utilizado como cliente S3:

```python
boto3.client(
    "s3",
    endpoint_url=self.endpoint,
    region_name=self.region,
    aws_access_key_id=self.access_key_id,
    aws_secret_access_key=self.secret_access_key,
)
```

O `endpoint_url` aponta para o Supabase, portanto:

```text
Python
   │
   ▼
Boto3
   │
   ▼
S3 API
   │
   ▼
Supabase Storage
```

---

# 🔄 Conversão CSV → Parquet

A função:

```python
converter_csv_to_parquet()
```

procura automaticamente todos os arquivos `.csv` existentes em:

```text
data/raw/
```

e converte para Parquet.

Exemplo:

```text
data/raw/clientes.csv
        ↓
data/parquet/clientes.parquet
```

```text
data/raw/produtos.csv
        ↓
data/parquet/produtos.parquet
```

```text
data/raw/vendas.csv
        ↓
data/parquet/vendas.parquet
```

```text
data/raw/preco_competidores.csv
        ↓
data/parquet/preco_competidores.parquet
```

O nome do arquivo é preservado, alterando somente a extensão.

---

# ☁️ Upload para o Supabase

Depois da conversão, o `main.py` lê cada arquivo Parquet e envia para o Supabase Storage.

Exemplo:

```text
data/parquet/vendas.parquet
             │
             ▼
       upload_bytes()
             │
             ▼
Supabase Storage
             │
             ▼
parquet/vendas.parquet
```

O prefixo utilizado atualmente é:

```text
parquet/
```

Portanto, os arquivos serão armazenados como:

```text
parquet/clientes.parquet
parquet/preco_competidores.parquet
parquet/produtos.parquet
parquet/vendas.parquet
```

---

# ▶️ Executando o pipeline Python

Entre na pasta `src`:

```powershell
cd src
```

Execute:

```powershell
python main.py
```

Ou, utilizando `uv`:

```powershell
uv run python main.py
```

---

# 🔎 Exemplo de execução

Durante a execução, o pipeline deverá apresentar mensagens semelhantes a:

```text
Convertendo: clientes.csv
Parquet criado: clientes.parquet

Convertendo: preco_competidores.csv
Parquet criado: preco_competidores.parquet

Convertendo: produtos.csv
Parquet criado: produtos.parquet

Convertendo: vendas.csv
Parquet criado: vendas.parquet
```

Depois será realizado o upload:

```text
########
parquet: parquet/clientes.parquet
########
Upload realizado: parquet/clientes.parquet

########
parquet: parquet/preco_competidores.parquet
########
Upload realizado: parquet/preco_competidores.parquet

########
parquet: parquet/produtos.parquet
########
Upload realizado: parquet/produtos.parquet

########
parquet: parquet/vendas.parquet
########
Upload realizado: parquet/vendas.parquet
```

---

# 🧱 dbt

Depois da etapa de ingestão, o projeto utiliza **dbt** para transformação dos dados.

As transformações estão organizadas em:

```text
dbt/ecommerce/models/
│
├── bronze/
├── silver/
└── gold/
```

## Bronze

A camada Bronze representa os dados em seu estado mais próximo possível da origem.

```text
Bronze
  │
  └── Dados brutos / staging
```

---

## Silver

A camada Silver realiza tratamentos e transformações:

```text
Silver
  │
  ├── limpeza
  ├── padronização
  ├── tratamento de tipos
  └── regras de negócio intermediárias
```

---

## Gold

A camada Gold contém dados preparados para consumo analítico:

```text
Gold
  │
  ├── KPIs
  ├── métricas
  ├── agregações
  └── modelos analíticos
```

---

# 🚀 Executando o dbt

Entre no projeto:

```powershell
cd src/dbt/ecommerce
```

Verifique a conexão:

```powershell
dbt debug
```

Execute os modelos:

```powershell
dbt run
```

Ou:

```powershell
dbt build
```

O `dbt build` também executa testes associados aos modelos.

---

# 🥉 Executar somente Bronze

```powershell
dbt build --select bronze
```

# 🥈 Executar somente Silver

```powershell
dbt build --select silver
```

# 🥇 Executar somente Gold

```powershell
dbt build --select gold
```

Executar todo o pipeline:

```powershell
dbt build
```

---

# 🔁 Fluxo completo

Para executar o projeto desde a ingestão:

### 1. Colocar os CSVs

```text
src/data/raw/
```

### 2. Executar Python

```powershell
cd src
python main.py
```

O Python:

```text
CSV
 ↓
Parquet
 ↓
Supabase Storage
```

### 3. Executar dbt

```powershell
cd src/dbt/ecommerce
dbt build
```

Resultado:

```text
Supabase / Dados de origem
          │
          ▼
       Bronze
          │
          ▼
       Silver
          │
          ▼
        Gold
```

---

# 📊 Arquitetura Medalhão

O projeto segue o conceito:

```text
                    DATA LAKE
                       │
                       ▼
              ┌─────────────────┐
              │     BRONZE      │
              │  Dados brutos   │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │     SILVER      │
              │ Dados tratados  │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │      GOLD       │
              │      KPIs       │
              │   Analytics     │
              └─────────────────┘
```

---

# 🧪 Testes

Para validar a configuração do dbt:

```bash
dbt debug
```

Para executar testes:

```bash
dbt test
```

Para executar modelos e testes:

```bash
dbt build
```

---

# 🛠️ Comandos úteis

### Ver versão do Python

```bash
python --version
```

### Ver versão do uv

```bash
uv --version
```

### Instalar dependências

```bash
uv sync
```

### Adicionar dependência

```bash
uv add nome-da-biblioteca
```

### Executar Python

```bash
uv run python src/main.py
```

### Validar dbt

```bash
dbt debug
```

### Executar dbt

```bash
dbt build
```

---

# 🔒 Segurança

Nunca coloque credenciais diretamente no código.

❌ Evite:

```python
boto3.client(
    "s3",
    aws_access_key_id="minha-chave",
    aws_secret_access_key="minha-secret",
)
```

✅ Utilize variáveis de ambiente:

```python
os.getenv("SUPABASE_ACCESS_KEY_ID")
os.getenv("SUPABASE_SECRET_ACCESS_KEY")
```

E mantenha:

```text
.env
```

fora do Git.

---

# 👨‍💻 Autor

Projeto desenvolvido como estudo prático de **Data Engineering**, explorando:

* ingestão de dados;
* armazenamento em Data Lake;
* formato Parquet;
* S3;
* Supabase Storage;
* Python;
* Pandas;
* dbt;
* Arquitetura Medalhão;
* transformação de dados;
* criação de camadas analíticas.
