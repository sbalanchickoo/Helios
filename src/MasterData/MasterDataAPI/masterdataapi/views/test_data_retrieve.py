import run
import models
from .data_retrieve import get_states, get_countries
from flask import url_for
import unittest
from masterdataapi import app


class TestDataRetrieve(unittest.TestCase):

    @unittest.skip("WIP")
    def test_get_states(self):
        states = get_states()
        self.assertEqual(3, len(states))

    @unittest.skip("WIP")
    def test_get_countries(self):
        countries = get_countries()
        self.assertNotEqual(0, len(countries))



