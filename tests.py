import pytest

from main import number_to_numerology


def test_bowler_donations():
    assert number_to_numerology(10) == "🎳"
    assert number_to_numerology(1010) == "🎳🎳"
    assert number_to_numerology(101010) == "🎳🎳🎳🦃🔥🔥🔥"
    assert number_to_numerology(10101010) == "🎳🎳🎳🎳🦃🦃🔥🔥🔥"
    assert number_to_numerology(1010101010) == "🎳🎳🎳🎳🎳🦃🦃🦃🔥🔥🔥"


def test_boobs_donations():
    assert number_to_numerology(6006) == "🎱🎱"
    assert number_to_numerology(6008) == "🎱🎱"
    assert number_to_numerology(8006) == "🎱🎱"
    assert number_to_numerology(8008) == "🎱🎱"


def test_ducksinarow_donations():
    assert number_to_numerology(2) == "🦆💩"
    assert number_to_numerology(22) == "🦆🦆"
    assert number_to_numerology(222) == "🦆🦆🦆"
    assert number_to_numerology(2222) == "🦆🦆🦆🦆"
    assert number_to_numerology(22222) == "🦆🦆🦆🦆🦆🔥"
    assert number_to_numerology(222222) == "🦆🦆🦆🦆🦆🦆🔥🔥🔥"
    assert number_to_numerology(2222222) == "🦆🦆🦆🦆🦆🦆🦆🔥🔥🔥"


def test_bitcoin_donations():
    assert number_to_numerology(21) == "🪙"
    assert number_to_numerology(2121) == "🪙🪙"
    assert number_to_numerology(212121) == "🪙🪙🪙🔥🔥🔥"


def test_magicnumber_donations():
    assert number_to_numerology(33) == "✨"
    assert number_to_numerology(333) == "✨"
    assert number_to_numerology(3333) == "✨✨"
    assert number_to_numerology(33333) == "✨✨🔥"


def test_swasslenuff_donations():
    assert number_to_numerology(69) == "💋"
    assert number_to_numerology(6969) == "💋💋"
    assert number_to_numerology(696969) == "💋💋💋🔥🔥🔥"


def test_stoner_donation():
    assert number_to_numerology(420) == "✌👽💨"
    assert number_to_numerology(420420) == "✌👽💨✌👽💨🔥🔥🔥"


def test_devil_donation():
    assert number_to_numerology(666) == "😈"
    assert number_to_numerology(666666) == "😈😈🔥🔥🔥"


def test_america_donation():
    assert number_to_numerology(1776) == "🇺🇸"

def test_canada_donation():
    assert number_to_numerology(1867) == "🇨🇦"

def test_wolf_donation():
    assert number_to_numerology(9653) == "🐺"


def test_combinations():
    assert number_to_numerology(2169) == "🪙💋"
    assert number_to_numerology(6921) == "💋🪙"
    assert number_to_numerology(3369) == "✨💋"
    assert number_to_numerology(6933) == "💋✨"
    assert number_to_numerology(1021) == "🎳🪙"
    assert number_to_numerology(2110) == "🪙🎳"
    assert number_to_numerology(1069) == "🎳💋"
    assert number_to_numerology(6910) == "💋🎳"
    assert number_to_numerology(7388) == "👋🥰"
    assert number_to_numerology(8873) == "🥰👋"