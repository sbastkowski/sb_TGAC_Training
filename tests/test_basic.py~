import sqer

class FakeRecord(object):
    def __init__(self, sequence, name=''):
        self.sequence = sequence
        self.name = name

def test_sum_bp():
    r = FakeRecord('ATGC')
    assert sqer.sum_bp(r) == 4

