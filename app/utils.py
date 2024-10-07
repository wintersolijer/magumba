import sqlite3
import hashlib
import os

class DbHandler:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, "database", "db.sql")
        self.conn: sqlite3.Connection = sqlite3.connect(db_path, check_same_thread=False)
        self.cur: sqlite3.Cursor = self.conn.cursor()

    def executeSQL(self, command:str):
        data = self.cur.execute(command)
        self.conn.commit()    
        return data

class PeopleHander:
    def __init__(self):
        self.DB_HANDLER = DbHandler()

    def createPerson(self, first_name, last_name, email, password, birthday) -> dict:
        id: str = getHash(f"{first_name}{last_name}{email}{birthday}")
        password_hash: str = getHash(password)

        sql_statement = f"""
            INSERT INTO Person (id, first_name, last_name, email, password_hash, birth_date, points, role)
            VALUES ('{id}', '{first_name}', '{last_name}', '{email}', '{password_hash}', '{birthday}', 0, 'user');
            """
        self.DB_HANDLER.executeSQL(sql_statement)

        return {"code": 200, "message": "success"}

    def checkLogin(self, email, password) -> dict:
        password_hash: str = getHash(password)

        sql_statement: str = f"""
            SELECT id FROM Person WHERE email='{email}' AND password_hash='{password_hash}'
        """
        data: list = self.DB_HANDLER.executeSQL(sql_statement).fetchall()
        if data == []:
            return {
                "code": 401,
                "message": "invalid login"
            }
        return {
            "code": 200,
            "message": "success",
            "user_id": data[0][0]
        }
    
    def getRanking(self) -> list:

        sql_statement: str = """
            SELECT id, last_name, first_name, points FROM Person ORDER BY points
        """

        data: list = self.DB_HANDLER.executeSQL(sql_statement).fetchall()
        return [
            {
                "id": person_data[0],
                "last_name": person_data[1],
                "first_name": person_data[2],
                "points": person_data[3],
            } for person_data in data
        ]

# utils function 
def getHash(input_string: str) -> str:
    hash_object = hashlib.sha256()
    hash_object.update(input_string.encode('utf-8'))
    return hash_object.hexdigest()