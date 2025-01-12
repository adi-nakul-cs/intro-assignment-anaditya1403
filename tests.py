from temperature import celsiusToFahrenheit
test1 = celsiusToFahrenheit(37)
#assert test1 == 98.60, "Expected answer is 98.60"
print(f"Test 1 passed: {test1:.2f}")

test2 = celsiusToFahrenheit(0)
print(f"Test 2 passed: {test2:.2f}")

test3 = celsiusToFahrenheit(-273)
print(f"Test 3 passed: {test3:.2f}")

test4 = celsiusToFahrenheit(100)
print(f"Test 4 passed: {test4:.2f}")

test5 = celsiusToFahrenheit(101)
print(f"Test 5 passed: {test5:.2f}")

test6 = celsiusToFahrenheit(69.696969)
print(f"Test 6 passed: {test6:.2f}")

test7 = celsiusToFahrenheit(-273.15)
print(f"Test 7 passed: {test7:.2f}")