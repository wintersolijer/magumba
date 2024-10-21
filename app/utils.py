import sqlite3
import hashlib
import os
import random

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

class PeopleHandler:
    def __init__(self):
        self.DB_HANDLER = DbHandler()

    def create_person(self, first_name, last_name, email, password, birthday) -> dict:
        # check if email is already in use
        check_email_sql = f"""
            SELECT id FROM Person WHERE email='{email}'
        """
        existing_rows = self.DB_HANDLER.executeSQL(check_email_sql)

        if existing_rows.fetchall() != []:
            return {
                "code": 403,
                "message": "email already exists"
            }

        user_id: str = get_hash(f"{first_name}{last_name}{email}{birthday}")
        password_hash: str = get_hash(password)

        sql_statement = f"""
            INSERT INTO Person (id, first_name, last_name, email, password_hash, birth_date, points, role)
            VALUES ('{user_id}', '{first_name}', '{last_name}', '{email}', '{password_hash}', '{birthday}', 0, 'user');
        """
        self.DB_HANDLER.executeSQL(sql_statement)

        return {"code": 200, "message": "success"}

    def check_login(self, email, password) -> dict:
        password_hash: str = get_hash(password)

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
    
    def get_ranking(self) -> list:

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

    def get_points(self, id: str) -> dict:
        sql_get_points = """
            SELECT points FROM Person WHERE id = ?
        """

        current_points = self.DB_HANDLER.executeSQL(sql_get_points, (id,)).fetchone()[0]
        return {
            "user_id": id,
            "current_points": current_points
        }

    def add_points(self, id: str, points: int) -> dict:
        sql_get_points = """
            SELECT points FROM Person WHERE id = ?
        """

        current_points = self.DB_HANDLER.executeSQL(sql_get_points, (id,)).fetchone()

        if current_points is None:
            return {
                "code": 404,
                "message": f"Person with id {id} not found."
            }

        # Add the new points to the current points
        new_points = current_points[0] + points

        # SQL statement to update the points
        sql_update_points = """
            UPDATE Person
            SET points = ?
            WHERE id = ?
        """

        # Update the points in the database
        self.DB_HANDLER.executeSQL(sql_update_points, (new_points, id))

        # Commit the changes
        self.DB_HANDLER.commit()

        return {
            "code": 200,
            "message": "points added"
        }

class QuestionHandler:
    def __init__(self):
        self.DB_HANDLER = DbHandler()
    
    def add_question(self, question: str, answers: list, points: int):
        """
        adding the question
        with the answers to the other things ...
        """
        question_id: str = get_hash(question)
        
        # adding the question
        insert_question_sql: str = f"""
            INSERT INTO Question (id, question_text, points)
            VALUES ('{question_id}', '{question}', {points})
        """

        self.DB_HANDLER.executeSQL(insert_question_sql)

        for answer_obj in answers:
            is_correct = answer_obj['isTrue']
            answer = answer_obj['answer']
            answer_id = get_hash(answer + question_id)
            explanation = answer_obj['explanation']

            insert_answer_sql = f"""
                INSERT INTO Answer (id, question_id, answer, is_correct, explanation)
                VALUES ('{answer_id}', '{question_id}', '{answer}', '{is_correct}', '{explanation}')
            """

            self.DB_HANDLER.executeSQL(insert_answer_sql)

        return {
            "code": 200,
            "message": "success"
        }

    def add_course_material(self, material: str, course: str, pdf_link: str):
        material_id: str = get_hash(material)
        course_id: str = get_hash(course)
        
        insert_material_sql: str = f"""
            INSERT INTO Material (id, course_id, material_path)
            VALUES ('{material_id}', '{course_id}', '{pdf_link}')
        """

        self.DB_HANDLER.executeSQL(insert_material_sql)

    def get_random_question(self):

        select_all_question: str = """
            SELECT id, question_text, points FROM Question
        """

        all_questions_data = self.DB_HANDLER.executeSQL(select_all_question).fetchall()
        size_questions = len(all_questions_data)

        question_data: tuple = all_questions_data[random.randint(0, size_questions-1)]
        question_id: str = question_data[0]
        question_text: str = question_data[1]
        question_points: int = int(question_data[2])

        select_question_answers: str = f"""
            SELECT answer, is_correct, explanation FROM Answer
            WHERE question_id = '{question_id}'
        """
        question_answers_data: list = self.DB_HANDLER.executeSQL(select_question_answers).fetchall()

        return {
            "question": question_text,
            "answers": [
               {
                   "answer": row[0],
                   "isTrue": row[1],
                   "explanation": row[2]
               } for row in question_answers_data
            ],
            "points": question_points
        }


def get_hash(input_string: str) -> str:
    hash_object = hashlib.sha256()
    hash_object.update(input_string.encode('utf-8'))
    return hash_object.hexdigest()


class CourseHandler:
    def __init__(self):
        self.DB_HANDLER = DbHandler()
    
    def add_points(self, course_id: str, points: float) -> dict:
        sql_get_course = """
            SELECT rating, num_of_ratings FROM Course WHERE id = ?
        """
        
        course_data = self.DB_HANDLER.executeSQL(sql_get_course, (course_id,)).fetchone()

        if course_data is None:
            return {
                "code": 404,
                "message": f"Course with id {course_id} not found."
            }

        current_rating, num_of_ratings = course_data

        new_num_of_ratings = num_of_ratings + 1
        new_rating = ((current_rating * num_of_ratings) + points) / new_num_of_ratings

        sql_update_course = """
            UPDATE Course
            SET rating = ?, num_of_ratings = ?
            WHERE id = ?
        """

        # Update the course rating in the database
        self.DB_HANDLER.executeSQL(sql_update_course, (new_rating, new_num_of_ratings, course_id))

        # Commit the changes
        self.DB_HANDLER.commit()

        return {
            "code": 200,
            "message": "Rating updated successfully"
        }
