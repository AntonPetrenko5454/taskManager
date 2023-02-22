import pref
import pymysql

class TaskController:
    host = pref.host
    user = pref.user
    passwd = pref.passwd
    db = pref.db

    @staticmethod
    def add_new_task(criteria, name, text, date, price, address, customer):
        connection = pymysql.connect(host=TaskController.host,
                                     user=TaskController.user,
                                     passwd=TaskController.passwd,
                                     db=TaskController.db)
        with connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO task (criteria, name, text, date, price, address, customer)'
                           'VALUES (%s, %s, %s, %s, %s ,%s)'
                           (criteria, name, text, date, price, address, customer))
            connection.commit()