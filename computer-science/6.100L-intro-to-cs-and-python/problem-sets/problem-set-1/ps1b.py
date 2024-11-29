## 6.100A PSet 1: Part B
## Name:
## Time Spent:
## Collaborators:

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25
down_payment = portion_down_payment * cost_of_dream_home
monthly_savings = yearly_salary * portion_saved / 12
amount_saved = 0
r = 0.05
months = 0

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
while amount_saved < down_payment:
    amount_saved = amount_saved * (1 + r/12) + monthly_savings

    if months > 0 and months % 6 == 0:
        yearly_salary = yearly_salary * (1 + semi_annual_raise)
        monthly_savings = yearly_salary * portion_saved / 12

    months = months + 1
    

print(f'Number of months: {months}')