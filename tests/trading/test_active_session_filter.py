from datetime import datetime

from aitradebot.trading.active_session_filter import (
    ActiveSessionFilter,
)


def test_before_market_open():
    session = ActiveSessionFilter()

    assert (
        session.is_active(
            datetime(2026, 8, 3, 9, 14),
        )
        is False
    )


def test_first_session_start():
    session = ActiveSessionFilter()

    assert (
        session.is_active(
            datetime(2026, 8, 3, 9, 15),
        )
        is True
    )


def test_first_session_active():
    session = ActiveSessionFilter()

    assert (
        session.is_active(
            datetime(2026, 8, 3, 10, 30),
        )
        is True
    )


def test_first_session_end():
    session = ActiveSessionFilter()

    assert (
        session.is_active(
            datetime(2026, 8, 3, 11, 0),
        )
        is False
    )


def test_lunch_break():
    session = ActiveSessionFilter()

    assert (
        session.is_active(
            datetime(2026, 8, 3, 12, 0),
        )
        is False
    )


def test_second_session_start():
    session = ActiveSessionFilter()

    assert (
        session.is_active(
            datetime(2026, 8, 3, 13, 30),
        )
        is True
    )


def test_second_session_active():
    session = ActiveSessionFilter()

    assert (
        session.is_active(
            datetime(2026, 8, 3, 14, 45),
        )
        is True
    )


def test_market_close():
    session = ActiveSessionFilter()

    assert (
        session.is_active(
            datetime(2026, 8, 3, 15, 0),
        )
        is False
    )