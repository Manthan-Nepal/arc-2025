from datetime import datetime
import json
from typing import Annotated
from pydantic import PlainSerializer, BaseModel

CustomDateTime = Annotated[
    datetime,
    PlainSerializer(lambda _datetime: _datetime.strftime("%Y/%M/%D, %H:%M:%S"), return_type=str),
]

class ExampleModel(BaseModel):
    custom_datetime: CustomDateTime

m = ExampleModel(custom_datetime= datetime.now())
print(m)

# with open("datetime.json", "w") as file:
#     json.dump(m, file, indent= 4)