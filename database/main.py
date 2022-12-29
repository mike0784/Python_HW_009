import csv
import os
from settings import *
from MainWindow import mainWindow
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

handler = logging.FileHandler(f"{__name__}.log", mode="w")
form = logging.Formatter("%(name)s : %(asctime)s %(levelname)s %(message)s")

handler.setFormatter(form)
log.addHandler(handler)

log.info(f"Testing the custom logger for module {__name__}...")
class application:
    def __init__(self):
        self.bd = operationBD(database)
        self.mWindow = mainWindow(struct)



if __name__ == "__main__":
    log.info("Call mainWindow")
    app = mainWindow(struct, database)


