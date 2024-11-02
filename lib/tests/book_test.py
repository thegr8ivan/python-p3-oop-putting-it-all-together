import pytest
import io
import sys
from lib.book import Book

class TestBook:
    '''Book in book.py'''

    def test_has_title_and_page_count(self):
        '''has the title and page_count passed into __init__, and values can be set to new instance.'''
        book = Book("And Then There Were None", 272, "Mystery")
        assert book.page_count == 272
        assert book.title == "And Then There Were None"
        assert book.genre == "Mystery"

    def test_requires_int_page_count(self):
        '''prints "page_count must be an integer" if page_count is not an integer.'''
        book = Book("And Then There Were None", 272, "Mystery")
        captured_out = io.StringIO()
        sys.stdout = captured_out
        book.page_count = "not an integer"  
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue().strip() == "page_count must be an integer"

    def test_can_turn_page(self):
        '''outputs "Flipping the page...wow, you read fast!" when method turn_page() is called.'''
        book = Book("The World According to Garp", 69, "Mystery")
        captured_out = io.StringIO()
        sys.stdout = captured_out
        book.turn_page()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue().strip() == "Flipping the page...wow, you read fast!"
