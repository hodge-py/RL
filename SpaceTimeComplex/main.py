import numpy as np
import pandas as pd
import timeit, gc
import matplotlib.pyplot as plt
import random
import string
import math
from sklearn.metrics import mean_squared_error
import statistics


"""A one-line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

Typical usage example:

  realTime = RealTime()
"""

class RealTime():
    
    """Summary of class here.

    

    Attributes:
        None

    """

    def animatePlot(self):
        print('ehys')
    

    def realTimeComplex(self,stmt='pass', globals=globals(), value=40):
        """
        Args:
            table_handle: An open smalltable.Table instance.
            keys: A sequence of strings representing the key of each table row to fetch.  String keys will be UTF-8 encoded.
            require_all_keys: If True only rows with values set for all keys will be returned.

        """
         
        
        result = timeit.repeat(stmt=stmt, globals=globals,repeat=value)
        
        x = np.arange(1,value+1)
        y = np.asarray(result) * 1000
        mean = np.mean(y)
        bottom90 = np.percentile(y,90)
        top10 = np.percentile(y,10)
        #write outputs to files eventually
        print(
            f"""
Mean is {round(mean,3)} ms
Bottom 90 is {round(bottom90,3)} ms
top 10 is {round(top10,3)} ms
            """ 
              )

        m, b = np.polyfit(x, y, 1)
        plt.scatter(x,y,zorder=0)
        plt.plot(x,m*x+b,zorder=3,c='green')
        plt.grid(zorder=-1.0)
        plt.axhline(y=mean, zorder=4)
        plt.axhline(y=bottom90,c='red')
        plt.axhline(y=top10,c='purple')
        plt.xlabel("Runs")
        plt.ylabel("Time (ms)")
        plt.show()



    
    def complexGuess(self,func,testSet):
        """
        Args:
            func (Function): Enter the callable name of a function
            testSet (Dict): Test set to be loop through. An example of the structure is given bellow.

        Returns:
            Pyplot: A plot of inputs against time
            Guess: Guesses what the time complexity by using RMSE of different curves.

        
        Example: 

            testSet = {
                0: [[0,3,2,3]], 
                1: [[0,3,2,4,3,2,2]], 
                2: [[343,23,4,234,3]],
                ... 
                }

        """

        gc.disable()

        arr = np.array([])
        inputSize = np.array([])

        for x in range(0,len(testSet)): #loop through every test set
            start = timeit.default_timer() #start the timer
            func(testSet[x])
            end = timeit.default_timer()
            arr = np.append(arr,[end-start])
            #loop through testSet and check for input size
            collect = 0
            for y in range(len(testSet[x])): #retrieve the value from test set
                if hasattr(testSet[x][y], '__len__'):
                    collect += len(testSet[x][y])
                else:
                    collect += testSet[x][y]

            inputSize = np.append(inputSize,collect)
        
        #x = np.arange(len(testSet)) # order by Runs
        x = inputSize # order by input size
        y = np.multiply(arr,1000)
        x2,y2 = (list(t) for t in zip(*sorted(zip(x, y))))
        graphx2 = x2
        graphy2 = y2
        print(f"x-values: {graphx2}")
        print(f"y-values: {graphy2}")

        x2 = np.log(x2)
        y2 = np.log(y2)

        log_fit, slopeCons = self.polyFunc(x2,y2,1)

        print(f"Algorithmn is of O(n^{slopeCons[0]}) time")
        print(f"Non-logarithmic function is T(N) = 2.71^({slopeCons[1]})*N^({slopeCons[0]})")
        # 2.71^constant*N^slope
        fig, (ax1,ax2) = plt.subplots(1,2)
        ax1.scatter(x2,y2, zorder=100)

        ax1.plot(x2,log_fit, c='red')
        ax2.scatter(graphx2,graphy2)
        plt.show()
        gc.enable()

        

    
    def polyFunc(self,x,y,degree):
        linear = np.polyfit(x,y,degree)
        trendpoly = np.poly1d(linear)
        print(trendpoly)
        fit_vals = [trendpoly(curr_t) for curr_t in x]
        return fit_vals, linear
    

    def treeComplex():
        pass
        
    def generateTestSet(self,amount = 50,type=0):
        """
        Args:
            amount (int): defines how many testing sets
            type (int): 0 = array, 1 = int, 2 = string

        Returns:
            dict: Value is an array. 

        Example:

            testSet = {
                0: [[0,3,2,3]],
                1: [[0,3,2,4,3,2,2]],
                2: [[343,23,4,234,3]]
                ...
            }


        """

        testSet = {}
        print(amount)
        for x in range(0,amount):
            if type == 0:
                testSet[x] = [np.random.randint(0,high=100, size=random.randint(5,100))]
            elif type == 1:
                testSet[x] = [random.randint(1,100)]
            elif type == 2:
                stringer = ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(1,50)))
                testSet[x] = [stringer]

        return testSet
    

    def spaceComplex():
        pass


    def combinedComplex():
        pass
        



