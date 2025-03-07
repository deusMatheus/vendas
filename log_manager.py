import datetime
from db_manager import db_manager as db

class Log_manager:

    def create_log(self, tableName, workerId, operationDescription):
        datetimeString = datetime.datetime.now()
        date = datetimeString.strftime('%d/%m/%Y')
        time = datetimeString.strftime('%H:%M:%S')
        db().insertValues('log', [f'("{date}", "{time}", "{tableName}", "{workerId}", "{operationDescription}")'])