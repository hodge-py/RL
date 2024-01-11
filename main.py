import numpy as np
import pandas as pd
import timeit
import matplotlib.pyplot as plt



class RealTime():
    
    def animatePlot(self):
        print('ehys')
    

    def realTimeComplex(self,stmt='pass', globals=globals(), number=5):
         

        result = timeit.repeat(stmt=stmt, globals=globals, number=number)

        x = np.arange(1,number+1)
        y = np.asarray(result)
        print(x)

        m, b = np.polyfit(x, y, 1)

        plt.scatter(x,y)
        plt.plot(x,m*x+b)
        plt.show()

    
    def animateRealTime():
        pass



def looper():
    for x in range(100):
        print(x)

n=5

print(globals())

x = RealTime()

x.realTimeComplex(stmt='looper()')