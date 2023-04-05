from enum import Enum

class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Received status code is NOT expected. (Code 200)."
    WRONG_ELEM_COUNT = "Received not expected amount of data."