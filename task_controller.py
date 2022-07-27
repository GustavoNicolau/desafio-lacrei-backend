import json
from database import get_db


def insert_task(name, description):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO tasks(name, description) VALUES (?, ?)"
    cursor.execute(statement, [name, description])
    db.commit()
    return True


def get_tasks():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT * FROM tasks"
    cursor.execute(query)
    data = cursor.fetchall()
    result = []
    for item in data:
        result.append({"id": item[0], "name": item[1], "description": item[2]})
    return result