# Adding repo path to PYTHONPATH
import sys
sys.path.append("/Users/nutella585/repos/pytest-learninng-course")

# Built-in imports
import requests

# Custom imports
from src.base_classes.response  import Response
from src.schemas.get            import GET_SCHEMA
from src.config.configuration   import SERVICE_URL
from src.enums.enums_global     import GlobalErrorMessages


def test_method_get():
    '''
    Test simple GET overall method from dedicated URL.
    '''
    r = requests.get(url=SERVICE_URL)
    response = Response(r)

    response.assert_status_code(200)
    response.validate(GET_SCHEMA)