"""
BARK PARK
"""

# Imports

from typing import List  # Specific annotations


def solve(dogs: List[str], beefs: List[List[str]]) -> int:
    """
    Return an int representing the number of valid parks in the problem.

    dogs is a list of dog names.
    beefs is a list of lists (pairs of beefing dog names).

    Precondition: each dog in <beefs> is in <dogs>.
    """
    lst = case_list(dogs, beefs)

    return len(lst)


def case_list(dogs: List[str], beefs: List[List[str]]) -> List:
    """get the correct cases for the bark park"""
    if len(dogs) == 0:
        return [[]]

    if len(dogs) == 1:
        return [[], [dogs[0]]]

    new_dog = dogs[0]
    last_dogs = dogs[1:]
    with_new_dog = []
    new_beefs = []
    for b in beefs:
        if new_dog in b:
            with_new_dog.append(b)
        elif new_dog not in b:
            new_beefs.append(b)
    new_lst_without_a = case_list(last_dogs, new_beefs)
    new_lst_without_a_2 = new_lst_without_a[:]
    lst_with_a = helper_add_dog(with_new_dog, new_lst_without_a_2, new_dog)
    return lst_with_a + new_lst_without_a


def helper_add_dog(with_d_beefs: List, without_d_cases: List, dog: str) -> List:
    """
    add the dog into the case if other dogs don't have beef with it.
    and return this list
    """
    ans = []
    new_with_d_beefs = []
    for beef_pair in with_d_beefs:
        for item in beef_pair:
            if item not in new_with_d_beefs:
                new_with_d_beefs.append(item)

    for d in without_d_cases:
        if len(d) > 1:
            if d[0] in new_with_d_beefs or d[1] in new_with_d_beefs:
                pass
            else:
                ans.append(d + [dog])
        if len(d) == 1:
            if d[0] not in new_with_d_beefs:
                ans.append(d + [dog])
        if len(d) == 0:
            ans.append(d + [dog])
    return ans


if __name__ == '__main__':
    #import python_ta

    #python_ta.check_all()

    mydogs = ['Grimm', 'Dogbert', 'Rufus']
    mybeefs = [['Grimm', 'Rufus'], ['Dogbert', 'Rufus']]
    print(solve(mydogs, mybeefs))
