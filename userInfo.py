class UserInfo:
    def __init__(self, id, nickname, password, urInfo, capabilities):
        self.id = id
        self.nickname = nickname
        self.password = password
        self.urInfo = urInfo
        self.capabilities = capabilities

    def __str__(self):
        return f'{self.id} {self.nickname} {self.password} {self.status}'
