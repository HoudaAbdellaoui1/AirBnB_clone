#!/usr/bin/python3
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def test_attributes_initialization(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    # Add more test cases as needed


if __name__ == '__main__':
    unittest.main()
