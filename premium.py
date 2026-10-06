print ("what is your monthly premium in CHF?")  #ask the user for the monthly premium
premium = input(">")
print ("your yearly premium is " + str(int(premium)*12)) #calculates the user's yearly premium (multiply by 12)
premiumYearly = str(int(premium)*12)
print ("and because you pay annually your insurance premium is reduced: ")
print ("your discounted premium is " + str(int(premiumYearly) * 0.95))
