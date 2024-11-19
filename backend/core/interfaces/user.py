from pydantic import BaseModel


class CreateUserDTO(BaseModel):
    username: str
    password: str


class LoginUserDTO(BaseModel):
    username: str
    password: str


class ResetPasswordDTO(BaseModel):
    username: str
    password: str


class UserDTO(BaseModel):
    id: int
    username: str
