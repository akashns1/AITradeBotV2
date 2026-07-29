from enum import StrEnum


class TimeFrame(StrEnum):
    ONE_MINUTE = "1m"
    TWO_MINUTES = "2m"
    THREE_MINUTES = "3m"
    FIVE_MINUTES = "5m"
    TEN_MINUTES = "10m"
    FIFTEEN_MINUTES = "15m"
    THIRTY_MINUTES = "30m"
    ONE_HOUR = "1h"
    ONE_DAY = "1d"

    @property
    def minutes(self) -> int:
        mapping = {
            TimeFrame.ONE_MINUTE: 1,
            TimeFrame.TWO_MINUTES: 2,
            TimeFrame.FIVE_MINUTES: 5,
        }

        return mapping[self]
