import requests
import pytest

from src.config.configuration import SERVICE_URL
from src.enums.global_enums   import GlobalErrorMessages


def test_get_post():
    '''
    Test POST method from and URL from configuration file.
    '''
    response = requests.get(url=SERVICE_URL)
    received_posts = response.json()

    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert len(received_posts) == 3, GlobalErrorMessages.WRONG_ELEM_COUNT.value
