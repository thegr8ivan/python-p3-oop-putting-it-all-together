#!/usr/bin/env python3

class Book:
   def __init__(self, title, page_count, genre):
       self.title = title
       self.page_count = None
       self.page_count = page_count
       self.genre = genre 

   @property
   def page_count(self):
       return self._page_count
   
   @page_count.setter
   def page_count(self, value):
       if not isinstance(value, int) or value <= 0:
          print("page_count must be an integer")
       else:
           self._page_count = value
   def turn_page(self):
       print("Flipping the page...wow, you read fast!")
        
