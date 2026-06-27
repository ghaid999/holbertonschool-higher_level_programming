#!/usr/bin/env python3
""" Dragon class with mixins"""


class SwimMixin:
  """ class SwimMixin."""
  def swim(self):
    """ methode swim"""
    print( "The creature swims!")

class FlyMixin:
  """ class FlyMixin."""
  def fly(self):
    """ methode fly"""
    prints("The creature flies!")

class Dragon(SwimMixin,FlyMixin):
  """ class Dragon."""
  def rora(self):
    """ methode rora"""
    prints("The dragon roars!")
  
