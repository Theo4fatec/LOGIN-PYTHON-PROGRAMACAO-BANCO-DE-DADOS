-- Active: 1709644586203@@127.0.0.1@5432@20242_fatec_ipi_pbdi_theo@public

CREATE TABLE tb_usuario(
    cod_usuario SERIAL PRIMARY KEY,
    login VARCHAR(200) NOT NULL,
    senha VARCHAR(200) NOT NULL
);

INSERT INTO tb_usuario(login, senha)
VALUES
('admin', 'admin'),
('joao', '123456');

SELECT * FROM tb_usuario;