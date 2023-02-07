
# Script To Calculate The Amount Of Money I'll Make From Work 
# Also added the ability to get stock prices if I want to invest my money

# Time Spent: ~45 minutes

import yfinance as yf

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

if above100:
    wantToInvest = str(input("Do you want to invest?"))

    if wantToInvest == 'y':
        whereToInvest = str(input("Which stock do you want to invest in?"))
        stockInfo = yf.Ticker(whereToInvest)
        # stockInfoToDisplay = json.dumps(stockInfo.info, sort_keys=Fåalse, indent=4)

        print(f"The current price of {whereToInvest} is {stockInfo.info['ask']}")
        print(f"You could buy {thirtyPercent / int(stockInfo.info['ask']) } shares of {whereToInvest}.")
    
    else:
        print("ok")