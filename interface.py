from abc import ABC
from typing import Union

from type import KEY, VALUE, SECOND


class InMemStore(ABC):

    def SET(self, key: KEY, value: VALUE):
        ...

    def GET(self, key: KEY) -> Union[VALUE, None]:
        ...

    def DELETE(self, key: KEY):
        ...

    def EXPIRE(self, key: KEY, second: SECOND):
        ...

    def TTL(self, key: KEY) -> SECOND:
        ...

    class BaseError(Exception):
        ...

    class InvalidKeyError(BaseError):
        ...

