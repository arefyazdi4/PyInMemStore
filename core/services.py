from typing import Union

from core.interfaces import InMemStore
from core.types import KEY, SECOND, VALUE


class HashInMemStore(InMemStore):
    def __init__(self):
        self.__store = dict()

    def SET(self, key: KEY, value: VALUE):
        self.__raise_if_key_is_null(key)
        self.__rase_if_key_type_is_invalid(key)
        self.__store[key] = value

    def GET(self, key: KEY) -> Union[VALUE, None]:
        try:
            return self.__store[key]
        except KeyError:
            return None

    def DELETE(self, key: KEY):
        try:
            self.__store.__delitem__(key)
        except KeyError:
            raise InMemStore.KeyNotFound()

    def EXPIRE(self, key: KEY, second: SECOND):
        ...

    def TTL(self, key: KEY) -> SECOND:
        ...

    def __raise_if_key_is_null(self, key):
        if key is None:
            raise InMemStore.InvalidKeyError('key cannot be empty')

    def __rase_if_key_type_is_invalid(self, key):
        if type(key) is not KEY:
            raise InMemStore.InvalidKeyError(f'key type must be {type(KEY)}')
