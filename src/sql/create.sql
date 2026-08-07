-- Criação da tabela de Clientes
CREATE TABLE clientes (
    id_cliente VARCHAR(50) PRIMARY KEY,
    nome_cliente VARCHAR(150) NOT NULL,
    estado VARCHAR(2) NOT NULL,
    pais VARCHAR(50) NOT NULL,
    data_cadastro TIMESTAMP NOT NULL
);

-- Criação da tabela de Produtos
CREATE TABLE produtos (
    id_produto VARCHAR(50) PRIMARY KEY,
    nome_produto VARCHAR(150) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    marca VARCHAR(50) NOT NULL,
    preco_atual NUMERIC(10, 2) NOT NULL,
    data_criacao TIMESTAMP NOT NULL
);

-- Criação da tabela de Vendas
CREATE TABLE vendas (
    id_venda VARCHAR(50) PRIMARY KEY,
    data_venda TIMESTAMP NOT NULL,
    id_cliente VARCHAR(50) NOT NULL,
    id_produto VARCHAR(50) NOT NULL,
    canal_venda VARCHAR(50) NOT NULL,
    quantidade INT NOT NULL,
    preco_unitario NUMERIC(10, 2) NOT NULL,
    CONSTRAINT fk_vendas_cliente FOREIGN KEY (id_cliente) REFERENCES clientes (id_cliente),
    CONSTRAINT fk_vendas_produto FOREIGN KEY (id_produto) REFERENCES produtos (id_produto)
);

CREATE TABLE preco_competidores (
    id_produto VARCHAR(50),
    nome_concorrente VARCHAR(100),
    preco_concorrente NUMERIC(10,2),
    data_coleta TIMESTAMP,
    CONSTRAINT fk_preco_produto
        FOREIGN KEY (id_produto)
        REFERENCES produtos(id_produto)
);
