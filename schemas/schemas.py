from pydantic import BaseModel
from typing import Optional
    
class User(BaseModel):
    id: Optional[str]
    username: str
    email: Optional[str]
    password: str
    
class Product(BaseModel):
    id: Optional[str]
    name: str
    description: str
    user_id: str
    