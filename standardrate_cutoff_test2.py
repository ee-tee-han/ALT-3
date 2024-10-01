def standardrate_cutoff(time, income, monthly_income): # calculates the standard rate at the cut off point using geometric series formula to sum up all the taxes each year and to predict the value of the standard cut off rate changes per year.

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

def standardrate_cutoff1(time, income, monthly_income): # calculates the standard rate at the cut off point using geometric series formula to sum up all the taxes each year and to predict the value of the standard cut off rate changes per year.
    standardrate = []
    if income != 0:
        if income > 42000:
            difference = ((42000) * (1.05983) * (0.2) * ((1 - ((1.05983) * (0.2)) ** time))) / (1 - ((1.05983) * (0.2)))
            standardrate.append(difference)
            diff1 = sum(standardrate)
        elif income < 42000:
            difference = ((income) * (0.2) * ((1 - (0.2) ** time))) / (1 - (0.2))
            standardrate.append(difference)
            diff1 = sum(standardrate)
    elif income == 0:
        income = monthly_income * 12
        if income > 42000:
            difference = ((42000) * (1.05983) * (0.2) * ((1 - ((1.05983) * (0.2)) ** time))) / (1 - ((1.05983) * (0.2)))
            standardrate.append(difference)
            diff1 = sum(standardrate)
        elif income < 42000:
            difference = ((income) * (0.2) * ((1 - (0.2) ** time))) / (1 - (0.2))
            standardrate.append(difference)
            diff1 = sum(standardrate)
    return diff1
while True: 
    time = int(input("time:"))
    income = int(input("income:"))

    if standardrate_cutoff1(time, income, 0) == standardrate_cutoff(time, income, 0):
        print("Passed")
    else:
        print("Failed")