"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract_type, salary=0, hourly_wage=0, hours_worked=0, bonus=0, contracts_landed=0, comms_per_contract=0):
        self.name = name
        self.contract_type = contract_type
        self.salary = salary
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
        self.bonus = bonus
        self.contracts_landed = contracts_landed
        self.comms_per_contract = comms_per_contract


    def get_pay(self):
        if self.contract_type == 'salary':
            contract_pay = self.salary
        elif self.contract_type == 'hourly':
            contract_pay = self.hourly_wage * self.hours_worked
        else:
            raise ValueError ("Invalid contract type")
        
        commision_pay = self.bonus + (self.contracts_landed * self.comms_per_contract)
        total_pay = contract_pay + commision_pay

        return total_pay


    def __str__(self):
        explanation = f"{self.name} works on a"

        if self.contract_type == 'salary':
            explanation += f" monthly salary of {self.salary}"
        elif self.contract_type == 'hourly':
            explanation += f" contract of {self.hours_worked} hours at {self.hourly_wage}/hour"
        else:
            explanation += "n invalid contract type"

        if self.bonus > 0:
            explanation += f" and receives a bonus commission of {self.bonus}."
        elif self.contracts_landed > 0:
            explanation += f" and receives a commission for {self.contracts_landed} contract(s) at {self.comms_per_contract}/contract."
        else:
            explanation += "."

        explanation += f" Their total pay is {self.get_pay()}."
        return explanation

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 'salary', salary=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 'hourly', hourly_wage=25, hours_worked=100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 'salary', salary=3000, contracts_landed=4, comms_per_contract=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan','hourly',hourly_wage=25, hours_worked=150, contracts_landed=3, comms_per_contract=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie','salary', salary=2000, bonus=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 'hourly', hourly_wage=30, hours_worked=120, bonus=600)

print(renee)
print(jan)
