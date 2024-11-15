from Calculator import Calculator

class MaxLimitCalculator(Calculator):
    def __init__(self):
        super().__init__()

    def add(self, val):
        super().add(val)
        if self.value >= 100:
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)
