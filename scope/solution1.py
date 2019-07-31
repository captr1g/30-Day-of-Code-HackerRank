# using scope find the maximum difference 
class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = None
    # find maximum and minmum of element and then subtract to find the difference
    def computeDifference(self):
        maximum=max(self.__elements)
        minimum=min(self.__elements)
        self.maximumDifference = maximum-minimum

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)