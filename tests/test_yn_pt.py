import os.path
import unittest
import json
from ovos_yes_no_solver import YesNoSolver


class TestYesNo(unittest.TestCase):
    def setUp(self):
        self.solver = YesNoSolver()
        # Load the test data from the JSON file
        with open(os.path.join(os.path.dirname(__file__), "test_sentences_pt.json"), "r") as f:
            self.test_data = json.load(f)

    def test_yesno(self):
        def test_utt(text, expected):
            res = self.solver.match_yes_or_no(text, "pt-pt")
            print(text, expected, res)
            self.assertEqual(res, expected)

        # Test "yes" cases
        for sentence in self.test_data["yes"]:
            test_utt(sentence, True)

        # Test "no" cases
        for sentence in self.test_data["no"]:
            test_utt(sentence, False)

        # Test "null" cases
        for sentence in self.test_data["null"]:
            test_utt(sentence, None)
