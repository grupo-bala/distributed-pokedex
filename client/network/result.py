from dataclasses import dataclass
from typing import Literal

ResultStatus = Literal[
    "Ok",
    "Error"
]

@dataclass
class Result:
    status: ResultStatus
    result: str
