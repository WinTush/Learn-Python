from dataclasses import dataclass


@dataclass
class Employee:
    first: str
    last: str
    pay: int


if __name__ == '__main__':
    emp_1 = Employee('Corey', 'Schafer', 50000)
    emp_2 = Employee('Test', 'Employee', 60000)
    print(emp_1)
