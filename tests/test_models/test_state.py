#!/usr/bin/python3
import unittest
from models.state import State


class TestState(unittest.TestCase):
    def test_attributes_initialization(self):
        state = State()
        self.assertEqual(state.name, "")

    # Add more test cases as needed


if __name__ == '__main__':
    unittest.main()
