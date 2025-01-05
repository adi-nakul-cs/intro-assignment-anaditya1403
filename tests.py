from temperature import celsiusToFahrenheit

test1 = celsiusToFahrenheit(37)
assert test1==98.60, f"Expected 98.60, got {test1}"

test2 = celsiusToFahrenheit(69.6556565)

test3 = celsiusToFahrenheit(101)

test4 = celsiusToFahrenheit(-273)

test5 = celsiusToFahrenheit(-280)