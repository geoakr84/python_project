class Misthotos:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Misthotos.empCount += 1

    def displayCount(self):
    	print("Number of employees: %d" % Misthotos.empCount)

    def displayEmployee(self):
    	print("Info of employees: ", self.name, " ", self.salary)

mis1 = Misthotos("George Akritidis", 1500)
mis2 = Misthotos("Nikos Panagiotidis", 1200)
mis3 = Misthotos("Aggeliki Petridou", 1700)

mis1.displayEmployee()
mis2.displayEmployee()
mis3.displayEmployee()
print("Total Employees: %d" % Misthotos.empCount)