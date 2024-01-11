import numpy as np
import pandas as pd
import timeit



class RealTime():
    
    def animatePlot(self):
        print('ehys')
    

    def animateHist(self):
         pass


    
    def animateRealTime():
        pass



def looper():
    for x in range(100):
        print(x)

n=5

print(globals())

x = RealTime()

result = timeit.timeit(stmt='looper()', globals=globals(), number=10)

print(result)