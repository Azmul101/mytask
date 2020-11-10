class Basic:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * 1.04)


emp_1 = Basic("Azmul", "Haq", 50000)
emp_2 = Basic("azmul", "haq", 20000)

print(emp_2.fullname())
print(Basic.fullname(emp_1))
print(emp_1.first)
print(emp_2.last)
print(emp_1.fullname())
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
