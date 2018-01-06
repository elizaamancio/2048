import unittest
from board.line import Line
from board.field import Field

class LineTest(unittest.TestCase):
    def test_if_returns_array_of_zeros_if_entry_is_array_with_zeros(self):
        line = Line([0,0,0,0])
        expected_beam = [0,0,0,0]
        line.squeeze()
        self.assertEqual(beam_field_to_int_array(line.beam), expected_beam)

    def test_if_numbers_2_moves_3_spots_to_the_left(self):
        line = Line([0,0,0,2])
        expected_beam = [2,0,0,0]
        line.squeeze()
        self.assertEqual(beam_field_to_int_array(line.beam), expected_beam)

    def test_if_numbers_2_moves_2_spots_to_the_left(self):
        line = Line([0,2,0,0])
        expected_beam = [2,0,0,0]
        line.squeeze()
        self.assertEqual(beam_field_to_int_array(line.beam), expected_beam)

    def test_if_numbers_2_and_4_moves_to_the_left(self):
        line = Line([0,2,0,4])
        expected_beam = [2,4,0,0]
        line.squeeze()
        self.assertEqual(beam_field_to_int_array(line.beam), expected_beam)

    def test_if_numbers_2_and_2_sum_and_moves_to_the_left(self):
        line = Line([0,2,0,2])
        expected_beam = [4,0,0,0]
        line.squeeze()
        self.assertEqual(beam_field_to_int_array(line.beam), expected_beam)

    def test_if_numbers_2_and_2_sum_and_they_all_move_to_the_left(self):
        line = Line([0,2,2,4])
        expected_beam = [4,4,0,0]
        line.squeeze()
        self.assertEqual(beam_field_to_int_array(line.beam), expected_beam)

    def test_if_numbers_2_2_2_2_squeeze_and_they_all_move_to_the_left(self):
        line = Line([2,2,2,2])
        expected_beam = [4,4,0,0]
        line.squeeze()
        self.assertEqual(beam_field_to_int_array(line.beam), expected_beam)

    def test_if_numbers_2_2_2_2_squeeze_and_they_all_move_to_the_left(self):
        line = Line([2,2,0,2,2])
        expected_beam = [4,4,0,0,0]
        line.squeeze()
        self.assertEqual(beam_field_to_int_array(line.beam), expected_beam)

def beam_field_to_int_array(beam):
    return [f.value for f in beam]
