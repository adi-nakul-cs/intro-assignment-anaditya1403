from factorial import factorial

testcases = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
expectedresults = [1, 1, 2, 6, 24, 420, 720, 5040, 40320, 362880, 3628800] 

for i in range(len(testcases)):
    assert factorial(testcases[i]) == expectedresults[i]
print("All test cases pass")    
