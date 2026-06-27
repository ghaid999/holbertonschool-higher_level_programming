#!/usr/bin/env python3
"""Dragon class with mixins."""


class SwimMixin:
    """Mixin that adds swimming."""

    def swim(self):
        """Swim method."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying."""

    def fly(self):
        """Fly method."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class."""

    def roar(self):
        """Roar method."""
        print("The dragon roars!")
