from enum import Enum

class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE   = "Received status code is NOT expected. (Code 200)."
    WRONG_METHOD        = "Received method is not according to expected."