'''
You will write a function called "celsiusToFahrenheit" to convert temperature in Celsius to Fahrenheit. These two values are related by the formula: celsius * 1.8 = fahrenheit – 32

As an input to the program, you will have to prompt the user to enter a value in Celsius. For prompting
and accepting the user for an input, use input(msg) in your code. It presents a prompt to the user (you
will have to replace ‘msg’ with a prompt message in quotes), gets input from the user and stores the
input entered by the user in a string. You will have to write code for displaying the equivalent Fahrenheit
value on screen.
Test your function with known inputs to verify if your output is correct or not.
Nakul Nayak
12:05 AM
assert keyword
if value is incorrect print: "Test 1 failed"
Nakul Nayak
12:07 AM
2. round to 2 decimal places


'''


def celsiusToFahrenheit(celsius):
    fahrenheit = (celsius*1.8) + 32
    return fahrenheit

if __name__ == "__main__":
    print("__name__ is:",__name__)
    celsius = float(input("Enter the Degree celsius temperature Boss:"))
    fahrenheit = celsiusToFahrenheit(celsius)
    print("The temperature in the fahrenheit scale is:")
    print(f"{fahrenheit:.2f}")

