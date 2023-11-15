""" Write a program that asks the user for an amount to invest,
the annual interest and the number of years, and display the capital
on the screen obtained in the investment rounded with two decimal places """


class InvestmentCalculator():
    def __init__(self):
        self.amount = 0
        self.annual_interest = 0
        self.year = 0

    def enter_data(self):
        while True:
            try:
                self.amount = float(
                    input("Enter the amount to want to invest: "))
                self.annual_interest = float(input(
                    "Enter the annual porcentage interest: "))
                self.year = int(input("Enter how many years: "))
                if self.amount < 0 or self.annual_interest < 0 or self.year < 0:
                    print("Enter a valid number")
                break
            except ValueError:
                print("You must enter a number")

    def obtain_result(self):
        return self.amount * ((self.annual_interest/100) + 1) ** self.year

    def show_result(self):
        total = self.obtain_result()
        print("Total amount ", round(total, 2))


calculator = InvestmentCalculator()
calculator.enter_data()
calculator.show_result()
