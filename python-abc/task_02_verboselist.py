#!/usr/bin/env python3
"""VerboseList."""


class VerboseList(list):
    """List class"""

    def append(self, item):
      """append method """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
      """extend method """
        count = len(items)
        super().extend(items)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
      """remove method """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
      """pop method """
        item = self[index]
        super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
