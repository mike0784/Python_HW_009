from tkinter import *
from tkinter import ttk
from functools import partial
from database import operationBD
import logging
from bot import Bot

class mainWindow:
    row = 1
    columnTableFrame = 0
    rowTableFrame = 0
    def __init__(self, struct, database):
        self.dbName = database
        self.bd = operationBD(database)
        self.struct = struct
        self.bot = Bot(struct, database)
        self.buildWindow()

        log = logging.getLogger(__name__)
        log.setLevel(logging.INFO)

        handler = logging.FileHandler(f"{__name__}.log", mode="w")
        formatter = logging.Formatter("%(name)s : %(asctime)s %(levelname)s %(message)s")

        handler.setFormatter(formatter)
        log.addHandler(handler)
        log.info("Create example class mainWindow")


    def buildWindow(self):
        self.window = Tk()
        self.window.title("Телефонный справочник")
        self.window.geometry('1300x400')
        ss = self.tableFrame()
        ss.grid(column=self.columnTableFrame, row=self.rowTableFrame, columnspan=3, padx=20, pady=2)

        self.ff = self.textPole()
        self.ff.grid(column=3, row=0, columnspan=3, padx=20, pady=2)

        self.window.mainloop()

    def tableFrame(self):
        bd = operationBD(self.dbName)
        lst = bd.selectRecord()
        del bd

        self.TableFrame = Frame(self.window, padx=20, pady=20)
        #Создание шапки таблицы
        mainTable = LabelFrame(self.TableFrame)
        coll = 0
        for item in self.struct:
            e = Label(mainTable, borderwidth=2, relief = "raised", width=10, fg='red', font=("Arial", 12, 'bold'), text=self.struct[item])
            e.grid(column = coll, row = 0)
            coll = coll + 1
        mainTable.grid(column=0, row=0)

        #Создание таблицы
        canvas = Canvas(self.TableFrame, width=535, height=200)
        scroll_y = ttk.Scrollbar(self.TableFrame, orient="vertical")
        scroll_y.config(command=canvas.yview)

        table = LabelFrame(canvas)
        table.grid(column=0, row=0)
        i = 0
        coll = 0
        rows = 0
        color = "white"
        for rows in range(len(lst)):
            for j in range(len(lst[0])):
                lb = Label(table, borderwidth=2, relief = "raised", width=10, text=lst[rows][j], fg='blue', font=("Arial", 12, 'bold'), bg=color, anchor="w")
                lb.grid(column=j, row=rows+1)
        canvas.create_window((0, 0), window=table)
        canvas.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scroll_y.set)
        canvas.grid(column=0, row=1)
        scroll_y.grid(column=1, row=1, sticky="ns")

        rows = rows + len(lst)
        return self.TableFrame

    def textPole(self):
        frame = Frame(self.window, padx=20, pady=20)
        self.text = Text(frame, width=50, height=20, bg="darkgreen", fg="white")
        scroll = Scrollbar(frame, command=self.text.yview, orient="vertical")
        self.text.config(yscrollcommand=scroll.set)
        self.text.grid(column=0, row=0)
        scroll.grid(column=1, row=0, sticky="ns")

        self.lineEdit = Entry(frame, width=50, font="Verdana 10")
        self.lineEdit.grid(column=0, row=1, columnspan = 1, pady=5)
        self.lineEdit.bind('<Return>', lambda event: self.eventTextPole(event, self.lineEdit.get()))
        return frame

    def eventTextPole(self, event, var):
        self.text.insert("end", "\nUSER: " + var)
        tt = self.bot.inputText(var)
        self.text.insert("end", "\n" + tt)
        self.lineEdit.delete(0, "end")

        self.reloadFrame()

    def reloadFrame(self):
        self.TableFrame.destroy()
        ss = self.tableFrame()
        ss.grid(column=self.columnTableFrame, row=self.rowTableFrame, columnspan=3, padx=20, pady=2)
