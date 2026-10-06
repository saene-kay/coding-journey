print("what is your monthly premium in CHF?")  #ask the user for the monthly premium
premium = float(input(">"))
premiumYearly = premium * 12 #calculates the user's yearly premium (multiply by 12)
print(f"your yearly premium is: {premiumYearly:.2f}")
premiumReduced = premiumYearly * 0.95 #calculates the premium reduction due to annual payments
print("and because you pay annually your insurance premium is reduced: ")
print(f"your discounted premium is: {premiumReduced:.2f}")
