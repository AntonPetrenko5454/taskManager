class DuplicateNicknameException(Exception):
    def __str__(self):
        return 'Пользователь с таким nickname уже существует'