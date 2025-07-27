"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and 
an amount. It prints out the result of converting the first currency to 
the second.

Author: Shelly Zhou sz498
Date:   09/15/2022
"""
import a1
old = str(input('Enter original currency: '))
new = str(input('Enter desired currency: '))
amt = float(input('Enter original amount: '))
result = a1.exchange(old, new, amt)
print('You can exchange '+ str(amt)+' '+str(old)+' '+'for '+str(result)+' '+str(new)+'.')