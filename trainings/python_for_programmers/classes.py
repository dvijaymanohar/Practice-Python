

class Employee:
    # This property and its value is shared by all the objects of this class.

    # This property is common and also its values is shared among all the properties of this class.
    team_name = 'Power and Performance team'  # Class variable

    # Initialisation of instance variables
    def __init__(self,
                 Id,
                 name=None,
                 dept=None,
                 salary=0):
        self.Id = id
        self.name = name
        self.dept = dept
        self.salary = salary
        self.formerCompanies = []

    def compute_tax(self, income):
        tax = 0
        # brackets = {(0, 500000): 0, {500001, 1000000}: 0.1, {1000001, }: 0.1...}
        # for bracket in brackets:
        #     if income > bracket[0]:
        #         for _ in range(bracket[0], min(income, bracket[1])):
        #             tax += brackets[bracket]

        if income <= 250000:  # 2 Lakh 50 thousand
            tax = 0

        elif income <= 500000:  # 5 Lakh
            tax = (income - 250000) * 0.05

        elif income <= 750000:  # 7 lakh 50 thousand
            tax = (income - 500000) * 0.10 + 12500

        elif income <= 1000000:  # 10 Lakh
            tax = (income - 750000) * 0.15 + 37500

        elif income <= 1250000:  # 12 lakh 50 thousand
            tax = (income - 1000000) * 0.20 + 75000

        elif income <= 1500000:  # 15 lakh
            tax = (income - 1250000) * 0.25 + 125000

        else:
            tax = (income - 1500000) * 0.30 + 187500

        print("you owe", tax, "Rupees in tax!")

        return tax

    def salaryPerDay(self):
        pass

    def salaryPerDay(self, income):
        pass

    @classmethod
    def get_team_name(cls):
        return team_name

    @staticmethod
    def calculate_bmi(height, weigth):
        return weigth / (height ** 2)


emp1 = Employee(113010,
                'Vijaya Manohar Dogiparthi',
                'CPUSS Software Development',
                '300000')

# emp1.title = "Senior Lead Engineer"
emp1.formerCompanies.append('Rambus Security')
emp1.formerCompanies.append('Qualcomm')
emp1.formerCompanies.append('Intel')
emp1.formerCompanies.append('Tes Electronics')


print(emp1.calculate_bmi())

print(emp1)
