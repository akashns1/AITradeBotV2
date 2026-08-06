from datetime import datetime, time


class ActiveSessionFilter:

    FIRST_START = time(9, 15)
    FIRST_END = time(11, 0)

    SECOND_START = time(13, 30)
    SECOND_END = time(15, 0)

    def is_active(
        self,
        now: datetime,
    ) -> bool:

        current = now.time()

        first_session = (
            self.FIRST_START <= current < self.FIRST_END
        )

        second_session = (
            self.SECOND_START <= current < self.SECOND_END
        )

        return first_session or second_session