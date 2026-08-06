"""
Live Dhan Market Feed Wrapper
"""

import logging

from dhanhq import DhanContext, MarketFeed

from aitradebot.config import (
    CLIENT_ID,
    ACCESS_TOKEN,
)

logger = logging.getLogger(__name__)

MARKET_FEED_VERSION = "v2"


class LiveFeed:
    """
    Wrapper around Dhan MarketFeed.
    """

    def __init__(self, on_ticks_callback):

        if not callable(on_ticks_callback):
            raise ValueError(
                "on_ticks_callback must be callable"
            )
        print("Calling callback...")
        self.on_ticks_callback = on_ticks_callback
        print("Callback finished.")
        self.instruments = []

        self.context = DhanContext(
            CLIENT_ID,
            ACCESS_TOKEN,
        )

        self.feed = None

    # --------------------------------------------------------

    def connect(self, contracts):

        if self.feed is not None:
            logger.warning(
                "Market Feed is already connected."
            )
            return

        # Accept single contract or list
        if not isinstance(contracts, (list, tuple)):
            contracts = [contracts]

        self.instruments = []

        for contract in contracts:

            self.instruments.append(
                (
                    contract.market_feed_segment,
                    str(contract.security_id),
                )
            )

        logger.info(
            "Connecting to Market Feed : %s",
            self.instruments,
        )

        print("\n========== SUBSCRIPTIONS ==========")
        print(self.instruments)
        print("==================================")

        self.feed = MarketFeed(
            dhan_context=self.context,
            instruments=self.instruments,
            version=MARKET_FEED_VERSION,
            on_connect=self._on_connect,
            on_ticks=self._on_ticks,
            on_close=self._on_close,
            on_error=self._on_error,
        )

        print("MarketFeed created")
        print("Calling run()...")

        try:
            self.feed.run()

        except Exception:
            logger.exception(
                "Market Feed crashed"
            )
            raise

    # --------------------------------------------------------

    def disconnect(self):

        if self.feed is None:
            return

        logger.info(
            "Disconnecting Market Feed"
        )

        self.feed.close_connection()
        self.feed = None

    # --------------------------------------------------------

    def subscribe(self, instruments):

        new = [
            instrument
            for instrument in instruments
            if instrument not in self.instruments
        ]

        if not new:
            return

        self.instruments.extend(new)

        if self.feed:
            self.feed.subscribe_symbols(new)

    # --------------------------------------------------------

    def unsubscribe(self, instruments):

        self.instruments = [
            instrument
            for instrument in self.instruments
            if instrument not in instruments
        ]

        if self.feed:
            self.feed.unsubscribe_symbols(
                instruments
            )

    # --------------------------------------------------------

    def _on_ticks(self, feed, ticks):

        try:

            print("\n========== TICKS RECEIVED ==========")
            print("Type :", type(ticks))

            if isinstance(ticks, list):

                print("Count:", len(ticks))

                if ticks:
                    print("First Tick:", ticks[0])

            else:
                print(ticks)

            print("====================================")

            self.on_ticks_callback(
                ticks,
            )

        except Exception as ex:

            logger.exception(
                "Error while processing ticks"
            )

            print("\n========== CALLBACK ERROR ==========")
            print(type(ex).__name__)
            print(ex)
            print("====================================")

            raise

    # --------------------------------------------------------

    @staticmethod
    def _on_connect(ws):

        logger.info(
            "Market Feed Connected"
        )

    # --------------------------------------------------------

    @staticmethod
    def _on_close(ws):

        logger.info(
            "Market Feed Closed"
        )

    # --------------------------------------------------------

    @staticmethod
    def _on_error(ws, error):

        logger.exception(
            "Market Feed Error"
        )
        logger.exception(error)