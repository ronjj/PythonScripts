
# Script To Calculate The Amount Of Money I'll Make From Work
# Time Spent: ~30 minutes

def workToMoney(week1Hours, week2Hours):
    
    rate = 14.45

    week1Total = rate * week1Hours
    week2Total = rate * week2Hours

    total = week1Total + week2Total
    return total

# Amount To Invest - Only Investing If I Make Over $100 A Paycheck
hours1 = float(input("Week 1 Hours: "))
hours2 = float(input("Week 2 Hours: "))
result = workToMoney(hours1,hours2)

above100 = result > 100
if above100:
    thirtyPercent = result * .30


print(f"Glooks, gonna make ${round(result, 2)}. Investing 30% would be {round(thirtyPercent, 2)}." if above100 else f"Get those numbers up, only making ${round(result, 2)}")
