class Employee:

    def __init__(self, first: str, last: str, pay: int):
        self.first = first
        self.last = last
        self.pay = pay

    def __repr__(self):
        return f"Employee(first='{self.first}', last='{self.last}', pay='{self.pay}'"

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.first, self.last, self.pay) == (other.first, other.last, other.pay)


if __name__ == '__main__':
    emp_1 = Employee('Corey', 'Schafer', 50000)
    emp_2 = Employee('Test', 'Employee', 60000)
    print(emp_1)
