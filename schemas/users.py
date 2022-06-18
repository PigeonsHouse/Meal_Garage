from pydantic import BaseModel


class SignUpPayload(BaseModel):
    name: str
    email: str
    password: str


class SignInPayload(BaseModel):
    email: str
    password: str


class User(BaseModel):
    user_id: str
    email: str
    name: str

    class Config:
        orm_mode = True


class AuthInfo(BaseModel):
    jwt: str
