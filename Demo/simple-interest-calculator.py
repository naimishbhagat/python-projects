principal = int(input("Enter the amount borrowed: "))
years = float(input("Enter the period in years: "))
rate = float(input("Enter the rate of interest: ")) 

interest = (principal * years * rate) / 100
print(f'The simple interest for a total amount {principal} and period of years {years} and rate of interest {rate} is: {interest}')
print(f'The simple interest is: {interest}')