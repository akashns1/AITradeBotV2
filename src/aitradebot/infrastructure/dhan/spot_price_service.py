"""
Spot Price Service

Fetches the latest spot price from Dhan.
"""

from aitradebot.infrastructure.dhan.broker import Broker
from aitradebot.infrastructure.dhan.instrument import BrokerInstrument


class SpotPriceService:
    """
    Retrieves the latest spot price for a broker instrument.
    """

    def __init__(
        self,
        broker: Broker,
    ) -> None:

        self._broker = broker

    # ---------------------------------------------------------

    def get_price(
        self,
        instrument: BrokerInstrument,
    ) -> float:

        print("\n========== SPOT PRICE REQUEST ==========")
        print(f"Security ID      : {instrument.security_id}")
        print(f"REST Segment     : {instrument.rest_segment}")
        print("========================================")

        request = {
                instrument.rest_segment: [
                    int(instrument.security_id),
                ]
        }

        print("\nRequest:")
        print(request)

        response = self._broker.api.ticker_data(request)

        print("\nResponse:")
        print(response)

        # ------------------------------------------
        # Validate response
        # ------------------------------------------

        if not response:
            raise RuntimeError(
                "No response received from Dhan."
            )

        if response.get("status") != "success":
            raise RuntimeError(
                f"Dhan API returned failure: {response}"
            )

        if "data" not in response:
            raise RuntimeError(
                f"Unexpected response: {response}"
            )

        try:

            price = (
                response["data"]["data"]
                [instrument.rest_segment]
                [instrument.security_id]
                ["last_price"]
            )

        except (KeyError, TypeError) as ex:

            raise RuntimeError(
                f"Unable to extract spot price: {response}"
            ) from ex

        

        return float(price)