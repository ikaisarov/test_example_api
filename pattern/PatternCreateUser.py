from pydantic import BaseModel


class NewUser:

    def __init__(self, name, job):
        self.name = name
        self.job = job

    def getNewUser(self):
        return {"name": self.name, "job": self.job}


class PatternNewUser(BaseModel):
    createdAt: str
    id: int
    job: str
    name: str


class PatternUpdateUser(BaseModel):
    updatedAt: str
    job: str
    name: str
