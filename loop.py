#!/usr/bin/env python3


class Employee:
    def __init__(self, name, score):
        self.name = name
        self.score = score


def add_newline_end(func):
    def inner_func(*args, **kargs):
        func(*args, **kargs)
        print()

    return inner_func


@add_newline_end
def enumerate_loop():
    employees = ["John", "Danny", "Jennifer"]
    for id, name in enumerate(employees, start=3000):
        print(f"{name}'s employee ID #:{id}")


@add_newline_end
def reverse_loop():
    meals = ["pizza", "hamberger", "pasta", "ramen", "salad"]
    for meal in reversed(meals):
        print(meal)


@add_newline_end
def sorted_loop():
    employee0 = Employee("John Smith", 95)
    employee1 = Employee("Mike Brown", 99)
    employee2 = Employee("Jennifer Thompson", 97)
    employees = [employee0, employee1, employee2]
    # For the key argument, we can specify a function of one argument to
    # compare each element in the iterable.
    for employee in sorted(employees, key=lambda x: x.score, reverse=True):
        print(f"{employee.name} score: {employee.score}")


@add_newline_end
def zip_loop():
    numbers0 = [4, 5, 6]
    numbers1 = [11, 12, 13]
    result = list(zip(numbers0, numbers1))
    print(result)
    for j, k in zip(numbers0, numbers1):
        print(f"{j} * {k} = {j * k}")


if __name__ == "__main__":
    enumerate_loop()
    reverse_loop()
    sorted_loop()
    zip_loop()
