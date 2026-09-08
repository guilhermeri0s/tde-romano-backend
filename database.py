import sqlite3
from contextlib import contextmanager

CAMINHO_BANCO = "erp.db"


@contextmanager
def conectar():
  
    conexao = sqlite3.connect(CAMINHO_BANCO)
    conexao.row_factory = sqlite3.Row
    try:
        yield conexao
        conexao.commit()
    except Exception:
        conexao.rollback()
        raise
    finally:
        conexao.close()


def criar_tabelas():
     with conectar() as conexao:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id       INTEGER PRIMARY KEY AUTOINCREMENT,
                nome     TEXT NOT NULL,
                email    TEXT NOT NULL UNIQUE,
                telefone TEXT NOT NULL,
                cidade   TEXT NOT NULL
            )
        """)
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                nome       TEXT    NOT NULL,
                codigo     TEXT    NOT NULL UNIQUE,
                preco      REAL    NOT NULL,
                quantidade INTEGER NOT NULL
            )
        """)