'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

# user investment amount
inves = float(input("Please insert the amount do you want to invest: "))
# interest rate in percentage
inter = float(input("What's the interest rate: "))
interf = (inter / 100)
# number of years to invest
year = int(input("How many years do you want to invest : "))
# present result for total
juros = (inves * interf)
resul = ((juros * year) + inves)
print(resul)
# present results for the upcoming years