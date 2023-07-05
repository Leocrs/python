# Métodos Mágicos- Atributos e métodos disponiveis para determinar
# tipo de dados o variaveis podem ter diferentes tipos de atributos e métodos
# Dunder __init__ (duble underscore)

class Livro:
    def __init__(self, titulo, autor, paginas): # __init__ é o construtor
        self.titulo = titulo
        self.autor = autor 
        self.paginas = paginas
    def __repr__(self): # __repr__  é o método 
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Paginas: {self.paginas}" 
    
    def __len__ (self):
        return self.paginas
               
livro1 = Livro("O Senhor dos Aneis", "J.R.R. Paginas", 400)
livro2 = Livro(" Nas Estrelas", "J.R.R. Paginas", 300)

print(livro1)
print(livro2)
print(len(livro1))
print(len(livro2))