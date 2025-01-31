-- Selecionar os primeiros registros
SELECT TOP (20) PERCENT NomeLivro 
FROM Livro
ORDER BY NomeLivro;

-- Selecionar todos os registros da tabela Livro
SELECT * FROM Livro;

-- Inserir registros na tabela Livro
INSERT INTO Livro (NomeLivro, ISBN13, DataPub, PrecoLivro, NumeroPaginas, IdAssunto, IdEditora)
VALUES
    ('Vinte Mil Léguas Submarinas', '9788582850022', '2014-09-16', 24.50, 448, 1, 16), -- Júlio Verne
    ('O Investidor Inteligente', '9788595080805', '2016-01-25', 79.90, 450, 7, 6); -- Benjamin Graham

-- Verificar inserção
SELECT * FROM Livro;

-- Inserir mais um registro na tabela Livro
INSERT INTO Livro (NomeLivro, ISBN13, DataPub, PrecoLivro, NumeroPaginas, IdAssunto, IdEditora)
VALUES 
    ('A Arte da Eletrônica', '9788582604342', '2017-03-08', 300.74, 1160, 3, 24);

-- Verificar inserção
SELECT * FROM Livro;

-- Inserir registros em lote a partir de arquivo CSV
INSERT INTO Livro (NomeLivro, ISBN13, DataPub, PrecoLivro, NumeroPaginas, IdEditora, IdAssunto)
SELECT 
    NomeLivro, ISBN13, DataPub, PrecoLivro, NumeroPaginas, IdEditora, IdAssunto
FROM OPENROWSET(
    BULK 'C:\SQL\Livros.CSV',
    FORMATFILE = 'C:\SQL\Formato.xml',
    CODEPAGE = '65001',  -- UTF-8
    FIRSTROW = 2
) AS LivrosCSV;

-- Verificar inserção
SELECT * FROM Livro;

-- Inserir registros na tabela LivroAutor
INSERT INTO LivroAutor (IdLivro, IdAutor)
VALUES
    (100, 15),
    (100, 16),
    (101, 27),
    (102, 26),
    (103, 41),
    (104, 24),
    (105, 32),
    (106, 20),
    (107, 27),
    (108, 1),
    (109, 22),
    (110, 10),
    (111, 21),
    (112, 5),
    (113, 10),
    (114, 8),
    (115, 18),
    (115, 19),
    (116, 31),
    (117, 22);

-- Verificar inserção
SELECT * FROM LivroAutor;

-- Consulta com INNER JOIN para verificar livros e autores
SELECT NomeLivro, NomeAutor, SobrenomeAutor
FROM Livro
INNER JOIN LivroAutor
    ON Livro.IdLivro = LivroAutor.IdLivro
INNER JOIN Autor
    ON Autor.IdAutor = LivroAutor.IdAutor
ORDER BY NomeLivro;

-- Inserir um novo registro na tabela Livro
INSERT INTO Livro (NomeLivro, ISBN13, DataPub, PrecoLivro, NumeroPaginas, IdAssunto, IdEditora)
VALUES 
    ('A Arte da Eletrônica', '9788582604342', '2017-03-08', 300.74, 1160, 3, 24);

-- Verificar inserção
SELECT * FROM Livro;

-- Selecionar registros da tabela Editora onde IdEditora é 24
SELECT * FROM Editora WHERE IdEditora = 24;

-- Inserir um novo registro na tabela Editora
INSERT INTO Editora (IdEditora, NomeEditora) VALUES (24, 'Nome da Editora Exemplo');

-- Inserir registros na tabela Livro
INSERT INTO Livro (NomeLivro, ISBN13, DataPub, PrecoLivro, NumeroPaginas, IdAssunto, IdEditora)
VALUES
    ('Vinte Mil Léguas Submarinas', '9788582850022', '2014-09-16', 24.50, 448, 1, 16), -- Júlio Verne
    ('O Investidor Inteligente', '9788595080805', '2016-01-25', 79.90, 450, 7, 6); -- Benjamin Graham

-- Aula 10: Filtrar Resultado de Consultas com Where
-- (adicionar consultas com cláusulas WHERE conforme necessário)
/* Sintaxe
SELECT colunas
FROM tabela 
WHERE coluna [operador] valor;
[ORDER BY]

*/

SELECT NomeLivro, DataPub 
FROM Livro
WHERE idEditora = 3;


-- Comandos SQL que você precisa conhecer

/*
SELECT -  Serve para selecionar as colunas da tabela
Exemplo: SELECT NomeLivro, ISBN13, DataPub, PrecoLivro, NumeroPaginas, IdEditora, IdAssunto

WHERE - Serve para filtrar as linhas da tabela
Exemplo: WHERE idEditora = 3

INSERT - Serve para inserir um novo registro na tabela
Exemplo: INSERT INTO Livro (NomeLivro, ISBN13, DataPub, PrecoLivro, NumeroPaginas, IdEditora, IdAssunto)

UPDATE -  Serve para atualizar um registro na tabela
Exemplo: UPDATE Livro SET NomeLivro = 'Nome do Livro Atualizado' WHERE idEditora = 3

DELETE -  Serve para remover um registro da tabela
Exemplo: DELETE FROM Livro WHERE idEditora = 3

ORDER -  BY Serve para ordenar os registros da tabela
Exemplo: ORDER BY NomeLivro

GROUP -  BY Serve para agrupar os registros da tabela 
Exemplo: GROUP BY NomeLivro registros de livros com o mesmo nome

JOIN -  Serve para juntar duas ou mais tabelas
Exemplo: JOIN LivroAutor ON Livro.IdLivro = LivroAutor.IdLivro

CREATE -  Serve para criar uma nova tabela
Exemplo: CREATE TABLE Editora (IdEditora INT, NomeEditora VARCHAR(50))

ALTER -  Serve para alterar uma tabela
Exemplo: ALTER TABLE Editora ADD Cidade VARCHAR(50)
*/