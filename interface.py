from abc import ABC

from type import KEY, VALUE, SECOND


class
    (ABC):

    def SET(self, key: KEY, value: VALUE):
        ...

    def GET(self, key: KEY):
        ...

    def DELETE(self, key: KEY):
        ...

    def EXPIRE(self, key: KEY, second: SECOND):
        ...

    def TTL(self, key: KEY):
        ...

