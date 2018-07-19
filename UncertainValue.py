##############################################################################
# @class UncertainValue
#     (c) 2018 Kyle West - kyle-west@github.com
#     MIT License. See: [Licensing Info](https://opensource.org/licenses/MIT)
# 
# Create a value from a random +/- uncertainty which can be treated like a
# float or integer. 
#
#    x = UncertainValue(50, 5)  # <--- random sample from 45 to 55. 
#
##############################################################################
from random import uniform

class UncertainValue:
    def __init__ (self, value = 0 , uncertainty = 0):
        self.v = value
        self.u = uncertainty
        self.resample()
        
    def resample(self):
        self.value = uniform(self.v - self.u, self.v + self.u)
        return self.value
        
    def get(self):
        return self.value

    def __float__(self):
        return self.get()
    
    def __radd__(self, other):     return other + self.get()
    def __rmul__(self, other):     return other * self.get()
    def __rlt__(self, other) :     return other < self.get()
    def __rge__(self, other) :     return other >= self.get()
    def __rsub__(self, other):     return other - self.get()
    def __rmod__(self, other):     return other % self.get()
    def __rtruediv__(self, other): return other / self.get()
    def __rle__(self, other):      return other <= self.get()
    def __req__(self, other):      return other == self.get()
    def __rne__(self, other):      return other != self.get()
    def __rgt__(self, other):      return other > self.get()
    
    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.get() + other.get()
        elif isinstance(other, (int,float)):
            return self.get() + other
    
    def __mul__ (self, other):
        if isinstance(other, self.__class__):
            return self.get() * other.get()
        elif isinstance(other, (float, int)):
            return self.get() * other
    
    def __lt__ (self, other):
        if isinstance(other, self.__class__): 
            return self.get() < other.get()
        elif isinstance(other, (int,float)): 
            return self.get() < other
    
    def __ge__ (self, other):
        if isinstance(other, self.__class__):
            return self.get() >= other.get()
        elif isinstance(other, (int,float)):
            return self.get() >= other
        
    def __sub__ (self, other):
        if isinstance(other, self.__class__):
            return self.get() - other.get()
        elif isinstance(other, (int,float)):
            return self.get() - other

    def __mod__ (self, other):
        if isinstance(other, self.__class__):
            return self.get() % other.get()
        elif isinstance(other, (int,float)):
            return self.get() % other

    def __truediv__ (self, other):
        if isinstance(other, self.__class__):
            return self.get() / other.get()
        elif isinstance(other, (int,float)):
            return self.get() / other

    def __le__ (self, other):
        if isinstance(other, self.__class__):
            return self.get() <= other.get()
        elif isinstance(other, (int,float)):
            return self.get() <= other

    def __eq__ (self, other):
        if isinstance(other, self.__class__):
            return self.get() == other.get()
        elif isinstance(other, (int,float)):
            return self.get() == other

    def __ne__ (self, other):
        if isinstance(other, self.__class__):
            return self.get() != other.get()
        elif isinstance(other, (int,float)):
            return self.get() != other

    def __gt__ (self, other):
        if isinstance(other, self.__class__):
            return self.get() > other.get()
        elif isinstance(other, (int,float)):
            return self.get() > other
        
    def __pow__ (self, other):
        if isinstance(other, self.__class__):
            return self.get() ** other.get()
        elif isinstance(other, (int,float)):
            return self.get() ** other
