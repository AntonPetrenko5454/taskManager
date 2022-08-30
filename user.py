class User:
    def __init__(self,id,nickname,password):
        self.id=id
        self.nickname=nickname
        self.password=password
    def __str__(self):
        return f'{self.id} {self.nickname} {self.password}'