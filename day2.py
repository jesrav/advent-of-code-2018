from typing import List

import numpy as np
from collections import Counter
from utils import load_data

# Get puzzle data
input_strings: List[str] = load_data('input_day2.txt')


# PART 1
def contains_n_of_a_kind(string: str, n: int) -> int:
    counts = Counter(list(string))
    return n in set(counts[el] for el in counts)


def get_checksum(strings: List[str]) -> int:
    count_2 = 0
    count_3 = 0
    for string in strings:
        count_2 += 1 * contains_n_of_a_kind(string, 2)
        count_3 += 1 * contains_n_of_a_kind(string, 3)

    return count_2 * count_3


print(get_checksum(input_strings))

# PART 2
test_data = [
    'abcde',
    'fghij',  # answer
    'klmno',
    'pqrst',
    'fguij',  # answer
    'axcye',
    'wvxyz',
]


def count_different_characters(string1: str, string2: str) -> int:
    string_array1 = np.array(list(string1))
    string_array2 = np.array(list(string2))
    return sum(string_array1 != string_array2)


def common_characters(string1: str, string2: str) -> str:
    string_array1 = np.array(list(string1))
    string_array2 = np.array(list(string2))
    return ''.join(list(string_array1[(string_array1 == string_array2)]))


def find_first_pair_of_strings_differing_by_one_character(strings: List[str]) -> str:
    string_sets = []
    for string1 in strings:
        remaining_strings = [string for string in strings if set([string1, string]) not in string_sets]
        for string2 in remaining_strings:
            string_set = set([string1, string2])
            string_sets.append(string_set)
            n_different_characters = count_different_characters(string1, string2)
            if n_different_characters == 1:
                return common_characters(string1, string2)


print(find_first_pair_of_strings_differing_by_one_character(input_strings))
