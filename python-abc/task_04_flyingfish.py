#!/usr/bin/env python3
""g Fish, Bird and FlyingFish classes."""


class Fish:
    """Fish class."""

    def swim(self):
        """Fish swims."""
        print("The fish is swimming")

    def habitat(self):
        """Fish habitat."""
        print("The fish lives in water")


class Bird:
    """Bird class."""

    def fly(self):
        """Bird flies."""
        print("The bird is flying")

    def habitat(self):
        """Bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish class."""

    def swim(self):
        """FlyingFish swims."""
        print("The flying fish is swimming!")

    def fly(self):
        """FlyingFish flies."""
        print("The flying fish is soaring!")

    def habitat(self):
        """FlyingFish habitat."""
        print("The flying fish lives both in water and the sky!")
