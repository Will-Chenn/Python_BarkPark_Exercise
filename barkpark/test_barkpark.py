"""
Tests for Exercise 2 Question 1 (Bark Park).
Feel free to add more tests!
"""

import python_ta
import pytest
import barkpark


def test_two_dogs_one_beef() -> None:
    """Test a case with two dogs and one beef between them."""
    dogs = ['Alma', 'Friede']
    beefs = [['Alma', 'Friede']]

    assert 3 == barkpark.solve(dogs, beefs)


def test_handout_example() -> None:
    """Test the example in the handout (3 dogs, 1 has beef with 2 others)."""
    dogs = ['Grimm', 'Dogbert', 'Rufus']
    beefs = [['Rufus', 'Grimm'], ['Rufus', 'Dogbert']]

    assert 5 == barkpark.solve(dogs, beefs)


# Run tests

if __name__ == '__main__':
    python_ta.check_all(config={'extra-imports': ['barkpark']})
    pytest.main(['test_barkpark.py'])
