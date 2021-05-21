from typing import *
from barkpark import *


def test_empty_park():
    dogs = []
    beefs = []
    assert 1 == solve(dogs, beefs)


def test_empty_beef_one_dog():
    dogs = ['A']
    beefs = []
    assert 2 == solve(dogs, beefs)


def test_empty_beef_two_dog():
    dogs = ['A', 'B']
    beefs = []
    assert 4 == solve(dogs, beefs)


def test_empty_beef_multiple_dog():
    dogs = ['A', 'B', 'C']
    beefs = []
    assert 8 == solve(dogs, beefs)


def test_one_beef_pair_two_dog():
    dogs = ['A', 'B']
    beefs = [['A', 'B']]
    assert 3 == solve(dogs, beefs)


def test_one_beef_pair_three_dog():
    dogs = ['A', 'B', 'C']
    beefs = [['B', 'A']]

    assert 6 == solve(dogs, beefs)


def test_one_beef_pair_multiple_dog():
    dogs = ['A', 'B', 'C', 'D']
    beefs = [['D', 'A']]

    assert 12 == solve(dogs, beefs)


def test_two_beef_pair_three_dog():
    dogs = ['A', 'B', 'C']
    beefs = [['A', 'B'], ['C', 'B']]

    assert 5 == solve(dogs, beefs)


def test_two_beef_pair_four_dog():
    dogs = ['A', 'B', 'C', 'D']
    beefs = [['A', 'B'], ['B', 'C']]

    assert 10 == solve(dogs, beefs)


def test_two_beef_pair_multiple_dog():
    dogs = ['A', 'B', 'C', 'D', 'E']
    beefs = [['A', 'E'], ['C', 'D']]

    assert 18 == solve(dogs, beefs)


def test_edge_case():
    dogs = ['A', 'B', 'C']
    beefs = [['A', 'B'], ['C', 'B'], ['C', 'A']]
    assert 4 == solve(dogs, beefs)


if __name__ == '__main__':
    import pytest

    pytest.main(['self_test_barkpark.py'])
