import pymysql

from exceptions import DuplicateNicknameException


class UserController:
    host = 'localhost'
    user = 'root'
    passwd = '5454Anton5454'
    db = 'taskmanager_db'

    @staticmethod
    def AddNewUser(id, nickname, password, fullname=None, email=None, phone=None):
        connection = pymysql.connect(host=UserController.host,
                                     user=UserController.user,
                                     passwd=UserController.passwd,
                                     db=UserController.db)
        with connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM user WHERE nickname=%s', nickname)
            row = cursor.fetchone()
            if row:
                raise DuplicateNicknameException()
            else:
                cursor.execute('INSERT INTO user (id, nickname, password, fullname, email, phone, status) '
                               'VALUES (%s, %s, %s, %s, %s, %s, %s)',
                               (id, nickname, password, fullname, email, phone, 'active'))
                connection.commit()

    @staticmethod
    def IsNicknameFree(nickname):
        connection = pymysql.connect(host=UserController.host,
                                     user=UserController.user,
                                     passwd=UserController.passwd,
                                     db=UserController.db)
        with connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM user WHERE nickname=%s', nickname)
            row = cursor.fetchone()
            if row is None:
                return False
            else:
                return True

    @staticmethod
    def HasUser(id):
        connection = pymysql.connect(host=UserController.host,
                                     user=UserController.user,
                                     passwd=UserController.passwd,
                                     db=UserController.db)
        with connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM user WHERE id=%s', id)
            row = cursor.fetchone()
            if row is None:
                return False
            else:
                return True

    @staticmethod
    def Authorization(id, password):
        # TODO: Реализация функции
        pass
