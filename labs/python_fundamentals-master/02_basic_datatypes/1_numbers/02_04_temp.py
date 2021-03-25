'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''

# create input to fahrenheit
fah = float(input("Please enter the temperature in fahrenheit: "))
# convert float "fah" do str to be presented in the result
fahr = str(fah)
# making the conversion ro celsius
cel = (fah - 32) * (5 / 9)
# convert float "cel" do str to be presented in the result
cels = str(cel)
print(fahr + " degrees fahrenheit = " + cels + " degrees celsius")
