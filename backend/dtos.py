from pydantic import BaseModel
class UserDTO(BaseModel):
    name: str = None
    email: str
    password: str
class createUserDTO(BaseModel):
    name: str
    email: str
    password: str
class bookingDTO(BaseModel):
    ID: str