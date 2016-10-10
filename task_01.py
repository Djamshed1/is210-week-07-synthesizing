#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 7 synthesizing task 01"""

def get_matches(players):
    """Matching the players together.

    Args:
        players(list): A list of players names.

    Returns:
        returns a tuples inside the list

    Examples:
        >>> import task_01
        >>> task_01.get_matches(['Harry', 'Howard', 'Hugh'])
        [('Harry', 'Howard'), ('Harry', 'Hugh'), ('Howard', 'Hugh')]
        >>> task_01.get_matches(['James', 'John', 'Johnson'])
        [('James', 'John'), ('James', 'Johnson'), ('John', 'Johnson')]
    """
    list1 = []

    for idx, item in enumerate(players):
        for idx2, item2 in enumerate(players):
            if idx < idx2:
                list2 = (item, item2)
                list1.append(list2)
    return list1
