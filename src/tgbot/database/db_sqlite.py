from typing import Any
import sqlite3 as sq

from settings.const import DB_NAME


class DataBaseHelper:
    def __init__(self):
        self.dbname = DB_NAME
        self.connect = sq.connect(self.dbname)
        self.cursor = self.connect.cursor()

    @property
    def setup_table(self) -> None:
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

        self.connect.execute(
            """
            CREATE TABLE IF NOT EXISTS services (
                name_service TEXT PRIMARY KEY,
                service_discription TEXT,
                link_channel TEXT,
                services_price INTEGER
            );
            """
        )

        self.connect.execute(
            """
            CREATE TABLE IF NOT EXISTS servicePackages (
                name_packege TEXT PRIMARY KEY,
                package_discription TEXT,
                packege_price INTEGER
            );
            """
        )

        # TODO finish the table with paid services
        # self.connect.execute(
        #     """
        #     CREATE TABLE IF NOT EXISTS paidOrders (
        #         id INTEGER PRIMARY KEY AUTOINCREMENT,
        #         id_form INTEGER NOT NULL,
        #         user_id INTEGER NOT NULL,
        #         price INTEGER NOT NULL,
        #         date TIMESTAMP NOT NULL,
        #         posted BOOL,
        #         FOREIGN KEY(id_form) REFERENCES forms(id) ON UPDATE CASCADE,
        #         FOREIGN KEY(user_id) REFERENCES users(telegram_id) ON UPDATE CASCADE
        #     );
        #     """
        # )

        self.connect.commit()

    def insert_user(self, username_id: int) -> None:
        self.cursor.execute(
            """
            INSERT OR IGNORE INTO users VALUES (?, ?, ?);
            """, (None, username_id, 1)
        )
        self.connect.commit()

    def insert_from(self, data: dict) -> None:
        self.cursor.execute(
            """
            INSERT INTO forms VALUES (?, ?, ?, ?, ?, ?, ?, ?);
            """, (
                None, data["company_name"], data["company_discription"],
                data["responsibilities"], data["requirements"], data["terms"],
                data["contact_link"], data["user_forms"]
            )
        )
        self.connect.commit()

    def select_all_services(self) -> list[Any]:
        return self.cursor.execute(
            """
            SELECT name_service, services_price, link_channel FROM services;
            """
        ).fetchall()

    def select_all_packeges(self) -> list[Any]:
        return self.cursor.execute(
            """
            SELECT name_packege, packege_price, package_discription FROM servicePackages;
            """
        ).fetchall()

    def select_service_with_key(self, service) -> list[Any]:
        return self.cursor.execute(
            f"""
            SELECT * FROM services WHERE name_service == "{str(service)}";
            """
        ).fetchall()
