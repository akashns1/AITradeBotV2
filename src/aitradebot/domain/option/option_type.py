from enum import Enum


class OptionType(str, Enum):
    CALL = "CALL"
    PUT = "PUT"