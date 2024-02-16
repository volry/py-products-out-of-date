from contextlib import contextmanager
import datetime
from unittest.mock import patch

@contextmanager
def mock_datetime_today(mock_date):
    class DateSubclass(datetime.date):
        @classmethod
        def today(cls):
            return mock_date

    with patch('datetime.date', DateSubclass):
        yield

from app.main import outdated_products  # Adjust the import path as necessary

def test_outdated_products_with_mock():
    mock_today = datetime.date(2022, 2, 2)
    with mock_datetime_today(mock_today):
        products = [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 2, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 2, 5),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2022, 2, 1),
                "price": 160
            }
        ]
        assert outdated_products(products) == ['duck']
