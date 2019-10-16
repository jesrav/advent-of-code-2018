from typing import List, Iterator
from utils import load_data

# Get puzzle data
frequency_change_data = load_data('input_day1.txt')
frequency_change_data = [int(freq_change) for freq_change in frequency_change_data]

def generate_frequencies(frequency_changes: List, start: int = 0) -> Iterator[int]:
    frequency = start
    while True:
        for frequency_change in frequency_changes:
            yield frequency
            frequency += frequency_change


def first_repeat_frequency(frequency_changes, start):
    seen = set()

    for frequency in generate_frequencies(frequency_changes, start):
        if frequency in seen:
            return frequency
        else: 
            seen.add(frequency)
        

print(first_repeat_frequency(frequency_change_data, start=0))
