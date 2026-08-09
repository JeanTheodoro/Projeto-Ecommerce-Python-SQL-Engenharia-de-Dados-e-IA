# 🛒 E-commerce Analytics — dbt + Supabase

Projeto de engenharia de dados para processamento e transformação de dados de **E-commerce**, utilizando **dbt** e **Supabase/PostgreSQL**.

A arquitetura segue o conceito de **Medallion Architecture**, dividindo o processamento em três camadas:

```text
                ┌─────────────────────┐
                │     Dados Fonte     │
                │   E-commerce / CSV  │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │       BRONZE        │
                │ Dados brutos        │
                │ + staging inicial   │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │       SILVER        │
                │ Dados tratados      │
                │ + padronização      │
                │ + regras de negócio │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │        GOLD         │
                │ KPIs e indicadores  │
                │ para análise        │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │       BI /          │
                │     Analytics       │
                └─────────────────────┘
```

---

## 📋 Tecnologias

- **dbt Core**
- **PostgreSQL**
- **Supabase**
- **SQL**
- **Git**
- **Python** — ambiente utilizado para execução do dbt

---

# 🏗️ Arquitetura

O projeto utiliza três camadas principais.

## 🥉 Bronze

A camada Bronze representa a primeira etapa de transformação dos dados.

Objetivos:

- Receber os dados provenientes das fontes;
- Manter a estrutura próxima ao dado original;
- Criar uma camada intermediária para os próximos tratamentos;
- Padronizar o acesso às tabelas de origem.

Modelos:

```text
models/
└── bronze/
    ├── bronze_clientes.sql
    ├── bronze_preco_competidores.sql
    ├── bronze_produtos.sql
    └── bronze_vendas.sql
```

### Modelos Bronze

| Modelo | Descrição |
|---|---|
| `bronze_clientes` | Dados brutos/intermediários de clientes |
| `bronze_preco_competidores` | Dados de preços praticados pelos concorrentes |
| `bronze_produtos` | Dados de produtos |
| `bronze_vendas` | Dados de vendas |

---

# 🥈 Silver

A camada Silver é responsável pela transformação e tratamento dos dados.

Objetivos:

- Limpeza dos dados;
- Padronização de tipos;
- Tratamento de valores;
- Aplicação de regras de transformação;
- Preparação dos dados para consumo analítico.

Estrutura:

```text
models/
└── silver/
    ├── silver_clientes.sql
    ├── silver_preco_competidores.sql
    ├── silver_produtos.sql
    └── silver_vendas.sql
```

### Modelos Silver

| Modelo | Descrição |
|---|---|
| `silver_clientes` | Clientes tratados e padronizados |
| `silver_preco_competidores` | Preços de concorrentes tratados |
| `silver_produtos` | Produtos tratados e padronizados |
| `silver_vendas` | Vendas tratadas para análises |

---

# 🥇 Gold

A camada Gold contém os dados preparados para **Analytics, BI e indicadores de negócio**.

Nesta camada são aplicadas regras de negócio e cálculos necessários para gerar KPIs.

Estrutura:

```text
models/
└── gold/
    ├── clientes_segmentacao.sql
    ├── precos_competitividade.sql
    └── vendas_temporais.sql
```

### Modelos Gold

#### `clientes_segmentacao`

Responsável pela **segmentação dos clientes com base em receita**.

Exemplo conceitual:

```text
Clientes
   │
   ├── Receita total
   │
   ├── Quantidade de compras
   │
   └── Indicadores de consumo
            │
            ▼
     Segmentação
            │
            ├── Alto valor
            ├── Médio valor
            └── Baixo valor
```

---

#### `precos_competitividade`

Modelo responsável pela análise de **competitividade de preços**.

Permite comparar:

```text
Preço do produto
       │
       ├──────────────┐
       │              │
       ▼              ▼
Nossa empresa    Concorrentes
       │              │
       └──────┬───────┘
              ▼
       Índice de
       competitividade
```

---

#### `vendas_temporais`

Modelo responsável pela análise temporal das vendas.

Permite analisar indicadores como:

- Vendas por dia;
- Vendas por mês;
- Vendas por ano;
- Receita;
- Quantidade de vendas;
- Evolução temporal;
- Comparação entre períodos.

---

# 📁 Estrutura do Projeto

Estrutura principal do projeto dbt:

```text
ecommerce/
│
├── analyses/
│
├── logs/
│
├── macros/
│
├── models/
│   │
│   ├── bronze/
│   │   ├── bronze_clientes.sql
│   │   ├── bronze_preco_competidores.sql
│   │   ├── bronze_produtos.sql
│   │   └── bronze_vendas.sql
│   │
│   ├── example/
│   │
│   ├── gold/
│   │   ├── clientes_segmentacao.sql
│   │   ├── precos_competitividade.sql
│   │   └── vendas_temporais.sql
│   │
│   └── silver/
│       ├── silver_clientes.sql
│       ├── silver_preco_competidores.sql
│       ├── silver_produtos.sql
│       └── silver_vendas.sql
│
├── seeds/
│
├── snapshots/
│
└── target/
    │
    ├── compiled/
    │   └── ecommerce/
    │       └── models/
    │           ├── bronze/
    │           ├── gold/
    │           └── silver/
    │
    └── run/
        └── ecommerce/
            └── models/
                ├── bronze/
                ├── gold/
                └── silver/
```

