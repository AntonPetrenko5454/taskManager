class User:
    def __init__(self,id,nickname,password,status,conditionAcc):
        self.id=id
        self.nickname=nickname
        self.password=password
        self.status=status
        self.conditionAcc=conditionAcc
    def __str__(self):
        return f'{self.id} {self.nickname} {self.password} {self.status} {self.conditionAcc}'