import random

import pytest

from core.interfaces import InMemStore
from core.services import HashInMemStore
from core.types import KEY, VALUE


def mock_key() -> KEY:
    return str(random.randint(0, 100))


def mock_value() -> VALUE:
    return str(random.randint(0, 100))


@pytest.fixture(scope="function")
def cache() -> InMemStore:
    return HashInMemStore()


class TestSetHashInMemStore:

    def test_rise_error_if_key_is_null(self, cache: InMemStore):
        null_key = None
        with pytest.raises(InMemStore.InvalidKeyError):
            cache.SET(key=null_key, value=mock_value())

    def test_rise_error_if_key_is_not_valid(self, cache: InMemStore):
        invalid_key = int()
        with pytest.raises(InMemStore.InvalidKeyError):
            cache.SET(key=invalid_key, value=mock_value())

    def test_can_set_if_key_is_duplicate(self, cache: InMemStore):
        key = mock_key()
        cache.SET(key=key, value=mock_value())
        cache.SET(key=key, value=mock_value())


class TestGetHashInMemStore:
    def test_get_value(self, cache: InMemStore):
        key = mock_key()
        value = mock_value()
        cache.SET(key=key, value=value)

        result = cache.GET(key=key)

        assert result == value

    def test_over_write_value_if_key_is_duplicate(self, cache: InMemStore):
        key = mock_key()
        cache.SET(key=key, value=mock_value())
        value = mock_value()
        cache.SET(key=key, value=value)

        result = cache.GET(key=key)

        assert result == value

    def test_return_null_if_key_not_exist(self, cache: InMemStore):
        result = cache.GET(key=mock_key())

        assert result is None


class TestDeleteHashInMemStore:
    def test_raise_error_if_key_not_found(self, cache: InMemStore):
        with pytest.raises(InMemStore.KeyNotFound):
            cache.DELETE(key=mock_key())

    def test_remove_key_successfully(self, cache: InMemStore):
        key = mock_key()
        cache.SET(key=key, value=mock_value())
        cache.DELETE(key=key)

