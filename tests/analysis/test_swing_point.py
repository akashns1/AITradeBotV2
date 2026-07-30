from aitradebot.analysis.swing_detector import (
    SwingAnalysis,
    SwingDetector,
    SwingPoint,
)

def test_creates_swing_point():
    point = SwingPoint(
        index=2,
        price=108,
    )

    assert point.index == 2
    assert point.price == 108

def test_swing_analysis_contains_swing_points():
        analysis = SwingAnalysis(
        swing_highs=[
            SwingPoint(index=2, price=108),
        ],
        swing_lows=[
            SwingPoint(index=5, price=95),
        ],
    )

        assert len(analysis.swing_highs) == 1
        assert len(analysis.swing_lows) == 1

        assert analysis.swing_highs[0].price == 108
        assert analysis.swing_lows[0].price == 95
def test_returns_latest_high():
    analysis = SwingAnalysis(
        swing_highs=[
            SwingPoint(index=2, price=108),
            SwingPoint(index=6, price=112),
        ],
        swing_lows=[],
    )

    assert analysis.latest_high.index == 6
    assert analysis.latest_high.price == 112


def test_returns_previous_high():
    analysis = SwingAnalysis(
        swing_highs=[
            SwingPoint(index=2, price=108),
            SwingPoint(index=6, price=112),
        ],
        swing_lows=[],
    )

    assert analysis.previous_high.index == 2
    assert analysis.previous_high.price == 108