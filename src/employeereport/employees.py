class employee:
    def __init__(self, name, age, dayOff, hireDate, salary):
        self.name = name
        self.age = age
        self.dayOff = dayOff
        self.hireDate = hireDate
        self.salary = salary


employee_list = [
    employee('Max', 17, 'Thursday', '2018-1-1', '$8.00'),
    employee('Sepp', 19, 'Tuesday', '2016-1-1', '$10.00'),
    employee('Tom', 20, 'Wednesday', '2019-1-1', '$20.00'),
    employee('Nina', 15, 'Wednesday', '2019-1-1', '$11.50'),
    employee('Mike', 30, 'Saturday', '2010-1-1', '$30.00')
]
