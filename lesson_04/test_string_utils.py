import pytest
from string_utils import StringUtils

string_utils = StringUtils()


# ==========================================
# 1. ТЕСТЫ ДЛЯ CAPITALIZE
# ==========================================
@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("skypro", "Skypro"),
        ("hello world", "Hello world"),
        ("python", "Python"),
        (
            "123abc",
            "123abc",
        ),  # Цифры не меняются, но это позитивный сценарий (строка на входе)
    ],
)
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("", ""),
        ("   ", "   "),
    ],
)
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# Баг: capitalize падает, если передать None (нарушение типизации)
@pytest.mark.negative
def test_capitalize_none():
    with pytest.raises(AttributeError):
        string_utils.capitalize(None)


# ==========================================
# 2. ТЕСТЫ ДЛЯ TRIM
# ==========================================
@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("   skypro", "skypro"),
        ("skypro", "skypro"),
        ("   hello world", "hello world"),
    ],
)
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("", ""),
        ("   ", ""),
        ("123", "123"),  # Пробелов нет, строка не меняется
    ],
)
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


# Баг: trim падает, если передать None
@pytest.mark.negative
def test_trim_none():
    with pytest.raises(AttributeError):
        string_utils.trim(None)


# ==========================================
# 3. ТЕСТЫ ДЛЯ CONTAINS
# ==========================================
@pytest.mark.positive
@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("SkyPro", "S", True),
        ("SkyPro", "k", True),
        ("SkyPro", "Pro", True),
    ],
)
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("SkyPro", "U", False),
        ("", "a", False),
        ("123", "a", False),
    ],
)
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


# Баг: contains падает с TypeError (а не ValueError), если передать None или список
@pytest.mark.negative
def test_contains_none():
    with pytest.raises(AttributeError):
        string_utils.contains(None, "S")


# ==========================================
# 4. ТЕСТЫ ДЛЯ DELETE_SYMBOL
# ==========================================
@pytest.mark.positive
@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("SkyPro", "k", "SyPro"),
        ("SkyPro", "Pro", "Sky"),
        ("SkyPro", "S", "kyPro"),
        ("123123", "1", "2323"),
    ],
)
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("SkyPro", "U", "SkyPro"),  # Символа нет, строка не меняется
        ("", "a", ""),
        ("   ", "a", "   "),
    ],
)
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


# Баг: delete_symbol падает при передаче None
@pytest.mark.negative
def test_delete_symbol_none():
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(None, "S")
