#procedural process----
_global_length=3
_global_width=5
def rectangle_area(_length,_width):
    return _length*_width

#object oriented process---
class Rectangl:
    def _init_(self,_length,_width):
        self.length=_length
        self.width=_width
    def rectangle_area(self):
        return self.length*self.width