from dataclasses import dataclass
from dataclasses import dataclass


@dataclass(frozen=True)
class SwingPoint:
    index: int
    price: float

@dataclass(frozen=True)
class SwingAnalysis:
    swing_highs: list[SwingPoint]
    swing_lows: list[SwingPoint]

    @property
    def latest_high(self) -> SwingPoint | None:
        if not self.swing_highs:
            return None
        return self.swing_highs[-1]

    @property
    def previous_high(self) -> SwingPoint | None:
        if len(self.swing_highs) < 2:
            return None
        return self.swing_highs[-2]

    @property
    def latest_low(self) -> SwingPoint | None:
        if not self.swing_lows:
            return None
        return self.swing_lows[-1]


    @property
    def previous_low(self) -> SwingPoint | None:
        if len(self.swing_lows) < 2:
            return None
        return self.swing_lows[-2]

class SwingDetector:
    def analyze(self, candles):
        swing_highs = []
        swing_lows = []

        for i in range(1, len(candles) - 1):
            if self._is_swing_high(candles, i):
                swing_highs.append(
                    SwingPoint(
                    index=i,
                    price=candles[i].high,
                )
            )
            if self._is_swing_low(candles, i):
                swing_lows.append(
                    SwingPoint(
                    index=i,
                    price=candles[i].low,
                )
            )

        return SwingAnalysis(
            swing_highs=swing_highs,
            swing_lows=swing_lows,
        )
    
    def _is_swing_high(self, candles, index):
        return (
            candles[index].high > candles[index - 1].high
            and candles[index].high > candles[index + 1].high
        )
    def _is_swing_low(self, candles, index):
        return (
            candles[index].low < candles[index - 1].low
            and candles[index].low < candles[index + 1].low
        )
    