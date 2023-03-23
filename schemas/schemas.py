from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id: Optional[str]
    name: str
    description: str
    
class User(BaseModel):
    id: Optional[str]
    username: str
    email: Optional[str]
    password: str
    