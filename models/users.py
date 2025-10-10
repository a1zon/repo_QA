
from dataclasses import dataclass 

@dataclass
class User : 
    name : str
    age: int  
    status : str
    items: list[str]

    # def __innit__(self,name,age,status,items):
    #     self.age = age 
    #     self.name = name 
    #     self.items = items 
    #     self.status = status