---

# 🔐 Configuração das variáveis de ambiente

A conexão com o Supabase/PostgreSQL deve ser configurada através de variáveis de ambiente.

Crie um arquivo:

```text
.env
```

Exemplo:

```env
SUPABASE_DATABASE_PASSWORD=sua_senha
SUPABASE_DATABASE_HOST=seu_host
SUPABASE_DATABASE_PORT=5432
SUPABASE_DATABASE_USER=seu_usuario
SUPABASE_DATABASE_DATABASE=seu_database
SUPABASE_DATABASE_SCHEMA=seu_schema
```

### Variáveis

| Variável | Descrição |
|---|---|
| `SUPABASE_DATABASE_PASSWORD` | Senha do banco |
| `SUPABASE_DATABASE_HOST` | Host do PostgreSQL/Supabase |
| `SUPABASE_DATABASE_PORT` | Porta do PostgreSQL |
| `SUPABASE_DATABASE_USER` | Usuário do banco |
| `SUPABASE_DATABASE_DATABASE` | Nome do banco |
| `SUPABASE_DATABASE_SCHEMA` | Schema utilizado pelo projeto |

> ⚠️ **Importante:** nunca publique `SUPABASE_DATABASE_PASSWORD` em repositórios Git públicos.

Adicione o arquivo `.env` ao `.gitignore`:

```gitignore
.env
.env.*
```

Uma alternativa recomendada é utilizar um arquivo `.env.example` contendo somente os nomes das variáveis:

```env
SUPABASE_DATABASE_PASSWORD=
SUPABASE_DATABASE_HOST=
SUPABASE_DATABASE_PORT=
SUPABASE_DATABASE_USER=
SUPABASE_DATABASE_DATABASE=
SUPABASE_DATABASE_SCHEMA=
```

---

# ⚙️ Configuração do dbt

O projeto utiliza um `profiles.yml` para configurar a conexão com o banco.

Exemplo:

```yaml
ecommerce:
  target: dev

  outputs:
    dev:
      type: postgres
      host: "{{ env_var('SUPABASE_DATABASE_HOST') }}"
      user: "{{ env_var('SUPABASE_DATABASE_USER') }}"
      password: "{{ env_var('SUPABASE_DATABASE_PASSWORD') }}"
      port: "{{ env_var('SUPABASE_DATABASE_PORT') | int }}"
      dbname: "{{ env_var('SUPABASE_DATABASE_DATABASE') }}"
      schema: "{{ env_var('SUPABASE_DATABASE_SCHEMA') }}"
      threads: 4
```

O arquivo normalmente fica em:

```text
~/.dbt/profiles.yml
```

No Windows:

```text
C:\Users\<SEU_USUARIO>\.dbt\profiles.yml
```

---

# 🚀 Instalação

## 1. Criar ambiente virtual

No Windows:

```powershell
python -m venv .venv
```

Ativar:

```powershell
.\.venv\Scripts\Activate.ps1
```

No Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

---

## 2. Instalar dbt

Para PostgreSQL:

```bash
pip install dbt-postgres
```

Verifique:

```bash
dbt --version
```

---

# 🔎 Testar a conexão

Execute:

```bash
dbt debug
```

O resultado esperado é semelhante a:

```text
Connection test: [OK connection ok]
```

---

# 🏃 Executando o projeto

## Executar todos os modelos

```bash
dbt run
```

ou:

```bash
dbt build
```

`dbt build` é recomendado quando você deseja executar modelos juntamente com testes e outros recursos configurados.

---

# 🥉 Executar somente Bronze

```bash
dbt build --select bronze
```

ou:

```bash
dbt run --select bronze
```

---

# 🥈 Executar somente Silver

```bash
dbt build --select silver
```

ou:

```bash
dbt run --select silver
```

---

# 🥇 Executar somente Gold

```bash
dbt build --select gold
```

ou:

```bash
dbt run --select gold
```

---

# 🔗 Executar uma camada e suas dependências

Para executar Silver juntamente com suas dependências:

```bash
dbt build --select +silver
```

Para Gold e tudo que ela depende:

```bash
dbt build --select +gold
```

Fluxo:

```text
Bronze
   │
   ▼
Silver
   │
   ▼
Gold
```

---

# 🧪 Testes

Executar os testes:

```bash
dbt test
```

Executar testes relacionados à Gold:

```bash
dbt test --select gold
```

Executar build completo:

```bash
dbt build
```

---

# 📊 Documentação

Gerar a documentação:

```bash
dbt docs generate
```

Executar o servidor:

```bash
dbt docs serve
```

A documentação permite visualizar:

- Modelos;
- Dependências;
- Colunas;
- Descrições;
- Linhagem dos dados;
- DAG do projeto.

