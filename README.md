# SpaceTimeComplex

This package was created to evaluate functions for time and space complexity. At the moment only time complexity is complete. The function runs an algorithm over and over with new
and increasing input sizes to judge the time complexity.

## Example

```python

import SpaceTimeComplex

def testone(n):
    for x in range(len(n[0])):
        for y in range(len(n[0])):
            two = y
            one = x

real = SpaceTimeComplex.RealTime() # Create the class

testSet = real.generateTestSet(type=0) #generate a test set

testSet1 = { # Test set example structure. Generated sets will only uses one type
            0: [4,"stnr=gwege"],
            1: [12,"sagsdgg"],
            2: [3,"esfsfsseafesfsefsef"]
            }

real.complexGuess(testone,testSet) #guess the complexity of a function. Returns the guess and a plot

```

![Figure_1](https://github.com/hodge-py/RealTime_Analysis/assets/105604814/fef612f2-ff1b-411a-b9b1-7d9ae8cd0af2)

![Screenshot 2024-01-15 020628](https://github.com/hodge-py/RealTime_Analysis/assets/105604814/b0b113f5-466d-4d21-9551-d3fd17e8a9bf)
