from Calculator import Calculator

class UpgradeCalculator(Calculator):
    def __init__(self):
        self.value = 0

    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)