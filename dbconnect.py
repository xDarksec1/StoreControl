import sqlite3


class ConnectDb:
    def __init__(self):

        self.connect = sqlite3.connect("prodDB.db")
        self.cursor = self.connect.cursor()

        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS produtos ("
            "id INTEGER UNIQUE,"
            "nome TEXT,"
            "valor REAL,"
            "quantidade INTEGER,"
            "categoria TEXT"
            ")"
        )

    def add_prod(self, id, nome, valor, qtde, categoria):
        self.cursor.execute(
            "INSERT INTO produtos (id, nome, valor, quantidade, categoria) VALUES (?, ?, ?, ?, ?)",
            (id, nome, valor, qtde, categoria),
        )
        self.connect.commit()
        self.close_connection()

    def update_prod(self, id, nome, valor, qtde):
        consult = (
            "UPDATE OR IGNORE produtos SET nome=?, valor=?, quantidade=? WHERE id=?"
        )
        self.cursor.execute(consult, (nome, valor, qtde, id))

        self.connect.commit()
        self.close_connection()

    def update_category(self, id, categoria_nova):
        consult = "UPDATE OR IGNORE produtos SET categoria=? WHERE id=?"
        self.cursor.execute(consult, (categoria_nova, id))
        self.connect.commit()
        self.close_connection()

    def del_id(self, num):
        consult = "DELETE FROM produtos WHERE id=?"
        self.cursor.execute(consult, (num,))
        self.connect.commit()
        self.close_connection()

    # def get_colum(self):
    #     self.cursor.execute("SELECT name FROM PRAGMA_TABLE_INFO('produtos')")
    #     lista = list(self.cursor.fetchall())
    #     lst = []
    #     for i in lista:
    #         i = "".join(i)
    #         lst.append(i)
    #     self.close_connection()
    #
    #     return lst

    def get_all_db(self):
        self.cursor.execute('SELECT * FROM produtos ORDER BY "id" ASC LIMIT 0, 49999;')

        lst = self.cursor.fetchall()
        self.close_connection()

        return lst

    def search_id(self, id):
        consult = "SELECT * FROM produtos WHERE id LIKE ?"
        self.cursor.execute(
            consult + ' ORDER BY "id" ASC LIMIT 0, 49999;', (f"%{id}%",)
        )
        lst = self.cursor.fetchall()
        self.close_connection()
        return lst

    def search_all(self, text):
        consult = "SELECT * FROM produtos WHERE nome LIKE ?"
        self.cursor.execute(
            consult + ' ORDER BY "id" ASC LIMIT 0, 49999;', (f"%{text}%",)
        )
        lst = self.cursor.fetchall()
        self.close_connection()
        return lst

    def search_nome(self, nome):
        consult = "SELECT * FROM produtos WHERE nome LIKE ?"
        self.cursor.execute(
            consult + ' ORDER BY "id" ASC LIMIT 0, 49999;', (f"%{nome}%",)
        )
        lst = self.cursor.fetchall()
        self.close_connection()
        return lst

    def close_connection(self):
        self.cursor.close()
        self.connect.close()
