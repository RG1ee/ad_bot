import sqlite3 as sq

from settings.const import DB_NAME


class DataBaseHelper:
    def __init__(self):
        self.dbname = DB_NAME
        self.connect = sq.connect(self.dbname)
        self.cursor = self.connect.cursor()

    @property
    def setup_table(self):
        self.connect.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                telegram_id INTEGER NOT NULL UNIQUE,
                is_active BOOL NOT NULL
            );
            """
        )

        self.connect.execute(
            """
            CREATE TABLE IF NOT EXISTS forms (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                company_name TEXT,
                company_discription TEXT,
                responsibilities TEXT,
                requirements TEXT,
                terms TEXT,
                contact_link TEXT,
                user_forms INTEGER NOT NULL,
                FOREIGN KEY(user_forms) REFERENCES users(telegram_id) ON UPDATE CASCADE
            );
            """
        )
        self.connect.commit()

    def insert_user(self, username_id: int):
        self.cursor.execute(
            """
            INSERT OR IGNORE INTO users VALUES (?, ?, ?)
            """, (None, username_id, 1)
        )
        self.connect.commit()

    def insert_from(self, data: dict):
        self.cursor.execute(
            """
            INSERT INTO forms VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                None, data["company_name"], data["company_discription"],
                data["responsibilities"], data["requirements"], data["terms"],
                data["contact_link"], data["user_forms"]
            )
        )
        self.connect.commit()
