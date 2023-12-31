import enum

from pydantic import BaseModel


class ApiSourceName(str, enum.Enum):
    yandex = 'YANDEX'
    other = 'Другой'


class ApiSource(BaseModel):
    id: int
    name: str
    type: str
    url: str
    header_key: str


class RequestCreateApiSource(BaseModel):
    name: str
    type: str
    url: str
    header_key: str


class ResponseCreateApiSource(BaseModel):
    name: str
    type: str
    url: str
    header_key: str
