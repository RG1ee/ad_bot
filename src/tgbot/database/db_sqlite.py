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

        self.connect.execute(
            """
            CREATE TABLE IF NOT EXISTS cart (
                user_id INTEGER,
                product TEXT,
                currency INTEGER,
                FOREIGN KEY(user_id) REFERENCES users(telegram_id) ON UPDATE CASCADE
            );
            """
        )

        self.connect.execute(
            """
            CREATE TABLE IF NOT EXISTS paidOrders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_form INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                date TIMESTAMP NOT NULL,
                posted BOOL,
                services TEXT,
                FOREIGN KEY(id_form) REFERENCES forms(id) ON UPDATE CASCADE,
                FOREIGN KEY(user_id) REFERENCES users(telegram_id) ON UPDATE CASCADE
            );
            """
        )

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

    def update_from(self, data: dict) -> None:
        self.cursor.execute(
            """
            UPDATE forms SET
            company_name = (?),
            company_discription = (?),
            responsibilities = (?),
            requirements = (?),
            terms = (?),
            contact_link = (?)
            WHERE user_forms = (?);
            """, (
                data["company_name"], data["company_discription"],
                data["responsibilities"], data["requirements"], data["terms"],
                data["contact_link"], data["user_forms"]
            )
        )
        self.connect.commit()

    def select_form(self, username_id) -> list[Any]:
        return self.cursor.execute(
            """
            SELECT * FROM forms
            WHERE user_forms = ?;
            """, (username_id,)
        ).fetchall()

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

    def select_service_with_key(self, name_service: str) -> list[Any]:
        return self.cursor.execute(
            """
            SELECT * FROM services WHERE name_service = ?;
            """, (name_service,)
        ).fetchall()

    def select_package_with_key(self, name_package: str) -> list[Any]:
        return self.cursor.execute(
            """
            SELECT * FROM servicePackages WHERE name_packege = ?;
            """, (name_package,)
        ).fetchall()


    def select_products_from_cart(self, username_id) -> list[Any]:
        return self.cursor.execute(
            """
            SELECT * FROM cart
            WHERE user_id = ?;
            """, (username_id,)
        ).fetchall()

    def add_product_to_cart(self, username_id: int, data: list[Any]) -> None:
        self.cursor.execute(
            """
            INSERT INTO cart VALUES (?, ?, ?);
            """, (username_id, data[0], data[-1])
        )

        self.connect.commit()

    def check_product_in_cart(self, username_id: int) -> list[Any]:
        return self.cursor.execute(
            """
            SELECT product, currency FROM cart
            WHERE user_id == ?;
            """, (username_id,)
        ).fetchall()

    def clear_cart(self, username_id: int) -> None:
        self.cursor.execute(
            """
            DELETE FROM cart WHERE user_id == ?;
            """, (username_id,)
        )

        self.connect.commit()

    def add_to_paid_orders(self, data: dict):
        self.cursor.execute(
            """
            INSERT INTO paidOrders VALUES (
                ?, ?, ?, ?, ?, ?
            );
            """, (None, data["id_form"], data["user_id"], data["date"], 0, data["services"])
        )

        self.connect.commit()

    def select_all_paid_orders(self) -> list[Any]:
        return self.cursor.execute(
            """
            SELECT * FROM paidOrders
            WHERE posted = FALSE;
            """
        ).fetchall()

    def select_paid_orders_by_id(self, id) -> list[Any]:
        return self.cursor.execute(
            """
            SELECT * FROM paidOrders
            WHERE id = ?;
            """, (id,)
        ).fetchall()

    def confirm_paid_orders(self, user_id: int, id: int) -> None:
        self.cursor.execute(
            """
            UPDATE paidOrders SET posted = True
            WHERE user_id = ? AND id = ?;
            """, (user_id, id)
        )

        self.connect.commit()
