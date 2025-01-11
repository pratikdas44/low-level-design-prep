import psycopg2
from models.DbInterface import DbInterface

class PostgresDb(DbInterface):
    def __init__(self, db_url, user, password, database):
        self.connection = psycopg2.connect(
            host=db_url,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def get(self, key):
        self.cursor.execute("SELECT value FROM cache_table WHERE key = %s", (key,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def put(self, key, value):
        self.cursor.execute("INSERT INTO cache_table (key, value) VALUES (%s, %s)", (key, value))
        self.connection.commit()

    def delete(self, key):
        self.cursor.execute("DELETE FROM cache_table WHERE key = %s", (key,))
        self.connection.commit()

    def __del__(self):
        self.cursor.close()
        self.connection.close()
