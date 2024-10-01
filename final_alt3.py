from time import sleep
from tqdm import tqdm
import random

#===================================================================================================================================================================================================================================================================

# Converts an input to a float value.

def float_conversion(amount, title): 
    while type(amount) != float:
        try:
            amount = float(amount)
            break
        except ValueError:
            amount = input(f"\n\tPlease enter {title} again: ")
    return amount    

#===================================================================================================================================================================================================================================================================
# Calculates the standard rate at the cut off point using geometric series formula to sum up all the taxes each year and
#     to predict the value of the standard cut off rate changes per year.

def standardrate_cutoff(time, income, monthly_income): 
    if income != 0:
        if income > 42000:
            difference = ((42000) * (1.05983) * (0.2) * ((1 - ((1.05983) * (0.2)) ** time))) / (1 - ((1.05983) * (0.2)))
            diff1 = difference
        elif income < 42000:
            difference = ((income) * (0.2) * ((1 - (0.2) ** time))) / (1 - (0.2))
            diff1 = difference
    elif income == 0:
        income = monthly_income * 12
        if income > 42000:
            difference = ((42000) * (1.05983) * (0.2) * ((1 - ((1.05983) * (0.2)) ** time))) / (1 - ((1.05983) * (0.2)))
            diff1 = difference
        elif income < 42000:
            difference = ((income) * (0.2) * ((1 - (0.2) ** time))) / (1 - (0.2))
            diff1 = difference
    return diff1
  
#===================================================================================================================================================================================================================================================================
  
# Finds the pay-related social insurance tax using math.

def prsi(monthly_income, income, time): 
    if monthly_income == 0:
        income_rate = ((income)/12) * 0.04
        diff3 = income_rate * 12 * time
        return diff3
    else:
        income_rate = monthly_income * 0.04
        diff3 = income_rate * 12 * time
        return diff3
    
#===================================================================================================================================================================================================================================================================

# Similar to standardrate_cutoff(), this function uses geometric series to find the standard rate after the cut off point.

def standardrate_cuton(time, income, monthly_income):
    if time > 0 or time < 0:
        if income != 0:
            if income > 42000:
                diff2 = (income)-42000
                diff2 = ((diff2) * (0.4) * ((1 - (0.4) ** time))) / (1 - (0.4))
            elif income < 42000:
                return 0
        elif income == 0:
            income = monthly_income * 12
            if income > 42000:
                diff2 = (income)-42000
                diff2 = ((diff2) * (0.4) * ((1 - (0.4) ** time))) / (1 - (0.4))
            elif income < 42000:
                return 0

    elif time == 0:
        if income != 0:
            if income < 42000:
                diff2 = (income)
                diff2 = (diff2*(0.4))
                return diff2
            diff2 = (income)-42000
            diff2 = ((diff2) * (0.4) * ((1 - (0.4) ** time))) / (1 - (0.4))
        elif income == 0:
            income = monthly_income * 12
            if income < 42000:
                return 0
            diff2 = (income)-42000
            diff2 = ((diff2) * (0.4) * ((1 - (0.4) ** time))) / (1 - (0.4))
            
        return diff2
        
#===================================================================================================================================================================================================================================================================

# Finds the universal social charge of the income and sums up each year, returning the overall difference to be taken away from the final balance and income.
# Takes in medical card and age details as well.

def usc(income, status, age, monthly_income, years):
    if income != 0:
        if income >= 13000:
            band1 = 12012 * 0.005
            band2 = 13748 * 0.02
            band3 = (income - (12012+13748)) * 0.04
            diff4 = (band1 + band2 + band3) * years
            return diff4   
        elif (status.lower() in {"Y", "Yes", "yes", "y"}) or (income < 60000 and age > 70):
            if income < 13000:
                return 0#brackets error
            else:
                band1 = 12012 * 0.005
                band3 = (income - 12012) * 0.02
                diff4 = (band1 + band3) * years
                return diff4
        elif income < 13000:
            return 0
            
    elif income == 0:
        income = monthly_income * 12
        if income >= 13000:
            band1 = 12012 * 0.005
            band2 = 13748 * 0.02
            band3 = (income - (12012+13748)) * 0.04
            diff4 = (band1 + band2 + band3) * years
            return diff4   
        elif (status.lower() in {"Y", "Yes", "yes", "y"}) or (income < 60000 and age > 70): 
            if income < 13000:
                return 0
            else:
                band1 = 12012 * 0.005
                band3 = (income - 12012) * 0.02
                diff4 = (band1 + band3) * years
                return diff4
        elif income < 13000:
            return 0

#===================================================================================================================================================================================================================================================================
    
# Checks if the input was a valid answer
def status_check(status):
    while status.lower() not in  {"Y", "Yes", "yes", "y", "n", "no", "No", "N",}:
        status = input("\n\tPlease enter a valid answer (Y/N): ")
    return status.lower()

#===================================================================================================================================================================================================================================================================

# Checks if the age is a reasonable number

def age_check(age):
    while True:
        if age < 0 or age > 117:
            age = input("\n\tPlease enter a valid age: ")
            age = float_conversion(age, "your age")
        elif age > 0 and age < 117:
            break
    
    return age

#===================================================================================================================================================================================================================================================================

# Switches between yearly or monthly income, depending on the input. (list[3] is monthly income and list[2] is yearly)

