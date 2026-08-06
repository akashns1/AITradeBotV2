"""
instrument_repository.py

Loads the Dhan instrument master and provides
fast lookup for tradable instruments.
"""

from pathlib import Path

import pandas as pd
from dhanhq import MarketFeed

from aitradebot.infrastructure.dhan.instrument import BrokerInstrument


MARKET_FEED_SEGMENT_MAP = {
    "I": MarketFeed.IDX,
    "N": MarketFeed.NSE,
    "D": MarketFeed.NSE_FNO,
}

REST_SEGMENT_MAP = {
    "I": "IDX_I",
    "N": "NSE_EQ",
    "D": "NSE_FNO",
}


class InstrumentRepository:
    """
    Repository for looking up broker instruments
    from the Dhan Security Master.
    """

    def __init__(self) -> None:

        csv_path = Path("data/api-scrip-master-detailed.csv")

        self.df = pd.read_csv(
            csv_path,
            low_memory=False,
        )

        print(
            f"Loaded {len(self.df)} instruments."
        )

    # ==================================================
    # Underlying Lookup
    # ==================================================

    def find_underlying(
        self,
        underlying: str,
    ) -> pd.DataFrame:

        underlying = underlying.upper()

        if underlying == "NIFTY":

            return self.df[
                (self.df["DISPLAY_NAME"].str.upper() == "NIFTY 50")
                &
                (self.df["SEGMENT"] == "I")
            ]

        raise ValueError(
            f"Unsupported underlying: {underlying}"
        )

    # --------------------------------------------------

    def get_underlying(
        self,
        underlying: str,
    ) -> BrokerInstrument | None:

        result = self.find_underlying(
            underlying,
        )

        if result.empty:
            return None

        row = result.iloc[0]

        return BrokerInstrument(
            security_id=str(row["SECURITY_ID"]),
            market_feed_segment=MARKET_FEED_SEGMENT_MAP[row["SEGMENT"]],
            rest_segment=REST_SEGMENT_MAP[row["SEGMENT"]],
            instrument_type=row["INSTRUMENT_TYPE"],
            symbol=row["DISPLAY_NAME"],
        )

    # ==================================================
    # Option Lookup
    # ==================================================

    def find_option(
        self,
        underlying: str,
        strike: int,
        option_type: str,
        expiry_date: str | None = None,
    ) -> pd.DataFrame:

        result = self.df[
            (self.df["UNDERLYING_SYMBOL"] == underlying)
            &
            (self.df["STRIKE_PRICE"] == strike)
            &
            (self.df["OPTION_TYPE"] == option_type)
        ]

        if expiry_date is not None:

            result = result[
                result["SM_EXPIRY_DATE"] == expiry_date
            ]

        return result

    # --------------------------------------------------

    def get_option(
        self,
        underlying: str,
        strike: int,
        option_type: str,
        expiry_date: str | None = None,
    ) -> BrokerInstrument | None:

        result = self.find_option(
            underlying=underlying,
            strike=strike,
            option_type=option_type,
            expiry_date=expiry_date,
        )

        if result.empty:
            return None

        row = result.iloc[0]

        return BrokerInstrument(
            security_id=str(row["SECURITY_ID"]),
            market_feed_segment=MARKET_FEED_SEGMENT_MAP[row["SEGMENT"]],
            rest_segment=REST_SEGMENT_MAP[row["SEGMENT"]],
            instrument_type=row["INSTRUMENT_TYPE"],
            symbol=row["DISPLAY_NAME"],
        )