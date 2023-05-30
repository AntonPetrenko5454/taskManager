import pref
import pymysql

class TaskController:
    host = pref.host
    user = pref.user
    passwd = pref.passwd
    db = pref.db

    @staticmethod
    def add_new_task(service, name, text, date, address, price, customer, creation_date, status):
        connection = pymysql.connect(host=TaskController.host,
                                     user=TaskController.user,
                                     passwd=TaskController.passwd,
                                     db=TaskController.db)
        with connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO task (service, name, description, deadline, address, price, customer, creation_date, status) '
                           'VALUES (%s, %s, %s, %s, %s ,%s, %s, %s, %s)',
                           (service, name, text, date, address, price, str(customer),creation_date,status))
            connection.commit()

    @staticmethod
    def find_user_tasks(customer):
        connection = pymysql.connect(host=TaskController.host,
                                     user=TaskController.user,
                                     passwd=TaskController.passwd,
                                     db=TaskController.db)
        with connection:
            cursor = connection.cursor()
            cursor.execute('SELECT task.id, task.name, creation_date, execution_date, deadline, price, status, address, file, description, customer, executor, service.name '
                           'FROM task '
                           'INNER JOIN service '
                           'ON service.id = task.service '
                           'WHERE customer = %s ',
                           (customer,))
            row = cursor.fetchall()
            return row