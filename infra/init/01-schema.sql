-- Schema inicial do Cadastro de Pessoas.
-- Executado automaticamente pelo MySQL na primeira inicialização do
-- contêiner principal, antes de a replicação ser configurada.

CREATE DATABASE IF NOT EXISTS cadastro
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_0900_ai_ci;

USE cadastro;

CREATE TABLE IF NOT EXISTS pessoa (
  id INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(100) NOT NULL,
  idade INT NOT NULL,
  email VARCHAR(150) NOT NULL,
  PRIMARY KEY (id),
  KEY idx_pessoa_nome (nome)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
