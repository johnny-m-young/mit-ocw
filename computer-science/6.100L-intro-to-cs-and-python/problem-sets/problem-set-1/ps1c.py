## 6.100A PSet 1: Part C
## Name:
## Time Spent:
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter the initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
cost_of_dream_home = 800000
portion_down_payment = 0.25
down_payment = cost_of_dream_home * portion_down_payment
months = 36
r0 = 0
r1 = 1
steps = 0
remainder = down_payment

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
if initial_deposit * ((1 + r1/12) ** months) < down_payment:
    r = None
else:
    while abs(remainder) >= 100:
        steps = steps + 1
        r = (r0 + r1) / 2
        amount_saved = initial_deposit * ((1 + r/12) ** months)
        remainder = amount_saved - down_payment
        
        if remainder > 0:
            r1 = r
        elif remainder < 0:
            r0 = r
        
    
print(f'Best savings rate: {r}')
print(f'Steps in bisection search: {steps}')
        