def income_choice(income_choice, list):
    while income_choice.lower() not in {"yearly income", "monthly income", "Yearly Income", "Monthly Income", "yi", "mi", "y", "m", "yearly", "monthly", "YEARLY", "MONTHLY"}:
        income_choice = input("\n\tPlease enter your choice again: ")
    if income_choice.lower() in {"yearly income", "Yearly Income", "yi", "y", "yearly", "YEARLY"}:
        list[3] = 0
    else:
        list[2] = 0
    return list

#===================================================================================================================================================================================================================================================================

# Used in the final calculation (see function below) and checks which income is vacant, using that value. Could be improved upon.

def income_swap(yearly_income, monthly_income):
    if yearly_income == 0:
        yearly_income = monthly_income * 12
    else:
        yearly_income = yearly_income
    return yearly_income

#===================================================================================================================================================================================================================================================================

# The final calculation, uses all the functions and determines a final value

def total_balance(balance, yearly_income, diff1, diff2, time, diff3, diff4, monthly_income):
    income = income_swap(yearly_income, monthly_income)
    totalbal = (balance+(income*time))-(diff1+diff2+diff3+diff4)
    return round(totalbal, 2)

#===================================================================================================================================================================================================================================================================

# If the difference is a negative, the function tells you how far you are from your target and removes the negative sign.
# If it is positive, it tells you how much money you are above your target

def target_difference(balance, target):
    difference = target - balance
    if difference < 0:
        print(f"\n\tYou are ", "€" + str(round(((-1 * difference)), 2)), "above your target")
    elif difference > 0:
        print(f"\n\tYou are ", "€" + str(round(difference)), "away from your target")

#===================================================================================================================================================================================================================================================================
#===================================================================================================================================================================================================================================================================

# Main program - Introduction

print("\n\t----------------------------------")

print("\tHello, welcome to your personal Net Balance Simulator\n(NB - this simulator assumes you are calculating as a single person)")

#===================================================================================================================================================================================================================================================================

# List creation.

list = [0, 0, 0, 0, 0]
list2 = ["your current account balance", "the amount of years you want to predict", "your yearly gross income", "your monthly gross income", "your target balance"]

#===================================================================================================================================================================================================================================================================

# Funny Quips

list3= ["Thanks for being a keyboard wiz!",
    "You're the Ctrl to my C!",
    "Thanks for typing like a boss!",
    "You're the key to my heart, and my data!",
    "Thanks for pressing all the right buttons!",
    "You're the QWERTY to my happiness!",
    "Thanks for being a space bar superstar!",
    "You're the ESC to my stress!",
    "Thanks for making data entry a breeze!",
    "You're the CAPS LOCK to my excitement!",]

#===================================================================================================================================================================================================================================================================

# Inputs

for i in range(len(list)):
    print("\n\t----------------------------------")
    list[i] = input(f"\n\tPlease enter {list2[i]}: ")
    list[i] = float_conversion(list[i], list2[i])
    print("\n\t", list3[random.randint(0, len(list3)-1)])
    print("\n")
    for i in tqdm(range(2)):
        sleep(0.5)



print("\n\t----------------------------------")
choice = input("\n\tWhich would you like to calculate? Yearly income or monthly income: ").strip()
print("\n\t", list3[random.randint(0, len(list3)-1)])
print("\n")
for i in tqdm(range(2)):
        sleep(0.5)

list = income_choice(choice, list)

print("\n\t----------------------------------")
status = input("\n\tDo you have a medical card (Y/N): ").strip()
print("\n\t", list3[random.randint(0, len(list3)-1)])
print("\n")
for i in tqdm(range(2)):
        sleep(0.5)
status = status_check(status)

print("\n\t----------------------------------")
age = input("\n\tPlease enter your age: ")
print("\n\t", list3[random.randint(0, len(list3)-1)])
print("\n")
for i in tqdm(range(2)):
        sleep(0.5)

age = float_conversion(age, "your age")
age = age_check(age)

#===================================================================================================================================================================================================================================================================

# Variable Assignment

balance = list[0]
years = list[1]
yearly_income = list[2]
monthly_income = list[3]
target_bal = list[4]

# these assignments could have been made in the total_balance() function
diff1 = standardrate_cutoff(years, yearly_income, monthly_income)
diff2 = standardrate_cuton(years, yearly_income, monthly_income)
diff3 = prsi(monthly_income, yearly_income, years)
diff4 = usc(yearly_income, status, age, monthly_income, years)
list_diff = [diff1, diff2, diff3, diff4]

#===================================================================================================================================================================================================================================================================

# Checks for None types
for i in range(0, 3):
    if list_diff[i] == None:
       list_diff[i] = 0


# the income swap couldve been made at the start
#===================================================================================================================================================================================================================================================================

# Final Balance and Differences

totalbal = total_balance(balance, yearly_income, list_diff[0], list_diff[1], years, list_diff[2], list_diff[3], monthly_income)
print("\n\t----------------------------------")
print("\n")
for i in tqdm(range(20)):
    sleep(0.5)
print("\n\t----------------------------------")


print(f"\n\tHere is your predicted net balance after {list[1]} years: ", "€" + str(totalbal))
target_diff = target_difference(totalbal, target_bal)
print("\n\t----------------------------------")
print("\n")


