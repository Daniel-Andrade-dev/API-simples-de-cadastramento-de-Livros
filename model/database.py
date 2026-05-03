import sqlite3 as lite

LIVROS = 'livros.db'

class Biblioteca:
    def __init__(self):
        self.db_path = LIVROS
        self.tabela_livros()

    def get_conn(self):
        conn = lite.connect(self.db_path)
        conn.row_factory = lite.Row #Invés de pegar pelos index [1] o Row ajuda pegando pela chave ['nome']
        return conn
    
    def tabela_livros(self):
        try:
            with self.get_conn() as conn:
                conn.execute("""
                        CREATE TABLE IF NOT EXISTS livros (
                            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            nome TEXT NOT NULL,
                            autor TEXT NOT NULL,
                            preco FLOAT NOT NULL,
                            ano INTEGER NOT NULL,
                            data_retirada DATE NOT NULL,
                            data_entrega DATE NOT NULL
                            )
                        """)
                return conn
        except lite.Error as e:
            raise ValueError(f"Erro ao criar tabela >> {e}")
        
    def cadastrar_livro(self, nome, autor, preco,ano, data_retirada, data_entrega):
        try:
            with self.get_conn() as conn:
                conn.execute("INSERT INTO livros (nome,autor,preco,ano,data_retirada,data_entrega) VALUES(?,?,?,?,?,?)",
                                   (nome,autor,preco,ano,data_retirada,data_entrega)
                                )
                return True
        except lite.Error as e:
            raise ValueError(f"Erro ao cadastrar livro no banco >> {e}")
        
    def listar_livros(self):
        try:
            with self.get_conn() as conn:
                cur = conn.execute("SELECT * FROM livros")
                livros = cur.fetchall()
            return [dict(livro) for livro in livros]
        except lite.Error as e:
            raise ValueError(f"Erro ao listar livros no banco >> {e}")

    def excluir_livro(self, livro_id):
        try:
            with self.get_conn() as conn:
                cur = conn.execute("DELETE FROM livros WHERE id = ?",(livro_id,))
            return cur.rowcount > 0
        except lite.Error as e:
            raise ValueError(f"Erro ao deletar livro no banco >> {e}")
        
    def buscar_livro(self, livro_id):
        try:
            with self.get_conn() as conn:
                cur = conn.execute("SELECT * FROM livros WHERE id = ?", (livro_id,))
                livro = cur.fetchone()
            return dict(livro) if livro else None
        except lite.Error as e:
            raise ValueError(f"Erro ao buscar livro no banco >> {e}")