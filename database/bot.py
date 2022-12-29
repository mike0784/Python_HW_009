import re
from readingForm import readingForm
from database import operationBD
import logging
class Bot():
    mode = 0
    lst = []
    step = 0
    def __init__(self, struct, database):
        self.database = database
        self.struct = struct

        self.log = logging.getLogger(__name__)
        self.log.setLevel(logging.INFO)

        handler = logging.FileHandler(f"{__name__}.log", mode="w")
        formatter = logging.Formatter("%(name)s : %(asctime)s %(levelname)s %(message)s")

        handler.setFormatter(formatter)
        self.log.addHandler(handler)
        self.log.info("Create example class Bot")

    def inputText(self, text):
        self.log.info("Text processing: " + text)
        text = text.upper()
        arr = list(text.split())

        pattern1 = ["ВСТАВИТЬ", "СОЗДАТЬ", "ЗАПИСАТЬ", "ЗАПИШИ", "ЗАПИСЬ"]
        pattern2 = ["РЕДАКТИРОВАТЬ", "ОТРЕДАКТИРОВАТЬ", "ОБНОВИТЬ"]
        pattern3 = ["УДАЛИТЬ", "СТЕРЕТЬ"]
        pattern4 = ["ПРОЧИТАТЬ", "ВЫВЕСТИ"]
        pattern5 = ["ЭКСПОРТ", "ЭКСПОРТИРОВАТЬ"]
        pattern6 = ["ИМПОРТ", "ИМПОРТИРОВАТЬ"]
        if self.mode == 0:
            for i in range(0, len(arr)):
                for patItem in pattern1:
                    if arr[i] == patItem:
                        return self.insert(arr, i)
                for patItem in pattern2:
                    if arr[i] == patItem:
                        return self.update(arr, i)
                for patItem in pattern3:
                    if arr[i] == patItem:
                        return self.delete(arr, i)
                for patItem in pattern4:
                    if arr[i] == patItem:
                        return self.select(arr, i)
                for patItem in pattern5:
                    if arr[i] == patItem:
                        return self.exportCSV()
                for patItem in pattern6:
                    if arr[i] == patItem:
                        return self.importCSV()
        return "БОТ: Ты что хочешь от меня?"

    def insert(self, arr, i):
        print(arr, arr[i])
        lst = {"surname" : arr[i+1].capitalize(), "name" : arr[i + 2].capitalize(), "patronymic" : arr[i + 3].capitalize(), "phone" : arr[i + 4]}
        bd = operationBD(self.database)
        bd.insertRecord(lst)
        del bd
        return f"БОТ: Запись произведена"

    def update(self, arr, i):
        form = readingForm(self.struct, self.database, int(arr[i + 1]))
        return "Обновление"

    def delete(self, arr, i):
        bd = operationBD(self.database)
        bd.deleteRecord(int(arr[i + 1]))
        del bd
        return "БОТ: Удаление завершено"

    def select(self):
        return "Чтение"

    def exportCSV(self):
        fields = list(self.struct.keys())
        del fields[0]
        bd = operationBD(self.database)
        lst = {}
        lst = bd.selectRecord()
        del bd

        result = {}
        i = 1
        for row in lst:
            text = list(row)
            del text[0]
            ss = dict(zip(fields, text))
            result[i] = ss
            i = i + 1

        from settings import csvFile
        import csv
        with open(csvFile, 'w', newline = '') as csv_file:
            writer = csv.DictWriter(csv_file, delimiter=';', fieldnames=fields)
            writer.writeheader()
            for row in result:
                writer.writerow(result[row])
        return "БОТ: экспорт данных завершен"

    def importCSV(self):
        from settings import csvFile
        import csv
        result = {}
        bd = operationBD(self.database)
        with open(csvFile, 'r', newline='', encoding='cp1251') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=';', quotechar='|')
            for row in reader:
                bd.insertRecord(row)
        del bd
        return "БОТ: импорт данных завершен"