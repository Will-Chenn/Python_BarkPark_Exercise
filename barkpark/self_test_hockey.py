from typing import *
from hockey import *


def test_2_team_no_play():
    target_team = 1
    num_team = 2
    already_played = []
    assert 1 == solve(target_team, num_team, already_played)


def test_2_team_win_play():
    target_team = 1
    num_team = 2
    already_played = [(1, 2, 'W')]
    assert 1 == solve(target_team, num_team, already_played)


def test_2_team_lose_play():
    target_team = 1
    num_team = 2
    already_played = [(1, 2, 'L')]
    assert 0 == solve(target_team, num_team, already_played)


def test_3_team_no_play():
    target_team = 1
    num_team = 3
    already_played = []
    assert 7 == solve(target_team, num_team, already_played)


def test_3_team_1_play_w():
    target_team = 1
    num_team = 3
    already_played = [(1, 2, 'W')]
    assert 5 == solve(target_team, num_team, already_played)


def test_3_team_1_play_l():
    target_team = 1
    num_team = 3
    already_played = [(1, 2, 'L')]
    assert 0 == solve(target_team, num_team, already_played)


def test_3_team_1_play_t():
    target_team = 1
    num_team = 3
    already_played = [(1, 2, 'T')]
    assert 2 == solve(target_team, num_team, already_played)


def test_3_team_2_play_w_w():
    target_team = 1
    num_team = 3
    already_played = [(1, 2, 'W'), (2, 3, 'W')]
    assert 2 == solve(target_team, num_team, already_played)


def test_3_team_2_play_w_t():
    target_team = 1
    num_team = 3
    already_played = [(1, 2, 'W'), (2, 3, 't')]
    assert 2 == solve(target_team, num_team, already_played)


def test_3_team_2_play_w_l():
    target_team = 1
    num_team = 3
    already_played = [(1, 2, 'W'), (2, 3, 'l')]
    assert 2 == solve(target_team, num_team, already_played)


def test_3_team_1_play_l_l():
    target_team = 1
    num_team = 3
    already_played = [(1, 2, 'L'), (2, 3, 'L')]
    assert 0 == solve(target_team, num_team, already_played)


def test_3_team_1_play_l_w():
    target_team = 1
    num_team = 3
    already_played = [(1, 2, 'L'), (2, 3, 'W')]
    assert 0 == solve(target_team, num_team, already_played)


def test_3_team_1_play_l_t():
    target_team = 1
    num_team = 3
    already_played = [(1, 2, 'L'), (2, 3, 'T')]
    assert 0 == solve(target_team, num_team, already_played)


def test_3_team_1_play_t_t():
    target_team = 1
    num_team = 3
    already_played = [(1, 2, 'T'), (2, 3, 'T')]
    assert 1 == solve(target_team, num_team, already_played)


def test_3_team_1_play_t_w():
    target_team = 1
    num_team = 3
    already_played = [(1, 2, 'T'), (2, 3, 'W')]
    assert 0 == solve(target_team, num_team, already_played)


def test_3_team_1_play_t_l():
    target_team = 1
    num_team = 3
    already_played = [(1, 2, 'T'), (2, 3, 'L')]
    assert 1 == solve(target_team, num_team, already_played)


if __name__ == '__main__':
    import pytest

    pytest.main(['self_test_hockey.py'])
