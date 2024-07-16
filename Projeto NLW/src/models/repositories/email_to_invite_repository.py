from typing import Dict, Tuple, List
from sqlite3 import Connection

class EmailstoInviteRepository():
    
    def __init__(self, conn: Connection) -> None:  ##conn é o parâmetro que está recebendo a conexão. Depois dos dois pontos é a tipagem, onde diz qual o tipo de dado que vai ser passado como parâmetro
        self.__conn = conn                         ## nao consegui entender como ele faz para puxar este objeto "conn" para colocar ele aqui como parâmetro 

    def registry_email(self, email_infos: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO emails_to_invite
                    (id, trip_id, email)
                VALUES
                    (?, ?, ?)
            ''',    (   
                email_infos["id"],
                email_infos["trip_id"],
                email_infos["email"],
            )
        )
        self.__conn.commit()

    def find_emails_from_trip(self, trip_id: str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''SELECT * FROM emails_to_invite WHERE id = ?''', (trip_id,)
        )
        emails = cursor.fetchall()
        return emails
        
    