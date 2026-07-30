from aitradebot.analysis.market_structure_analyzer import MarketStructureAnalyzer
from aitradebot.analysis.swing_detector import SwingAnalysis, SwingPoint


def test_detects_higher_high():
    analysis = SwingAnalysis(
        swing_highs=[
            SwingPoint(index=2, price=108),
            SwingPoint(index=6, price=112),
        ],
        swing_lows=[],
    )

    analyzer = MarketStructureAnalyzer()

    structure = analyzer.analyze(analysis)

    assert structure.is_higher_high is True
    assert structure.is_higher_low is False
    assert structure.is_lower_high is False
    assert structure.is_lower_low is False

def test_does_not_detect_higher_high_when_latest_high_is_lower():
    analysis = SwingAnalysis(
        swing_highs=[
            SwingPoint(index=2, price=112),
            SwingPoint(index=6, price=108),
        ],
        swing_lows=[],
    )

    analyzer = MarketStructureAnalyzer()

    structure = analyzer.analyze(analysis)

    assert structure.is_higher_high is False


def test_not_higher_high_when_only_one_swing_high_exists():
    analysis = SwingAnalysis(
        swing_highs=[
            SwingPoint(index=2, price=108),
        ],
        swing_lows=[],
    )

    analyzer = MarketStructureAnalyzer()

    structure = analyzer.analyze(analysis)

    assert structure.is_higher_high is False
    
def test_detects_higher_low():
    analysis = SwingAnalysis(
        swing_highs=[],
        swing_lows=[
            SwingPoint(index=3, price=95),
            SwingPoint(index=8, price=100),
        ],
    )

    analyzer = MarketStructureAnalyzer()

    structure = analyzer.analyze(analysis)

    assert structure.is_higher_low is True
def test_does_not_detect_higher_low_when_latest_low_is_lower():
    analysis = SwingAnalysis(
        swing_highs=[],
        swing_lows=[
            SwingPoint(index=3, price=100),
            SwingPoint(index=8, price=95),
        ],
    )

    analyzer = MarketStructureAnalyzer()

    structure = analyzer.analyze(analysis)

    assert structure.is_higher_low is False
def test_not_higher_low_when_only_one_swing_low_exists():
    analysis = SwingAnalysis(
        swing_highs=[],
        swing_lows=[
            SwingPoint(index=3, price=95),
        ],
    )

    analyzer = MarketStructureAnalyzer()

    structure = analyzer.analyze(analysis)

    assert structure.is_higher_low is False

def test_detects_lower_high():
    analysis = SwingAnalysis(
        swing_highs=[
            SwingPoint(index=2, price=112),
            SwingPoint(index=6, price=108),
        ],
        swing_lows=[],
    )

    analyzer = MarketStructureAnalyzer()

    structure = analyzer.analyze(analysis)

    assert structure.is_lower_high is True
def test_detects_lower_low():
    analysis = SwingAnalysis(
        swing_highs=[],
        swing_lows=[
            SwingPoint(index=3, price=100),
            SwingPoint(index=8, price=95),
        ],
    )

    analyzer = MarketStructureAnalyzer()

    structure = analyzer.analyze(analysis)

    assert structure.is_lower_low is True
def test_does_not_detect_lower_low_when_latest_low_is_higher():
    analysis = SwingAnalysis(
        swing_highs=[],
        swing_lows=[
            SwingPoint(index=3, price=95),
            SwingPoint(index=8, price=100),
        ],
    )

    analyzer = MarketStructureAnalyzer()

    structure = analyzer.analyze(analysis)

    assert structure.is_lower_low is False
def test_not_lower_low_when_only_one_swing_low_exists():
    analysis = SwingAnalysis(
        swing_highs=[],
        swing_lows=[
            SwingPoint(index=3, price=95),
        ],
    )

    analyzer = MarketStructureAnalyzer()

    structure = analyzer.analyze(analysis)

    assert structure.is_lower_low is False
def test_detects_bullish_break_of_structure():
    analysis = SwingAnalysis(
        swing_highs=[
            SwingPoint(index=2, price=108),
            SwingPoint(index=6, price=112),
        ],
        swing_lows=[
            SwingPoint(index=3, price=95),
            SwingPoint(index=8, price=100),
        ],
    )

    analyzer = MarketStructureAnalyzer()

    structure = analyzer.analyze(analysis)

    assert structure.is_bullish_bos is True
def test_detects_bearish_break_of_structure():
    analysis = SwingAnalysis(
        swing_highs=[
            SwingPoint(index=2, price=112),
            SwingPoint(index=6, price=108),
        ],
        swing_lows=[
            SwingPoint(index=3, price=100),
            SwingPoint(index=8, price=95),
        ],
    )

    analyzer = MarketStructureAnalyzer()

    structure = analyzer.analyze(analysis)

    assert structure.is_bearish_bos is True