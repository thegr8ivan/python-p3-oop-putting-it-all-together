import pytest
import io
import sys
from lib.shoe import Shoe  

class TestShoe:
    '''Shoe in shoe.py'''

    def test_has_brand_and_size(self):
        '''has the brand and size passed to __init__, and values can be set to new instance.'''
        stan_smith = Shoe("Adidas", 9, "Leather")
        assert stan_smith.brand == "Adidas"
        assert stan_smith.size == 9
        assert stan_smith.material == "Leather"

    def test_requires_int_size(self):
        '''prints "size must be an integer" if size is not an integer.'''
        stan_smith = Shoe("Adidas", 9, "Leather")
        captured_out = io.StringIO()
        sys.stdout = captured_out
        stan_smith.size = "not an integer"  
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue().strip() == "size must be an integer"

    def test_can_cobble(self):
        '''says that the shoe has been repaired.'''
        stan_smith = Shoe("Adidas", 9, "Leather")
        captured_out = io.StringIO()
        sys.stdout = captured_out
        stan_smith.cobble()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue().strip() == "The Adidas shoe has been repaired."

    def test_cobble_makes_new(self):
        '''creates an attribute on the instance called 'condition' and set equal to 'New' after repair.'''
        stan_smith = Shoe("Adidas", 9, "Leather")
        stan_smith.cobble()
        assert stan_smith.condition == "New"
