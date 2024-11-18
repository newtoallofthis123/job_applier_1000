from helpers.file import get_db_path
import sqlite3


class Db:
    def __init__(self):
        self.db_path = get_db_path()
        self.conn = self.connect_db()

    def connect_db(self):
        return sqlite3.connect(self.db_path)

    def close_db(self):
        self.conn.close()
