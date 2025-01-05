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
print("salamalikum")

def celsiusToFahrenheit(celsius):
    fahrenheit = (celsius*1.8) + 32
    assert celsius>-273, "NO VALUE OF TEMPERATURE CAN BE LESS THAN ABSOLUTE 0"
    assert celsius<100, "MAX. value in celsius scale is 100"
    return fahrenheit

celsius = float(input("Enter the Degree celsius temperature bossu:"))
fahrenheit = celsiusToFahrenheit(celsius)
print("The temperature in the fahrenheit scale is bossu:",round(fahrenheit,2))


test1 = celsiusToFahrenheit(37)

test2 = celsiusToFahrenheit(69.6556565)

test3 = celsiusToFahrenheit(101)

test4 = celsiusToFahrenheit(-273)

test5 = celsiusToFahrenheit(-280)


#Enter the Degree celsius temperature bossu:37
#The temperature in th fahrenheit scale is bossu: 98.60000000000001
#PS C:\Users\Admin\OneDrive\Documents\GitHub\adi-nakul-cs-classroom-c2987d-intro-assignment-lab->

#69
#Enter the Degree celsius temperature bossu:69
#The temperature in th fahrenheit scale is bossu: 156.2
#PS C:\Users\Admin\OneDrive\Documents\GitHub\adi-nakul-cs-classroom-c2987d-intro-assignment-lab->


#Enter the Degree celsius temperature bossu:273
#The temperature in th fahrenheit scale is bossu: 523.4000000000001
#PS C:\Users\Admin\OneDrive\Documents\GitHub\adi-nakul-cs-classroom-c2987d-intro-assignment-lab-> 

#Enter the Degree celsius temperature bossu:0
#The temperature in th fahrenheit scale is bossu: 32.0
#PS C:\Users\Admin\OneDrive\Documents\GitHub\adi-nakul-cs-classroom-c2987d-intro-assignment-lab-

#Enter the Degree celsius temperature bossu:100
#The temperature in th fahrenheit scale is bossu: 212.0
#PS C:\Users\Admin\OneDrive\Documents\GitHub\adi-nakul-cs-classroom-c2987d-intro-assignment-lab-