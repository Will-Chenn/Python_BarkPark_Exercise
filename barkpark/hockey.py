"""
Exercise 2 Question 2: ZINGARO HOCKEY LEAGUE
a.k.a. Started from the Bottom Now the Whole Team Here
a.k.a. "You Miss N Percent of the Shots You Don't Take; Find N" - Wayne Gretzky
"""

from typing import List, Tuple
from typing import Dict


def solve(t: int, num_teams: int,
          already: List[Tuple[int, int, str]]) -> int:
    """
    t is a team number between 1 and num_teams.
    num_teams is the total number of teams.
    Each triple in already_played describes one game that has already been
    played and is of the form (team_a, team_b, result),
    where team_a is a team number, team_b is a team number,
    and result is 'W' if team_a wins, 'L' if team_a loses,
    and 'T' if the game is a tie.

    Return the number of outcomes in which t has strictly more points
    than each other team.

    Precondition: num_teams >= 2.

    Precondition: t is a team in the range from 1 to num_teams.

    Precondition: each (team_a, team_b, result) triple in already_played
                  has team_a < team_b.
    """
    total = (num_teams * (num_teams - 1)) // 2
    if len(already) == total:
        help_dict = get_points(already)
        outcome = help_dict[t]
        a = 0
        for values in help_dict.values():
            if values > outcome:
                return 0
            if values == outcome:
                a += 1
        if a == 1:
            return 1
        return 0

    pair = rest_battle(num_teams, already)
    curr1 = solve(t, num_teams, already + [(pair[0], pair[1], "W")])
    curr2 = solve(t, num_teams, already + [(pair[0], pair[1], "T")])
    curr3 = solve(t, num_teams, already + [(pair[0], pair[1], "L")])

    return curr1 + curr2 + curr3


def get_points(already: List[Tuple[int, int, str]]) -> Dict:
    """return the dict, keys are each team, values are how many points they
     have"""
    ans = {}
    for play in already:
        if play[0] not in ans:
            ans[play[0]] = 0
        if play[1] not in ans:
            ans[play[1]] = 0

    for outcome in already:
        if outcome[2] == 'W':
            ans[outcome[0]] += 3
        elif outcome[2] == 'L':
            ans[outcome[1]] += 3
        elif outcome[2] == 'T':
            ans[outcome[0]] += 1
            ans[outcome[1]] += 1
    return ans


def rest_battle(num_teams: int,
                already: List[Tuple[int, int, str]]) -> List:
    """return the rest_battle"""
    pair = []

    for i in range(1, num_teams + 1):
        for j in range(i + 1, num_teams + 1):
            pair.append([i, j])

    for ch in already:
        t = [ch[0], ch[1]]
        if t in pair:
            pair.remove(t)

    return pair[0]


if __name__ == '__main__':
    import python_ta

    python_ta.check_all()

    already_played = [(1, 2, 'W'), (1, 3, 'W'), (2, 3, 'L')]
    print(solve(1, 3, already_played))
