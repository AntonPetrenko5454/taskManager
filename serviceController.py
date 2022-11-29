import pymysql

import pref
from exceptions import DuplicateNicknameException


class ServiceController:
    host = pref.host
    user = pref.user
    passwd = pref.passwd
    db = pref.db

    @staticmethod
    def GetServices():
        connection = pymysql.connect(host=ServiceController.host,
                                     user=ServiceController.user,
                                     passwd=ServiceController.passwd,
                                     db=ServiceController.db)
        with connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM service')
            row = cursor.fetchall()
            return row
