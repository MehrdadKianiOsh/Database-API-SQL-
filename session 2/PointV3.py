import re
class Point: # inherit form object: __new__(), __init__(), __repr__(), __eq__()
    def __init__(self, valx, valy):
        self.__x=valx # x is a "data attribute" or "instance variable"
        self.y=valy
    def __repr__(self):
        return f"<{self.__x},{self.y}>"
    def clear(self):
        self.__x=self.y=0
    def __eq__(self, other): # ==
        return self.__x == other.__x and self.y ==other.y
    
    def setX(self, valx):
        if isinstance(valx, int):
            self.__x=valx
        else:
            raise Exception ("Wrong value for x")
    def getX(self):
        return self.__x
    
    x=property(getX, setX)
    
    # parse is a "class" or "static" method:
    def parse(cls, text):
        regexp=re.compile(r"<(\d+),(\d+)>")
        mo=regexp.match(text)
        if mo:
            return Point(int(mo.group(1)), int(mo.group(2)))
        else:
            return Point(0,0)
        
    parse=classmethod(parse)  
    
c=Point.parse("<23,56>")
print(c) # <23,56>