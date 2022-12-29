import sqlite3
from sqlite3 import Error
import logging

class operationBD:
    table = "table1"
    def __init__(self, database):
        self.database = database
        self.log = logging.getLogger(__name__)
        self.log.setLevel(logging.INFO)

        handler = logging.FileHandler(f"{__name__}.log", mode="a")
        formatter = logging.Formatter("%(name)s : %(asctime)s %(levelname)s %(message)s")

        handler.setFormatter(formatter)
        self.log.addHandler(handler)
        self.log.info("Create example class operationBD")

    def run_query(self, query):
        with sqlite3.connect(self.database) as conn:
            c = conn.cursor()
            try:
                result = c.execute(query)
                conn.commit()
                c.close()
                return result
            except Error as e:
                print(e)

    def run_select(self, query):
        with sqlite3.connect(self.database) as conn:
            c = conn.cursor()
            try:
                c.execute(query)
                records = c.fetchall()
                c.close()
                return records
            except Error as e:
                print("Ошибка чтения БД: ", e)

    def create_table(self):
        sql_create_table = f"CREATE TABLE IF NOT EXISTS {operationBD.table} (id INTEGER PRIMARY KEY AUTOINCREMENT, surname TEXT, name TEXT, patronymic TEXT, phone TEXT)"
        result = self.run_query(sql_create_table)
        self.log.info("Create table")


    def selectRecord(self):
        sql_select_table = f"SELECT * FROM {operationBD.table}"
        self.log.info("select data base")
        return self.run_select(sql_select_table)


    def updateRecord(self, param):
        sql_update_table = f'UPDATE {operationBD.table} SET surname="{param["surname"]}", name="{param["name"]}", patronymic="{param["patronymic"]}", phone="{param["phone"]}" WHERE id={param["id"]}'
        self.run_query(sql_update_table)
        self.log.info("update " + str(param))

    def deleteRecord(self, param):
        sql_delete_table = f"DELETE FROM {operationBD.table} WHERE id={param}"
        self.run_query(sql_delete_table)
        self.log.info("delete " + str(param))

    def insertRecord(self, param):
        sql_insert_table = f'INSERT INTO {operationBD.table} ( surname, name, patronymic, phone ) VALUES ( "{param["surname"]}", "{param["name"]}", "{param["patronymic"]}", "{param["phone"]}" )'
        self.run_query(sql_insert_table)
        self.log.info("insert " + str(param))

    def selectRecordId(self, id):
        sql_query = f'SELECT * FROM {operationBD.table} WHERE id={id}'
        return self.run_select(sql_query)