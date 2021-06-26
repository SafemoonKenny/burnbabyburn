
# Importing necessary packages
from datetime import datetime, timedelta

def burn_calculation(circulating=580.828875377658,target_mc=1, target_price=0.001,limit = 10000):

    # Variables in Function
    # -- circulating: Circulating Supply of Safemoon
    # -- target_mc: Target Market Cap of Safemoon
    # -- target_price: Target End Price of Safemoon
    # -- limit: Maximum Number of Iterations of while loop
    
    # CURRENT MARKET DATA
    # ==============

    # Total Supply of Safemoon is 1 quadrillion or 1,000 trillion
    total_supply = 1000. # trillion

    # Current Burn Wallet Size
    burn_wallet = total_supply - circulating # trillion

    # TARGET SETTING
    # ==============
    
    # Target Circulating Supply
    target_circulating = target_mc * pow(10,9) / target_price / pow(10,12) # trillion
    
    # Required Total Burn
    required_burn = total_supply - target_circulating # trillion

    # INITIALISATION
    # ==============

    # Initialise day counter and daily burn
    counter = 0
    initial_price = 0.000004
    
    # WHILE LOOP
    # ==========

    while required_burn > burn_wallet:

        # Date Calculations
        counter += 1
        current_date = datetime.today() + timedelta(counter)

        # Maximum Number of Iterations
        if counter == limit:
            break


        # Daily Price and Volume Estimate
        if counter <= 30*1.5: # Pre-Wallet Release
            daily_price = initial_price # USD per SM
            daily_volume = 20 # million USD
        elif counter <= 30*6: # Wallet Released and Pre-Exchange
            daily_price = 0.00001 # USD per SM 
            daily_volume = 100 # million USD
        elif counter <= 30*12: # Exchange Released 
            daily_price = 0.00008 # USD per SM 
            daily_volume = 500 # million USD
        else: # Gambia Partnership Announced
            daily_price = 0.0001 # USD per SM                    
            daily_volume = 1000 # million USD

            
#        daily_price = 0.000002939
#        daily_volume = 14.95
        
        # Burn Reflection
        burned = (daily_volume*pow(10,6)) * (burn_wallet*pow(10,12)) / (20*pow(10,15)*daily_price) / pow(10,12) # trillion

        # Closing Balance
        circulating -= burned # trillion
        burn_wallet += burned # trillion

    else:

        if current_date.strftime("%d") == "01":
            suffix_d = "st"
        elif current_date.strftime("%d") == "02":
            suffix_d = "nd"
        elif current_date.strftime("%d") == "03":
            suffix_d = "rd"
        else:
            suffix_d = "th"
        
        if current_date.strftime("%m") == "01":
            suffix_m = "January"
        elif current_date.strftime("%m") == "02":
            suffix_m = "February"
        elif current_date.strftime("%m") == "03":
            suffix_m = "March"
        elif current_date.strftime("%m") == "04":
            suffix_m = "April"
        elif current_date.strftime("%m") == "05":
            suffix_m = "May"
        elif current_date.strftime("%m") == "06":
            suffix_m = "June"
        elif current_date.strftime("%m") == "07":
            suffix_m = "July"
        elif current_date.strftime("%m") == "08":
            suffix_m = "August"
        elif current_date.strftime("%m") == "09":
            suffix_m = "September"
        elif current_date.strftime("%m") == "10":
            suffix_m = "October"
        elif current_date.strftime("%m") == "11":
            suffix_m = "November"
        elif current_date.strftime("%m") == "12":
            suffix_m = "December"
        
        # Finalise print of result
        print(int(round(target_circulating,0))," TRILLION TIMING",sep="")
        print("===============================")
        print("Date reached: ",int(current_date.strftime("%d")),suffix_d," ",suffix_m," ",int(current_date.strftime("%Y")),sep="")
        print("Days:",counter)
        print("Months:",round(counter/30,1))
        print("Years:",round(counter/365,2)) 
        print("\nRETURN ON INVESTMENT")
        print("===============================")
        investment = 3500 # GBP
        average_buy = 0.0000035 # USD per SM
        print("Initial Investment:",investment)
        print("Ending Value:",int(round(investment*daily_price/average_buy,0)))
        print("Return:",round(pow(daily_price/average_buy,1/(int(current_date.strftime("%Y"))/365))-1,1)*100," %")
        
        