---

# 🔄 Data Lineage

O fluxo principal do projeto é:

```text
                 ┌───────────────────┐
                 │      Clientes     │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Bronze Clientes   │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Silver Clientes   │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌─────────────────────────┐
                 │ Clientes Segmentação    │
                 └─────────────────────────┘


                 ┌───────────────────┐
                 │      Produtos     │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Bronze Produtos   │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Silver Produtos   │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌─────────────────────────┐
                 │ Preços Competitividade  │
                 └─────────────────────────┘


                 ┌───────────────────┐
                 │       Vendas      │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │  Bronze Vendas    │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │  Silver Vendas    │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌─────────────────────────┐
                 │     Vendas Temporais    │
                 └─────────────────────────┘
```

---

# 🗃️ Modelos do Projeto

## Bronze

```text
bronze_clientes.sql
bronze_preco_competidores.sql
bronze_produtos.sql
bronze_vendas.sql
```

## Silver

```text
silver_clientes.sql
silver_preco_competidores.sql
silver_produtos.sql
silver_vendas.sql
```

## Gold

```text
clientes_segmentacao.sql
precos_competitividade.sql
vendas_temporais.sql
```

---

# 📌 Convenção de nomenclatura

Os modelos seguem a convenção:

```text
<camada>_<entidade>.sql
```

Exemplos:

```text
bronze_clientes.sql
silver_clientes.sql
```

Para modelos analíticos da camada Gold:

```text
clientes_segmentacao.sql
precos_competitividade.sql
vendas_temporais.sql
```

---

# 🧱 Arquitetura Medalhão

A arquitetura pode ser resumida da seguinte forma:

```text
┌───────────────────────────────────────────────┐
│                   SOURCE                      │
│                                               │
│ Clientes | Produtos | Vendas | Concorrentes  │
└───────────────────────┬───────────────────────┘
                        │
                        ▼
┌───────────────────────────────────────────────┐
│                    BRONZE                     │
│                                               │
│ bronze_clientes                               │
│ bronze_produtos                               │
│ bronze_vendas                                 │
│ bronze_preco_competidores                     │
└───────────────────────┬───────────────────────┘
                        │
                        ▼
┌───────────────────────────────────────────────┐
│                    SILVER                     │
│                                               │
│ silver_clientes                               │
│ silver_produtos                               │
│ silver_vendas                                 │
│ silver_preco_competidores                     │
└───────────────────────┬───────────────────────┘
                        │
                        ▼
┌───────────────────────────────────────────────┐
│                     GOLD                      │
│                                               │
│ clientes_segmentacao                          │
│ precos_competitividade                        │
│ vendas_temporais                              │
└───────────────────────┬───────────────────────┘
                        │
                        ▼
┌───────────────────────────────────────────────┐
│                 CONSUMO / BI                  │
│                                               │
│ KPIs | Dashboards | Analytics | Relatórios   │
└───────────────────────────────────────────────┘
```

---

# 🔒 Segurança

Nunca versionar informações sensíveis.

Não faça:

```text
❌ senha diretamente no profiles.yml
❌ senha diretamente nos arquivos SQL
❌ arquivo .env no Git
❌ credenciais em README.md
```

Prefira:

```text
.env
   │
   ▼
variáveis de ambiente
   │
   ▼
profiles.yml
   │
   ▼
dbt
   │
   ▼
Supabase/PostgreSQL
```

Antes de realizar o primeiro commit:

```bash
git status
```

Verifique se o `.env` não está sendo listado.

---

# 🛠️ Comandos úteis

### Verificar projeto

```bash
dbt debug
```

### Compilar SQL

```bash
dbt compile
```

### Executar modelos

```bash
dbt run
```

### Executar Bronze

```bash
dbt build --select bronze
```

### Executar Silver

```bash
dbt build --select silver
```

### Executar Gold

```bash
dbt build --select gold
```

### Executar tudo

```bash
dbt build
```

### Testes

```bash
dbt test
```

### Documentação

```bash
dbt docs generate
dbt docs serve
```

---

# 📈 Objetivo Analítico

O projeto busca transformar dados operacionais de E-commerce em informações analíticas através de três principais frentes:

### 👥 Clientes

Identificar segmentos de clientes com base em comportamento e receita.

### 💰 Competitividade

Avaliar a posição dos preços dos produtos em relação aos concorrentes.

### 📅 Vendas

Analisar o comportamento das vendas ao longo do tempo.

O resultado final é uma camada Gold preparada para consumo por ferramentas de **Business Intelligence, Analytics e tomada de decisão**.

---

# 👨‍💻 Projeto

Projeto desenvolvido como parte dos estudos de **Engenharia de Dados**, utilizando arquitetura de dados em camadas e transformação ELT com dbt.

```text
Raw Data
   ↓
Bronze
   ↓
Silver
   ↓
Gold
   ↓
Analytics
```

---
## 📄 Licença

Este projeto é destinado a fins educacionais e de estudo em Engenharia de Dados.