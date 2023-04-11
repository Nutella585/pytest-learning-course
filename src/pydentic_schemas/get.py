from pydantic import BaseModel, Field, validator

class Get(BaseModel):
    id          : int   = Field(le=2) # Built-in `pydantic` validation if `id` less-equal `2`.
    name        : str
    username    : str
    email       : str
    address     : object
    phone       : str
    website     : str
    company     : object

    # ----------------
    # Custom validation
    # ----------------
    # @validator("id")
    # def check_id_less_two(cls, v):
    #     if v > 2:
    #         raise ValueError('`id` is not less than two!')
    #     else: 
    #         return v

