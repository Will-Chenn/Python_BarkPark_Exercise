"""
Tests for Exercise 2 Question 1 (Zingaro Hockey League)
"""

import python_ta
import pytest
import hockey


def test_three_teams_all_played() -> None:
    """Test 3 teams that have played all their games."""
    already_played = [(1, 2, 'W'), (1, 3, 'W'), (2, 3, 'L')]
    result = hockey.solve(1, 3, already_played)
    assert 1 == result


def test_five_teams() -> None:
    """Test 5 teams that have played most of their games."""
    already_played = [(1, 3, 'L'), (1, 4, 'T'), (1, 5, 'W'),
                      (2, 3, 'W'), (2, 4, 'T'), (3, 4, 'T'), (3, 5, 'W'),
                      (4, 5, 'W')]
    result = hockey.solve(3, 5, already_played)
    assert 2 == result


if __name__ == '__main__':
    python_ta.check_all(config={'extra-imports': ['hockey']})
    pytest.main(['test_hockey.py'])
