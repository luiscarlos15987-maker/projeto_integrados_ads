-- Laboratório acadêmico isolado. Exemplos ainda não executados nesta sessão.
CREATE DATABASE IF NOT EXISTS ads_revisao CHARACTER SET utf8mb4;
USE ads_revisao;
CREATE TABLE IF NOT EXISTS categoria (
 id INT PRIMARY KEY, nome VARCHAR(80) NOT NULL
) ENGINE=InnoDB;
CREATE TABLE IF NOT EXISTS produto (
 id INT PRIMARY KEY, nome VARCHAR(100) NOT NULL,
 categoria_id INT NOT NULL, preco DECIMAL(10,2) NULL,
 CONSTRAINT fk_categoria FOREIGN KEY (categoria_id) REFERENCES categoria(id)
) ENGINE=InnoDB;
-- Executar INSERT uma vez em banco novo; IDs duplicados geram erro ao repetir.
INSERT INTO categoria VALUES (1,'Mel'),(2,'Chia'),(3,'Barras');
INSERT INTO produto VALUES (1,'Mel puro',1,20.00),(2,'Chia a granel',2,NULL);
SELECT COUNT(*) AS linhas, COUNT(preco) AS precos_informados FROM produto;
-- Esperado: linhas=2; precos_informados=1.
SELECT c.nome, COUNT(p.id) AS produtos
FROM categoria c LEFT JOIN produto p ON p.categoria_id=c.id
GROUP BY c.id,c.nome ORDER BY c.id;
-- Esperado: Mel=1, Chia=1, Barras=0.
START TRANSACTION;
UPDATE produto SET preco=22.00 WHERE id=1;
SAVEPOINT ajuste;
UPDATE produto SET preco=25.00 WHERE id=1;
ROLLBACK TO SAVEPOINT ajuste;
SELECT preco FROM produto WHERE id=1; -- Esperado: 22.00 nesta transação.
ROLLBACK; -- Reverte o primeiro UPDATE; preço volta a 20.00.

