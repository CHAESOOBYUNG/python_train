class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self): 
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal()
a.setdata(3,4)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(type(a))
print(type(a.add()))
print()

b = FourCal()
b.setdata(2,5)
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())
