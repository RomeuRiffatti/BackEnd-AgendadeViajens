import sqlite3
from sqlite3 import Connection ## para dizer que vai retornar um objeto connection, uma conexão com o banco de dados

class DbConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "storage.db"
        self._conn = None
    
    def connect(self) -> None:
        conn = sqlite3.connect(self.__connection_string, check_same_thread=False)
        self._conn = conn

    def get_connection(self) -> Connection:
        return self._conn
    
db_connection_handler = DbConnectionHandler() ##objeto que tem uma conexão direta com o DB