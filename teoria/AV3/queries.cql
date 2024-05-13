1-
CREATE TABLE IF NOT EXISTS estoque (
    oid INT PRIMARY KEY,
    nome TEXT,
    carro TEXT,
    estante INT,
    nivel INT,
    quantidade INT,
);

INSERT INTO estoque (oid, nome, carro, estante, nivel, quantidade) VALUES (5, 'Pistao', 'Mustang', 4, 1, 167);
INSERT INTO estoque (oid, nome, carro, estante, nivel, quantidade) VALUES (4, 'Suspencao', 'Argo', 1, 1, 3500);

2-
SELECT * FROM estoque WHERE nome = 'Pistao' ALLOW FILTERING;
SELECT AVG(quantidade) AS "media_colunas" FROM estoque;
SELECT COUNT(*) AS "n_colunas" FROM estoque;
SELECT MAX(quantidade) AS "maior quantidade", MIN(quantidade) AS "menor quantidade" FROM estoque;
SELECT nome, carro, quantidade FROM estoque WHERE estante = 3 ALLOW FILTERING;
SELECT AVG(quantidade) AS "media_qtd" FROM estoque WHERE nivel = 1 ALLOW FILTERING;
SELECT * FROM estoque WHERE estante < 3 AND nivel > 4 ALLOW FILTERING;