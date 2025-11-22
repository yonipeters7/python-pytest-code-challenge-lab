import pytest
from palindrome import longest_palindromic_substring

# Basic test cases from the examples
def test_babad():
    result = longest_palindromic_substring("babad")
    # Either "bab" or "aba" is valid
    assert result == "bab" or result == "aba"

def test_cbbd():
    result = longest_palindromic_substring("cbbd")
    assert result == "bb"

def test_single_character():
    result = longest_palindromic_substring("a")
    assert result == "a"

def test_two_characters():
    result = longest_palindromic_substring("ac")
    # Either "a" or "c" is valid
    assert result == "a" or result == "c"

def test_racecar():
    result = longest_palindromic_substring("racecar")
    assert result == "racecar"

# Edge cases
def test_empty_string():
    # Testing with empty string
    result = longest_palindromic_substring("")
    assert result == ""

def test_all_same_character():
    result = longest_palindromic_substring("aaaa")
    assert result == "aaaa"

def test_no_palindrome_longer_than_one():
    result = longest_palindromic_substring("abcdef")
    # Should return any single character
    assert len(result) == 1

def test_palindrome_at_beginning():
    result = longest_palindromic_substring("abacabad")
    assert result == "abacaba"

def test_palindrome_at_end():
    result = longest_palindromic_substring("xyracecar")
    assert result == "racecar"

# Testing with numbers mixed in
def test_with_numbers():
    result = longest_palindromic_substring("a1b2b1a")
    assert result == "1b2b1"

# Longer string test
def test_longer_string():
    result = longest_palindromic_substring("bananas")
    assert result == "anana"

# Two character palindrome
def test_two_char_palindrome():
    result = longest_palindromic_substring("aa")
    assert result == "aa"

# Multiple palindromes same length
def test_multiple_same_length():
    result = longest_palindromic_substring("abba")
    assert result == "abba"
