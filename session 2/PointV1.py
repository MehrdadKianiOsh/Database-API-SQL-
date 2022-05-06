
class Point: # inherit form object: __new__(), __init__(), __repr__(), __eq__()
    def __init__(self, valx, valy):
        self.x=valx # x is a "data attribute" or "instance variable"
        self.y=valy
    def __repr__(self):
        return f"<{self.x},{self.y}>"
    def clear(self):
        self.x=self.y=0
    def __eq__(self, other): # ==
        return self.x == other.x and self.y ==other.y
    
center=Point(2,3)
print(center.__dict__)

# 1) center=Point.__new__()
# 2) center.__init__(2,3)
# 3) __init__(center, 2, 3)

print(center)
# 1) print(center.__repr__()))

center.clear()
print(center)

p1=Point(2,0)

print(center==p1) # print(center.__eq__(p1))