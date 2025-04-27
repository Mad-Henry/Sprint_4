import pytest
from main import BooksCollector

@pytest.fixture
def empty_collector():
    empty_collector = BooksCollector()
    return empty_collector

