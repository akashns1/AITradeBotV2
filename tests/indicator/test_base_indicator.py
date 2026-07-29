import pytest

from aitradebot.indicators import BaseIndicator


def test_base_indicator_is_abstract() -> None:
    with pytest.raises(TypeError):
        BaseIndicator()
