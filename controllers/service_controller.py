import pymysql
import pref


class ServiceController:
    host = pref.host
    user = pref.user
    passwd = pref.passwd
    db = pref.db

    @staticmethod
    def GetServices(parent=0):
        connection = pymysql.connect(host=ServiceController.host,
                                     user=ServiceController.user,
                                     passwd=ServiceController.passwd,
                                     db=ServiceController.db)
        with connection:
            cursor = connection.cursor()
            query = 'SELECT * FROM service WHERE ' + ('parent=%s' if parent != 0 else 'parent IS NULL')
            if parent == 0:
                cursor.execute(query)
            else:
                cursor.execute(query, parent)
            row = cursor.fetchall()
            return row


    @staticmethod
    def getServiceName(id):
        connection = pymysql.connect(host=ServiceController.host,
                                     user=ServiceController.user,
                                     passwd=ServiceController.passwd,
                                     db=ServiceController.db)
        with connection:
            cursor = connection.cursor()
            query = 'SELECT service.name FROM service WHERE id=%s'
            cursor.execute(query, id)
            row= cursor.fetchone()[0]
            if row is None:
                return 0
            return row


    @staticmethod
    def GetServiceParent(id):
        connection = pymysql.connect(host=ServiceController.host,
                                     user=ServiceController.user,
                                     passwd=ServiceController.passwd,
                                     db=ServiceController.db)
        with connection:
            cursor = connection.cursor()
            query = 'SELECT parent FROM service WHERE id=%s'
            cursor.execute(query, id)
            value = cursor.fetchone()[0]
            if value is None:
                return 0
            return value
