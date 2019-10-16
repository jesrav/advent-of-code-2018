from utils import load_data
from collections import defaultdict

claims_input = load_data('input_day3.txt')

test_claims = [
    '#1 @ 1,3: 4x4',
    '#2 @ 3,1: 4x4',
    '#3 @ 5,5: 2x2',
]

class Claim(object):

    def __init__(self, claim_str):
        self.claim_str = claim_str
        self.id = int(self.claim_str.split(' ')[0][1:])
        start_coordinates = self.claim_str.split(' ')[2].replace(":", "").split(',')
        self.start_x = int(start_coordinates[0])
        self.start_y = int(start_coordinates[1])
        end_coordinates = self.claim_str.split(' ')[3].split('x')
        self.end_x = self.start_x + int(end_coordinates[0])
        self.end_y = self.start_y + int(end_coordinates[1])

class CommonArea(object):

    def __init__(self):
        self.areas = defaultdict(list)
        self.unit_ids = set()

    def add_unit_id_area(self, unit_id, area_x, area_y):
        self.areas[(area_x, area_y)].append(unit_id)

    def add_unit_id(self, unit_id):
        self.unit_ids.add(unit_id)

    def add_claim(self, claim):
        self.add_unit_id(claim.id)
        for x in range(claim.start_x, claim.end_x):
            for y in range(claim.start_y, claim.end_y):
                self.add_unit_id_area(claim.id, x,y)

    def n_areas_with_more_than_one_claim(self):
        return len([key for key in self.areas if len(self.areas[key]) > 1])

    def non_overlapping_unit_ids(self):
        units_with_overlap = [self.areas[key] for key in self.areas if len(self.areas[key]) > 1]
        units_with_overlap_set = set([item for sublist in units_with_overlap for item in sublist])
        return [unit_id for unit_id in self.unit_ids if unit_id not in units_with_overlap_set]

common_area = CommonArea()

for claim_string in claims_input:
    common_area.add_claim(Claim(claim_string))

print(common_area.n_areas_with_more_than_one_claim())
print(common_area.non_overlapping_unit_ids())