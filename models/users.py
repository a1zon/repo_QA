
from dataclasses import dataclass 
from enum import Enum

USER_ADULT_AGE = 18

class Status(Enum):
    STUDENT = "student"
    WORKER = "worker"

@dataclass
class User : 
    
    name : str
    age: int  
    status : Status  
    items: list[str]

    def is_adult(self)->bool: 
        return self.age >= USER_ADULT_AGE

    # def __innit__(self,name,age,status,items):
    #     self.age = age 
    #     self.name = name 
    #     self.items = items 
    #     self.status = status