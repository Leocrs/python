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