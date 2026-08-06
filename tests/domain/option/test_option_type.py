from aitradebot.domain.option.option_type import OptionType


def test_option_type_values():
    assert OptionType.CALL.value == "CALL"
    assert OptionType.PUT.value == "PUT"


def test_option_types_are_distinct():
    assert OptionType.CALL != OptionType.PUT