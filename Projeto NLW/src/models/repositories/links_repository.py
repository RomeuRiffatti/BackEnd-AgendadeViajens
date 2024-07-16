from typing import Dict, Tuple, List
from sqlite3 import Connection

class LinksRepository():
    
    def __init__(self, conn: Connection) -> None:  ##conn é o parâmetro que está recebendo a conexão. Depois dos dois pontos é a tipagem, onde diz qual o tipo de dado que vai ser passado como parâmetro
        self.__conn = conn                         ## nao consegui entender como ele faz para puxar este objeto "conn" para colocar ele aqui como parâmetro 

    def registry_link(self, link_infos: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO links
                    (id, trip_id, link, title)
                VALUES
                    (?, ?, ?, ?)
            ''',    (   
                link_infos["id"],
                link_infos["trip_id"],
                link_infos["link"],
                link_infos["title"],
            )
        )
        self.__conn.commit()

    def find_links_from_trip(self, trip_id: str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''SELECT * FROM links WHERE trip_id = ?''', (trip_id,)
        )
        links = cursor.fetchall()
        return links
        
    