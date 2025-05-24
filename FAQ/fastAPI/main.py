import pymysql
import os
import json
from dotenv import load_dotenv

def get_key(cursor):
    cursor.execute("SELECT description FROM Icog WHERE id = %s", ("key",))
    result = cursor.fetchone()
    if result:
         stored_list = json.loads(result["description"])
         return stored_list
    else:
        return []
def get_knowledge(cursor):
    cursor.execute("SELECT description FROM Icog WHERE id = %s", ("Knowledge",))
    result = cursor.fetchone()
    return result["description"]
def updateKey(array,cursor,connection):
    update_query = """
    UPDATE Icog
    SET description = %s
    WHERE id = %s
    """
    dataString = json.dumps(array)
    data = (dataString, "key")
    cursor.execute(update_query, data)
    connection.commit()
    return "Done"
def updateKnowledge(knowledge,cursor,connection):
    update_query = """
    UPDATE Icog
    SET description = %s
    WHERE id = %s
    """
    data = (knowledge, "Knowledge")
    cursor.execute(update_query, data)
    connection.commit()
    return "Done"
    