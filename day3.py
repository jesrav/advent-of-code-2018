from utils import load_data

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


print(claims_input)

test_claim = Claim(test_claims[0])
test_claim.start_x
